import json
import requests
from datetime import datetime
import os

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
        return field.get('en-US', '')  # Assume 'en-US' localization, use empty string if not found
    elif isinstance(field, str):
        return field  # If it's already a plain string, return it as is
    return ''  # Return an empty string if field is None or unexpected type

def get_asset_url(asset):
    """Extract the URL from a Contentful asset."""
    file_field = asset.get('fields', {}).get('file')
    # Debugging statements
    # print("Asset ID:", asset.get('sys', {}).get('id'))
    # print("file_field:", file_field)
    if isinstance(file_field, dict):
        # Assume 'en-US' localization
        file_info = file_field.get('en-US', {}) if 'en-US' in file_field else next(iter(file_field.values()))
    else:
        file_info = file_field  # Could be a string or None
    # print("file_info:", file_info)
    if isinstance(file_info, dict):
        url = file_info.get('url', '')
    elif isinstance(file_info, str):
        url = file_info  # Assume it's already the URL
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

def rich_text_to_markdown(node, list_type=None):
    """Recursively convert Contentful Rich Text node to Markdown."""
    node_type = node.get('nodeType')
    content = node.get('content', [])

    if node_type == 'document':
        # Process all top-level content nodes
        return '\n\n'.join(rich_text_to_markdown(child) for child in content)
    elif node_type == 'paragraph':
        # Process paragraph content
        return ''.join(rich_text_to_markdown(child) for child in content)
    elif node_type.startswith('heading-'):
        level = int(node_type[-1])
        return '#' * level + ' ' + ''.join(rich_text_to_markdown(child) for child in content)
    elif node_type == 'unordered-list':
        # Process each list item
        return '\n'.join(rich_text_to_markdown(child, list_type='ul') for child in content)
    elif node_type == 'ordered-list':
        return '\n'.join(rich_text_to_markdown(child, list_type='ol') for child in content)
    elif node_type == 'list-item':
        # list_type should be passed from parent
        prefix = '- ' if list_type == 'ul' else '1. '
        # Process the child nodes, which may be 'paragraph's
        item_content = ''.join(rich_text_to_markdown(child, list_type=list_type) for child in content)
        return prefix + item_content
    elif node_type == 'hyperlink':
        # Generate Markdown link
        url = node.get('data', {}).get('uri', '')
        text = ''.join(rich_text_to_markdown(child) for child in content)
        return f'[{text}]({url})'
    elif node_type == 'text':
        value = node.get('value', '')
        marks = node.get('marks', [])
        for mark in marks:
            mark_type = mark.get('type')
            if mark_type == 'bold':
                value = f'**{value}**'
            elif mark_type == 'italic':
                value = f'*{value}*'
            elif mark_type == 'underline':
                value = f'<u>{value}</u>'
            elif mark_type == 'code':
                value = f'`{value}`'
        return value
    else:
        # For other node types, return empty string or handle accordingly
        return ''

def get_body_content(body_field):
    """Convert Contentful Rich Text body field to Markdown."""
    if isinstance(body_field, dict):
        return rich_text_to_markdown(body_field)
    elif isinstance(body_field, str):
        return body_field  # If it's plain text, return as-is
    return ""  # Return empty string if body_field is None or unexpected type

def create_markdown_file(entry, assets):
    """Create a Markdown file for a Contentful entry."""
    fields = entry.get('fields', {})

    # Fetch title, slug, date, and body, handling both localized dictionaries and plain strings
    title = get_field_value(fields.get('title'))
    slug = get_field_value(fields.get('slug'))
    date = get_field_value(fields.get('date'))
    body = get_body_content(fields.get('body'))
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
    if not title or not slug or not date or not body:
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
    slug = get_field_value(item.get('fields', {}).get('slug'))
    if slug:
        current_slugs.add(slug)
    create_markdown_file(item, assets)

# Remove Markdown files for unpublished content
remove_unpublished_files(current_slugs)
