# 🎨 GalleryGenerator

GalleryGenerator is a simple, no-code gallery creator for artists, illustrators, and designers.
Just drop this tool into any folder containing your images — and it will instantly generate ready-to-host HTML gallery pages.

## ✨ Features

* 🖼️ Automatically detects supported image formats listed in settings.txt

* ⚙️ Creates two gallery pages:

    * index.html — includes image names

    * index2.html — clean view without image names

* 💾 Generates .htaccess to block direct access to image and text files

* 🌈 Gradient background (white to 50% gray) for better visibility of light images

* 🧭 Floating image viewer — click any thumbnail to view full size

* Zero dependencies once built — single .exe file for ease of use

## 🚀 How to Use

* Copy GalleryGenerator.exe (or gallerygenerator.py if using Python) into your image folder.

* Run it by double-clicking.

* If a settings.txt file isn’t found, the program will create one and display an error asking you to edit it before re-running.

* Once run successfully, it will generate:

    * index.html

     * index2.html

    * .htaccess

* Open index.html in any browser to preview your gallery.

## ⚙️ Building from Source (Optional)

If you prefer to build your own executable:

~~~
pip install pyinstaller
pyinstaller --onefile gallerygenerator.py
~~~

Your single-file executable will appear in the dist folder.

### 🖥️ How to Host

Once your gallery is generated, you can easily publish it online.
Here are a few simple options — no coding required:

1. GitHub Pages (Free)

* Create a free GitHub account at github.com


* Make a new repository (e.g., my-gallery).

* Upload all your image files, index.html, and .htaccess (if needed).

* Go to Settings → Pages, set the branch to main, and click Save.

* Your gallery will be live at:
https://yourusername.github.io/my-gallery/


2. Netlify (Free & Fast)

* Visit netlify.com


* Drag and drop your entire folder onto the Netlify dashboard.

* Your site will be live instantly with a free .netlify.app link.

3. Personal Hosting / cPanel

* If you already have a hosting plan, upload your generated files via File Manager or FTP to your public HTML folder (often named public_html or www).

* Your gallery will appear at your domain automatically.


4. Local Preview

    To preview on your computer, just double-click index.html.
It will open in your browser like a normal webpage.
