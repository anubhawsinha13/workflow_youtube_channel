# How to Find Your Creatomate Template Element Names

## Quick Guide

Element names are the **identifiers** for each part of your Creatomate template (images, audio, text). You need to know these names to tell Creatomate which parts to replace with your content.

## Step-by-Step Instructions

### Step 1: Open Your Template

1. Go to https://creatomate.com
2. Log in
3. Click on **"Templates"** in the sidebar
4. Open the template you're using (the one with ID from `CREATOMATE_TEMPLATE_ID` in your `.env`)

### Step 2: Find Element Names

For each element in your template:

1. **Click on the element** (image, text box, audio track)
2. **Look at the right panel** (Properties panel)
3. **Find the "Name" field** - This is your element name!

**Example:**
- Click image → Properties show `Name: Image-1` → Element name is `Image-1`
- Click text → Properties show `Name: Caption-1` → Element name is `Caption-1`
- Click audio → Properties show `Name: Voiceover-1` → Element name is `Voiceover-1`

### Step 3: Note All Element Names

Write down all element names you find:
- Image elements: `Image-1`, `Image-2`, etc.
- Audio elements: `Voiceover-1`, `Voiceover-2`, etc.
- Text elements: `Text-1`, `Caption-1`, etc.

### Step 4: Compare with Code

The code currently generates:
- `Image-{num}.source` for images
- `Voiceover-{num}.source` for audio
- `Text-{num}.text` for dialogue

**Do your template element names match?**

- ✅ **Yes** → You're good! The code will work.
- ❌ **No** → You need to either:
  1. Rename elements in template to match code
  2. Use element prefix when running script
  3. Customize code to match your template

## Visual Example

```
Your Creatomate Template:
┌─────────────────────────┐
│  [Image Element]         │ ← Click this → Name: "Image-1"
│  "Your text here"        │ ← Click this → Name: "Text-1"
│  [Audio Track]           │ ← Click this → Name: "Voiceover-1"
└─────────────────────────┘

API Payload:
{
  "Image-1.source": "https://...",      ← Matches "Image-1"
  "Text-1.text": "Your text here",      ← Matches "Text-1"
  "Voiceover-1.source": "https://..."   ← Matches "Voiceover-1"
}
```

## Common Element Name Patterns

### Pattern 1: Simple Sequential
```
Image-1, Image-2, Image-3
Voiceover-1, Voiceover-2
Text-1, Text-2
```
✅ **Matches code default** - No changes needed!

### Pattern 2: Prefix Pattern
```
1PC-Photo-1, 1PC-Photo-2
MPP-Photo-1, MPP-Photo-2
IT-Text, ID-Text
```
⚠️ **Needs prefix** - Use `element_prefix` parameter

### Pattern 3: Custom Names
```
Background-Image
Main-Voiceover
Caption-Text
```
⚠️ **Needs customization** - Update code or template

## What to Do Next

1. **Find your element names** (follow steps above)
2. **Share them with me** - I'll update the code to match
3. **OR** rename template elements to match code defaults
4. **OR** use element prefix when running the script

## Example: Your Template (from creatomate.txt)

Based on your `creatomate.txt` file, your template uses:
- `1PC-Photo.source` - Single photo
- `MPP-Photo-{num}.source` - Multi-photo (numbered)
- `IT-Text.text` - Intro text
- `ID-Date.text` - Date text
- `FM-Text.text` - Final text

**This doesn't match the code defaults!**

**Solution**: Use element prefix `"1PC-"` or `"MPP-"` when running, OR update template to use `Image-{num}` and `Voiceover-{num}`.
