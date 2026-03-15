# Visual Generation Directive

## Goal
Generate images for each scene using DALL-E based on visual prompts from script.

## Inputs
- `script` (dict): Script with visual prompts
- `style` (str, optional): Image style preference

## Execution
1. **Check Character Folder**: First check `character/` folder for character images
   - Looks for files matching scene numbers: `character_1.png`, `scene_1.png`, etc.
   - Supports: `.png`, `.jpg`, `.jpeg`, `.gif`, `.webp`
   - If character found, uses it and skips API generation
2. **Fallback to Gemini**: If no character found, generate with Gemini API
   - Uses Google Gemini for image generation (requires Vertex AI Imagen or fallback)
   - If Gemini not available, falls back to OpenAI DALL-E

## Outputs
- `image_files` (list): List of image file paths
  - Each scene generates one image: `scene_1.png`, `scene_2.png`, etc.
- `image_urls` (list): List of image URLs (if stored in cloud)
- `source` (str): Source of image - "character_folder" or "gemini" or "openai"

## Tools
1. **Character Folder** (`character/` folder in workspace)
   - First priority: Check for existing character images
   - File naming: `character_{scene_num}.png` or `scene_{scene_num}.png`
   - Supports multiple image formats
2. **Google Gemini API** (`google-generativeai` package) - Fallback option
   - Model: `gemini-1.5-pro` with image generation capabilities
   - Requires Vertex AI Imagen 3 for actual generation
   - Often more cost-effective
   - Good quality for YouTube thumbnails and visuals
3. **OpenAI DALL-E API** (`openai` package) - Final fallback
   - Model: `dall-e-3` for best quality
   - Used if Gemini image generation not available

## Edge Cases
- Missing visual prompts: Generate default prompt from scene text
- Content policy violations: Retry with safer prompt
- Image generation failures: Use placeholder or retry
- Style inconsistencies: Ensure consistent style across images

## Quality Requirements
- Images match scene descriptions
- Consistent style across all images
- High resolution (1024x1024 or higher)
- Appropriate for YouTube content policies

## Error Handling
- Retry on content policy errors with modified prompt
- Generate placeholder images if generation fails
- Log all generation errors
- Validate image files are readable

## Cost Optimization
- Cache images if visual prompts unchanged
- Use appropriate image sizes (not always highest quality)
- Reuse similar images when possible

## Notes
- Visual quality impacts click-through rate
- Ensure images are engaging and relevant
- Consider Ken Burns effect for static images
- Store images in `.tmp/` during processing
