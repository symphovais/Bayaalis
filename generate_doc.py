import json
import requests
from datetime import datetime
import os

# Configuration using environment variables
SPACE_ID = "slui2y4fqnvv"
ENVIRONMENT_ID = os.getenv('CONTENTFUL_ENVIRONMENT_ID', 'master')  # Default to 'master'
ACCESS_TOKEN = "v2DFDE4HB77cFBdosY5nl0-L910jvBPOGJWeWVhCtJs"
CONTENT_TYPE_ID = 'documentationTopic-2'  # e.g., 'blogPost'
# API Endpoint for entries
BASE_URL = f'https://cdn.contentful.com/spaces/{SPACE_ID}/environments/{ENVIRONMENT_ID}/entries'

# Headers for the API request
headers = {
    'Authorization': f'Bearer {ACCESS_TOKEN}'
}

# Folder to save Markdown files
OUTPUT_FOLDER = 'content/docs/guides'

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
        return field.get('en-US', '')  # Assume 'en-US' localization
    elif isinstance(field, str):
        return field
    return ''

def get_body_content(fields):
    """Get the body content from the 'contentMd' field."""
    md_body_field = fields.get('contentMd')  # Note the field ID is 'contentMd', matching your content type
    md_body = get_field_value(md_body_field)
    return md_body.strip() if md_body else ""

def create_markdown_file(entry):
    """Create a Markdown file for a Contentful entry."""
    fields = entry.get('fields', {})
    sys_data = entry.get('sys', {})

    # Fetch title, slug, date, and body
    title = get_field_value(fields.get('title'))
    slug = get_field_value(fields.get('slug'))
    body = get_body_content(fields)
    description = ""  # Set to empty or use another field if available

    # Use 'updatedAt' or 'createdAt' from sys data as date
    date = sys_data.get('createdAt') or sys_data.get('updatedAt')

    # Format date to ISO 8601 with "Z" timezone
    try:
        formatted_date = datetime.fromisoformat(date.replace("Z", "+00:00")).strftime("%Y-%m-%dT%H:%M:%SZ")
    except (ValueError, TypeError):
        print(f"Skipping entry due to invalid date format: {date}")
        return

    # Metadata for Markdown file
    md_content = f"""---
title: "{title}"
description: "{description}"
date: {formatted_date}
draft: false
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
entries, _ = fetch_all_entries()
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
    create_markdown_file(item)

# Remove Markdown files for unpublished content
remove_unpublished_files(current_slugs)