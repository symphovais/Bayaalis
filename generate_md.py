import json
import requests
from datetime import datetime
import os
from contentful_rich_text import RichTextRenderer

# Configuration using environment variables
SPACE_ID = os.getenv('CONTENTFUL_SPACE_ID')
ENVIRONMENT_ID = os.getenv('CONTENTFUL_ENVIRONMENT_ID', 'master')  # Default to 'master'
ACCESS_TOKEN = os.getenv('CONTENTFUL_ACCESS_TOKEN')
CONTENT_TYPE_ID = 'article'  # e.g., 'blogPost'

# API Endpoint for entries
BASE_URL = f'https://cdn.contentful.com/spaces/{SPACE_ID}/environments/{ENVIRONMENT_ID}/entries'

# Headers for the API request
headers = {
    'Authorization': f'Bearer {ACCESS_TOKEN}'
}

# Folder to save Markdown files
OUTPUT_FOLDER = 'content/blog'

# Ensure output directory exists
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Initialize the Rich Text renderer
renderer = RichTextRenderer()

def fetch_all_entries():
    """Fetch all entries from Contentful, handling pagination."""
    entries = []
    assets = {}
    limit = 100  # Maximum per request
    skip = 0
    total = None

    while True:
        params = {
            'content_type': CONTENT_TYPE_ID,
            'limit': limit,
            'skip': skip,
            'include': 2  # Include linked assets and entries
        }
        response = requests.get(BASE_URL, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()
        entries.extend(data.get('items', []))
        # Build assets dictionary
        includes = data.get('includes', {})
        for asset in includes.get('Asset', []):
            assets[asset['sys']['id']] = asset
        if total is None:
            total = data.get('total', 0)
        skip += limit
        if skip >= total:
            break

    return entries, assets

def get_field_value(field):
    """Helper function to get the value of a field, handling both localized and plain strings."""
    if isinstance(field, dict):
        return field.get('en-US', '')  # Assume 'en-US' localization
    elif isinstance(field, str):
        return field
    return ''

def get_asset_url(asset):
    """Extract the URL from a Contentful asset."""
    file_field = asset.get('fields', {}).get('file')
    if isinstance(file_field, dict):
        # Assume 'en-US' localization
        file_info = file_field.get('en-US', {}) if 'en-US' in file_field else next(iter(file_field.values()))
    else:
        file_info = file_field
    if isinstance(file_info, dict):
        url = file_info.get('url', '')
    elif isinstance(file_info, str):
        url = file_info
    else:
        print(f"Unexpected file_info type: {type(file_info)}")
        return ''
    if url:
        if url.startswith('//'):
            url = 'https:' + url
        elif url.startswith('/'):
            url = 'https://images.ctfassets.net' + url
        return url
    return ''

def get_body_content(fields):
    """Get the body content, preferring mdBody over body."""
    md_body_field = fields.get('mdBody')
    md_body = get_field_value(md_body_field)

    if md_body:
        # Use mdBody content directly
        return md_body.strip()
    else:
        # Use the body field
        body_field = fields.get('body')
        if isinstance(body_field, dict):
            # Render Rich Text to HTML and include it as-is
            html_content = renderer.render(body_field)
            return html_content.strip()
        elif isinstance(body_field, str):
            return body_field.strip()
        else:
            return ""

def create_markdown_file(entry, assets):
    """Create a Markdown file for a Contentful entry."""
    fields = entry.get('fields', {})
    sys_data = entry.get('sys', {})

    # Fetch title, slug, date, and body
    title = get_field_value(fields.get('title'))
    slug = get_field_value(fields.get('slug'))
    date = get_field_value(fields.get('date'))
    body = get_body_content(fields)
    description = get_field_value(fields.get('description'))

    # Get featuredImage URL
    featured_image_url = ''
    featured_image_field = fields.get('featuredImage')
    if featured_image_field:
        image_link = featured_image_field.get('sys', {})
        if image_link.get('type') == 'Link' and image_link.get('linkType') == 'Asset':
            asset_id = image_link.get('id')
            asset = assets.get(asset_id)
            if asset:
                featured_image_url = get_asset_url(asset)
            else:
                print(f"Asset with ID {asset_id} not found in assets.")
        else:
            print(f"Invalid image_link structure: {image_link}")

    # Check for required fields and skip entry if any are missing
    if not title or not slug or not date:
        print(f"Skipping entry due to missing required fields: {entry}")
        return

    # Format date to ISO 8601 with "Z" timezone
    try:
        formatted_date = datetime.fromisoformat(date.replace("Z", "+00:00")).strftime("%Y-%m-%dT%H:%M:%SZ")
    except ValueError:
        print(f"Skipping entry due to invalid date format: {date}")
        return

    # Metadata for Markdown file
    md_content = f"""---
title: "{title}"
description: "{description}"
summary: ""
date: {formatted_date}
lastmod: {formatted_date}
draft: false
weight: 50
categories: []
tags: []
contributors: []
pinned: false
homepage: false
featuredImage: "{featured_image_url}"
seo:
  title: "" # custom title (optional)
  description: "" # custom description (recommended)
  canonical: "" # custom canonical URL (optional)
  robots: "" # custom robot tags (optional)
---

{body}
"""

    # Write to a Markdown file
    file_path = os.path.join(OUTPUT_FOLDER, f"{slug}.md")
    with open(file_path, 'w', encoding='utf-8') as md_file:
        md_file.write(md_content)
    print(f"Markdown file created for '{title}' at {file_path}")

def remove_unpublished_files(current_slugs):
    """Remove markdown files for content that is no longer published."""
    for filename in os.listdir(OUTPUT_FOLDER):
        if filename.endswith('.md'):
            slug = filename[:-3]  # Remove '.md' extension
            if slug not in current_slugs:
                file_path = os.path.join(OUTPUT_FOLDER, filename)
                os.remove(file_path)
                print(f"Removed unpublished content file: {file_path}")

# Fetch entries and assets
entries, assets = fetch_all_entries()
current_slugs = set()

# Process entries and create Markdown files
for item in entries:
    # Check if the entry is published
    if item.get('sys', {}).get('publishedVersion') is None:
        # Remove the Markdown file if it exists
        slug = get_field_value(item.get('fields', {}).get('slug'))
        if slug:
            file_path = os.path.join(OUTPUT_FOLDER, f"{slug}.md")
            if os.path.exists(file_path):
                os.remove(file_path)
                print(f"Removed unpublished content file: {file_path}")
        continue

    slug = get_field_value(item.get('fields', {}).get('slug'))
    if slug:
        current_slugs.add(slug)
    create_markdown_file(item, assets)

# Remove Markdown files for unpublished content
remove_unpublished_files(current_slugs)
