̥̥̥# 🖼️ Image Scraper

A modern Python-based image scraper that downloads high-quality images from Google Images using Selenium WebDriver.

## ✨ Features

- 🔍 Searches Google Images with custom queries
- 📊 Filters images by minimum size requirements
- 🚀 Handles both HTTP and Base64 encoded images
- 🎯 Configurable maximum image count
- 💾 Organized image storage in query-specific folders

## 🛠️ Prerequisites

- Python 3.6+
- Chrome WebDriver
- Required Python packages:
  ```
  selenium
  Pillow
  requests
  ```

## 🚀 Getting Started

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Update the Chrome WebDriver path in `scrape-static-images.py`:
   ```python
   service = Service(r"path/to/your/chromedriver.exe")
   ```

3. Run the script:
   ```bash
   python scrape-static-images.py
   ```

## ⚙️ Configuration

You can customize the following parameters in the script:

```python
query = "whale"              # Search term
MINIMUM_SIZE_KB = 4         # Minimum image size in KB
MAX_IMAGES = 10             # Maximum number of images to download
```

## 📝 How It Works

1. Initializes Chrome WebDriver
2. Performs Google Image search
3. Scrolls to load more images
4. Filters images based on size
5. Downloads and saves valid images
6. Handles both HTTP and Base64 encoded images

## 📋 Output

Images are saved in a folder named after the search query:
```
whale/
  ├── image_1.jpg
  ├── image_2.jpg
  └── ...
```

## ⚠️ Disclaimer

Please ensure you comply with Google's terms of service and copyright laws when using this script.

## 📄 License

This project is open source and available under the MIT License.