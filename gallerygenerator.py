import os
import sys

def pause_exit(message):
    """Show message and wait for any key press before exiting."""
    print("\n" + message)
    input("Press any key to exit...")
    sys.exit()

def create_default_settings():
    """Create a default settings.txt file."""
    default_content = "svg\npng\njpg\njpeg\ngif"
    with open("settings.txt", "w") as f:
        f.write(default_content)

def read_formats():
    """Read image formats from settings.txt."""
    if not os.path.exists("settings.txt"):
        create_default_settings()
        pause_exit("⚠️  settings.txt not found.\nA default one has been created.\nPlease review and re-run the program.")
    with open("settings.txt", "r") as f:
        return [line.strip().lower().lstrip(".") for line in f if line.strip()]

def get_image_files(formats):
    """Scan current directory for image files."""
    all_files = [f for f in os.listdir(".") if os.path.isfile(f)]
    image_files = [f for f in all_files if any(f.lower().endswith(ext) for ext in formats)]
    image_files.sort()
    return image_files

def create_htaccess(formats):
    """Create .htaccess file to restrict direct file access."""
    deny_list = [f"*." + ext for ext in formats] + ["*.txt"]
    htaccess_content = "Options -Indexes\n<FilesMatch \"(" + "|".join([d.replace("*.", "") for d in deny_list]) + ")\">\n"
    htaccess_content += "  Require all denied\n</FilesMatch>\n"
    with open(".htaccess", "w") as f:
        f.write(htaccess_content)

def generate_html_files(image_files):
    """Generate index.html and index2.html."""

    html_head = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<style>
  body {{
    font-family: Arial, sans-serif;
    background: #f5f5f5;
    margin: 20px;
  }}
  .gallery {{
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(160px, 1fr));
    gap: 15px;
  }}
  .item {{
    background: white;
    border-radius: 10px;
    padding: 10px;
    box-shadow: 0 2px 6px rgba(0,0,0,0.1);
    cursor: pointer;
    transition: transform 0.2s ease;
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    height: 160px;
  }}
  .item:hover {{
    transform: scale(1.03);
  }}
  .item img {{
    max-width: 100%;
    max-height: 120px;
    object-fit: contain;
    display: block;
    background: linear-gradient(135deg, #ffffff, #cccccc);
    border-radius: 6px;
    padding: 5px;
  }}
  .filename {{
    font-size: 12px;
    color: #333;
    margin-top: 6px;
    word-wrap: break-word;
  }}
  .lightbox {{
    display: none;
    position: fixed;
    z-index: 100;
    left: 0;
    top: 0;
    width: 100%;
    height: 100%;
    background: rgba(255,255,255,0.95);
    justify-content: center;
    align-items: center;
  }}
  .lightbox img {{
    max-width: 90%;
    max-height: 90%;
    box-shadow: 0 4px 20px rgba(0,0,0,0.3);
    background: linear-gradient(135deg, #ffffff, #cccccc);
    border-radius: 8px;
  }}
</style>
</head>
<body>
<div class="gallery">
"""

    html_foot = """</div>
<div class="lightbox" id="lightbox"><img src="" alt=""></div>
<script>
  const lightbox = document.getElementById('lightbox');
  const lightboxImg = lightbox.querySelector('img');
  document.querySelectorAll('.item img').forEach(img => {{
    img.addEventListener('click', () => {{
      lightboxImg.src = img.src;
      lightbox.style.display = 'flex';
    }});
  }});
  lightbox.addEventListener('click', () => {{
    lightbox.style.display = 'none';
  }});
</script>
</body>
</html>
"""

    # index.html (with names)
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html_head.format(title="Image Gallery with Names"))
        for file in image_files:
            f.write(f'  <div class="item"><img src="{file}" alt=""><div class="filename">{file}</div></div>\n')
        f.write(html_foot)

    # index2.html (without names)
    with open("index2.html", "w", encoding="utf-8") as f:
        f.write(html_head.format(title="Image Gallery"))
        for file in image_files:
            f.write(f'  <div class="item"><img src="{file}" alt=""></div>\n')
        f.write(html_foot)

def main():
    formats = read_formats()
    image_files = get_image_files(formats)

    if not image_files:
        pause_exit("⚠️  No image files found matching settings.txt formats.")

    generate_html_files(image_files)
    create_htaccess(formats)

    print(f"✅ Generated index.html and index2.html with {len(image_files)} images.")
    print("✅ Created .htaccess file to restrict direct file access.")
    pause_exit("All done successfully!")

if __name__ == "__main__":
    main()
