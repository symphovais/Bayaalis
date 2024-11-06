import json
import requests
from datetime import datetime
import os

# Configuration
SPACE_ID = 'slui2y4fqnvv'
ENVIRONMENT_ID = 'master'  # Usually 'master'
ACCESS_TOKEN = 'v2DFDE4HB77cFBdosY5nl0-L910jvBPOGJWeWVhCtJs'
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

def fetch_entries():
    """Fetch entries from Contentful."""
    params = {'content_type': CONTENT_TYPE_ID}
    response = requests.get(BASE_URL, headers=headers, params=params)
    response.raise_for_status()
    return response.json()

def get_field_value(field):
    """Helper function to get the value of a field, handling both localized and plain strings."""
    if isinstance(field, dict):
        return field.get('en-US', '')  # Assume 'en-US' localization, use empty string if not found
    elif isinstance(field, str):
        return field  # If it's already a plain string, return it as is
    return ''  # Return an empty string if field is None or unexpected type

def get_body_content(body_field):
    """Extract text from a Contentful Rich Text body field."""
    if isinstance(body_field, dict) and body_field.get('nodeType') == 'document':
        content = []
        for node in body_field.get('content', []):
            if node.get('nodeType') == 'paragraph':
                paragraph_text = "".join(
                    child.get('value', '') for child in node.get('content', []) if child.get('nodeType') == 'text'
                )
                content.append(paragraph_text)
        return "\n\n".join(content)  # Join paragraphs with double newline
    elif isinstance(body_field, str):
        return body_field  # If it's plain text, return as-is
    return ""  # Return empty string if body_field is None or an unexpected type

def create_markdown_file(entry):
    """Create a Markdown file for a Contentful entry."""
    fields = entry.get('fields', {})

    # Fetch title, slug, date, and body, handling both localized dictionaries and plain strings
    title = get_field_value(fields.get('title'))
    slug = get_field_value(fields.get('slug'))
    date = get_field_value(fields.get('date'))
    
    # Print the body field structure to understand its format for troubleshooting
    print("Body field structure:", fields.get('body'))

    # Use the new function to handle Rich Text conversion
    body = get_body_content(fields.get('body'))

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
description: "{fields.get('description', {}).get('en-US', '')}"
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

# Fetch entries and create Markdown files
entries = fetch_entries()
for item in entries['items']:
    create_markdown_file(item)