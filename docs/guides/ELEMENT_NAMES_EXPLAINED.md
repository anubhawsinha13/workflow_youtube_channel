# Creatomate Element Names - Complete Guide

## What Are Element Names?

**Element names** are identifiers for the dynamic parts of your Creatomate template. They tell Creatomate which parts of your video template should be replaced with your content (images, audio, text).

Think of it like placeholders in a document:
- Template has: `[Image-1]`, `[Voiceover-1]`, `[Text-1]`
- Your code sends: `Image-1.source = "your_image_url"`
- Creatomate replaces: `[Image-1]` with your image

## How Element Names Work

### In Your Creatomate Template

When you create a template in Creatomate, each element (image, video, text, audio) has a **name**. This name is what you use in the API to modify that element.

**Example Template Structure:**
```
Template: "My Video Template"
├── Image Element (name: "Image-1")
├── Audio Element (name: "Voiceover-1")
├── Text Element (name: "Text-1")
└── Image Element (name: "Image-2")
```

### In the API Payload

You reference these elements using **dot notation** in the modifications object:

```json
{
  "template_id": "your-template-id",
  "modifications": {
    "Image-1.source": "https://your-image-url.jpg",
    "Voiceover-1.source": "https://your-audio-url.mp3",
    "Text-1.text": "Your dialogue text here"
  }
}
```

## Element Name Format

### Basic Format
```
{ElementName}.{Property} = {Value}
```

### Common Properties
- **`.source`** - For images, videos, and audio (the file URL)
- **`.text`** - For text elements (the text content)
- **`.trim`** - For audio/video (start time in seconds)
- **`.volume`** - For audio (0-100)

### Examples from Your Template (creatomate.txt)

```json
{
  "1PC-Photo.source": "https://...",           // Image element named "1PC-Photo"
  "MPP-Photo-1.source": "https://...",         // Image element named "MPP-Photo-1"
  "IT-Text.text": "in loving memory of",       // Text element named "IT-Text"
  "ID-Date.text": "12.2.2002 ~ 12.3.2024",    // Text element named "ID-Date"
  "FM-Text.text": "As we look to the stars..." // Text element named "FM-Text"
}
```

## How to Find Your Template's Element Names

### Method 1: Creatomate Dashboard (Easiest)

1. Go to [Creatomate Dashboard](https://creatomate.com)
2. Open your template
3. Click on each element (image, text, audio)
4. Look at the **"Name"** or **"ID"** field in the properties panel
5. That's your element name!

**Example:**
- Click on an image → Properties show: `Name: Image-1` → Use `Image-1.source`
- Click on text → Properties show: `Name: Caption-1` → Use `Caption-1.text`
- Click on audio → Properties show: `Name: Voiceover-1` → Use `Voiceover-1.source`

### Method 2: Template JSON Export

1. In Creatomate dashboard, export your template as JSON
2. Look for elements with `"name"` property
3. Those are your element names

### Method 3: Test Render

1. Make a test render with sample data
2. Check the API request payload
3. See what element names were used

## Common Element Naming Patterns

### Pattern 1: Sequential Numbers
```
Image-1, Image-2, Image-3
Voiceover-1, Voiceover-2, Voiceover-3
Text-1, Text-2, Text-3
```

### Pattern 2: Prefix + Type + Number
```
1PC-Photo-1, 1PC-Photo-2
MPP-Photo-1, MPP-Photo-2
IT-Text, ID-Text, FM-Text
```

### Pattern 3: Descriptive Names
```
Background-Image
Main-Voiceover
Caption-Text
Title-Text
```

## Your Current Code vs Template

### What the Code Generates (Default)
```json
{
  "Image-1.source": "https://...",
  "Image-2.source": "https://...",
  "Voiceover-1.source": "https://...",
  "Voiceover-2.source": "https://...",
  "Text-1.text": "Dialogue...",
  "Text-2.text": "Dialogue..."
}
```

### What Your Template Might Expect
Based on `creatomate.txt`, your template might use:
```json
{
  "1PC-Photo.source": "https://...",
  "MPP-Photo-1.source": "https://...",
  "MPP-Photo-2.source": "https://...",
  "IT-Text.text": "Intro text...",
  "FM-Text.text": "Final text..."
}
```

## How to Match Element Names

### Option 1: Use Element Prefix

If your template uses a prefix pattern, pass it when running:

```bash
python execution/assemble_video.py \
  script.json audio.json image.json \
  your_template_id \
  "1PC-"  # This prefix will be added to all element names
```

**Result:**
- `1PC-Photo-1.source` (instead of `Image-1.source`)
- `1PC-Voiceover-1.source` (instead of `Voiceover-1.source`)
- `1PC-Text-1.text` (instead of `Text-1.text`)

### Option 2: Update Template Element Names

Rename elements in your Creatomate template to match the code:
- Change `1PC-Photo` → `Image-1`
- Change `MPP-Photo-1` → `Image-1`
- Change `IT-Text` → `Text-1`

### Option 3: Custom Element Mapping

Tell me your exact element names and I'll update the code to match them.

## Step-by-Step: Finding Your Element Names

1. **Log into Creatomate**: https://creatomate.com
2. **Open your template**: Click on the template you're using
3. **Select an element**: Click on an image, text, or audio element
4. **Check properties panel**: Look for "Name" or "ID" field
5. **Note the name**: Write it down (e.g., "Image-1", "1PC-Photo", etc.)
6. **Repeat for all elements**: Check all images, audio, and text elements

## Example: Complete Element Mapping

If your template has these elements:
```
Template Elements:
- Image named "Background" → Use "Background.source"
- Image named "1PC-Photo" → Use "1PC-Photo.source"
- Text named "Caption" → Use "Caption.text"
- Audio named "Voiceover-1" → Use "Voiceover-1.source"
```

Your API payload would be:
```json
{
  "template_id": "your-template-id",
  "modifications": {
    "Background.source": "https://image1.jpg",
    "1PC-Photo.source": "https://image2.jpg",
    "Caption.text": "Your caption text",
    "Voiceover-1.source": "https://audio1.mp3"
  }
}
```

## Quick Checklist

- [ ] Logged into Creatomate dashboard
- [ ] Opened your template
- [ ] Clicked on each element (image, audio, text)
- [ ] Noted the "Name" or "ID" for each element
- [ ] Compared with what the code generates
- [ ] Decided on solution (prefix, rename template, or customize code)

## Need Help?

Share your template's element names and I'll update the code to match them exactly!
