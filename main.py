import os
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI(
    title="Aguililla Auto Detail API",
    description="Backend routing for the bilingual Aguililla Auto Detail web platform.",
    version="1.0.0"
)

# 1. SERVE DYNAMIC STATIC IMAGES AND ASSETS
# This mounts your local 'images', 'style.css', and 'script.js' files 
# so the browser can easily download and read them.
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Ensure your CSS/JS files can be found in the root or a static folder
# For simplicity, we mount the current directory for root assets, or specific folders
if os.path.isdir(os.path.join(BASE_DIR, "images")):
    app.mount("/images", StaticFiles(directory=os.path.join(BASE_DIR, "images")), name="images")

# 2. LANDING PAGE ROUTE
@app.get("/", response_class=FileResponse)
def read_index():
    """
    Serves the main bilingual HTML landing page for Aguililla Auto Detail.
    """
    index_path = os.path.join(BASE_DIR, "index.html")
    if os.path.exists(index_path):
        return FileResponse(index_path)
    return {"error": "index.html file not found in root directory."}

# 3. HELPFUL ROUTE FOR THE CSS AND JS ASSETS IF NOT FOLDER-STRUCTURED
@app.get("/style.css", response_class=FileResponse)
def get_style():
    return FileResponse(os.path.join(BASE_DIR, "style.css"))

@app.get("/script.js", response_class=FileResponse)
def get_script():
    return FileResponse(os.path.join(BASE_DIR, "script.js"))

# 4. FUTURE EXPANSION ENDPOINT (SCALING PREPARATION)
# You can connect this to a cloud database (like MongoDB Atlas) later to dynamically load photos!
@app.get("/api/gallery")
def get_gallery_images():
    """
    Endpoint prepared for future portfolio expansion.
    Returns a list of dynamic image metadata URLs.
    """
    return {
        "status": "success",
        "count": 4,
        "images": [
            {"id": 1, "url": "https://images.unsplash.com/photo-1607860108855-64acf2078ed9?w=600", "title": "Paint Correction"},
            {"id": 2, "url": "https://images.unsplash.com/photo-1563720223185-11003d516935?w=600", "title": "Interior Detail"},
            {"id": 3, "url": "https://images.unsplash.com/photo-1619642751034-765dfdf7c58e?w=600", "title": "Engine Wash"},
            {"id": 4, "url": "https://images.unsplash.com/photo-1520340356584-f9917d1eea6f?w=600", "title": "Gloss Finish"}
        ]
    }