#!/usr/bin/env node

/**
 * Sync Contentful "Chapter" entries to Hugo content directory.
 */

const fs = require('fs');
const path = require('path');
const { createClient } = require('contentful');
require('dotenv').config();

const { CONTENTFUL_TOKEN, SPACE_ID, ENVIRONMENT_ID = 'master' } = process.env;

if (!CONTENTFUL_TOKEN || !SPACE_ID) {
  console.error('Error: Missing required environment variables CONTENTFUL_TOKEN or SPACE_ID.');
  console.error('Please ensure you have a .env file with these values.');
  process.exit(1);
}

const client = createClient({
  space: SPACE_ID,
  accessToken: CONTENTFUL_TOKEN,
  environment: ENVIRONMENT_ID,
});

// The output directory for your markdown files
const outDir = path.join(process.cwd(), 'content', 'docs', 'guides');

// Ensure the output directory exists
fs.mkdirSync(outDir, { recursive: true });

// A simple function to create URL-friendly slugs
function slugify(str) {
    if (!str) return '';
    return str
        .toLowerCase()
        .trim()
        .replace(/[^a-z0-9\s-]/g, '') // remove invalid chars
        .replace(/\s+/g, '-') // collapse whitespace and replace by -
        .replace(/-+/g, '-'); // collapse dashes
}

async function syncContentful() {
  console.log('Fetching entries from Contentful...');
  try {
    const entries = await client.getEntries({
      content_type: 'chapter', // Using the 'chapter' content type from your screenshot
      limit: 1000,
      order: 'fields.order', // Sort by the 'order' field, ascending
    });

    if (entries.items.length === 0) {
        console.log('No entries of type "chapter" found in Contentful.');
        return;
    }

    console.log(`Found ${entries.items.length} chapters. Writing to markdown files...`);

    for (const item of entries.items) {
      const { title, slug, body, order, tags } = item.fields;
      const fileName = slug ? slugify(slug) : slugify(title);

      if (!fileName) {
          console.warn(`Skipping entry with ID ${item.sys.id} because it has no title or slug.`);
          continue;
      }
      
      // --- Build the Frontmatter ---
      let frontmatter = '---\n';
      frontmatter += `title: "${title || ''}"\n`;
      frontmatter += `date: ${item.sys.updatedAt}\n`;
      if (order) {
        // Use 'weight' for ordering pages in Hugo
        frontmatter += `weight: ${order}\n`; 
      }
      if (tags && tags.length > 0) {
        frontmatter += `tags: [${tags.map(t => `"${t}"`).join(', ')}]\n`;
      }
      frontmatter += '---\n\n';

      const fileContent = frontmatter + (body || '');
      const filePath = path.join(outDir, `${fileName}.md`);

      fs.writeFileSync(filePath, fileContent, 'utf8');
    }

    console.log(`✅ Successfully synced ${entries.items.length} chapters to ${outDir}`);
  } catch (error) {
    console.error('Error syncing content from Contentful:', error);
    process.exit(1);
  }
}

syncContentful();