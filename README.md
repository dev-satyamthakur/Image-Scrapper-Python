# 🖼️ Bio - Guardian : Image Scraper

A modern Python-based image scraper that downloads high-quality images from Google Images using Selenium WebDriver, with support for both headless and standard browser operations.

## ✨ Features

- 🔍 Searches Google Images with custom queries
- 📊 Filters images by minimum size requirements
- 🚀 Handles both HTTP and Base64 encoded images
- 🎯 Configurable maximum image count
- 💾 Organized image storage in query-specific folders
- 🤖 Supports both headless and standard browser modes
- 📋 Optional JSON/JS array output of image URLs

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

2. Update the Chrome WebDriver path in either script:
   ```python
   CHROMEDRIVER_PATH = r"path/to/your/chromedriver.exe"
   ```

3. Choose a script to run:
   ```bash
   # For standard browser mode:
   python scrape-static-images.py
   
   # For headless mode:
   python scrape-image-headless.py
   ```

## ⚙️ Configuration

You can customize the following parameters in either script:

```python
# Standard mode (scrape-static-images.py)
query = "whale"              # Search term
MINIMUM_SIZE_KB = 4         # Minimum image size in KB
MAX_IMAGES = 10             # Maximum number of images to download

# Headless mode (scrape-image-headless.py)
QUERY = "dog"               # Search term
MINIMUM_SIZE_KB = 4         # Minimum image size in KB
MAX_IMAGES = 10             # Maximum number of images to download
```

## 📝 How It Works

1. Initializes Chrome WebDriver (headless or standard)
2. Performs Google Image search
3. Scrolls to load more images
4. Filters images based on size
5. Downloads and saves valid images
6. Handles both HTTP and Base64 encoded images
7. Optionally outputs URLs in JavaScript array format (headless mode)

## 📋 Output

Images are saved in a folder named after the search query:
```
query_term/
  ├── image_1.jpg
  ├── image_2.jpg
  └── ...
```

The headless version also outputs a JavaScript array of image URLs:
```javascript
const imageUrls = [
  "https://example.com/image1.jpg",
  "https://example.com/image2.jpg",
  // ...
];
```

## 🔄 Script Comparison

- **scrape-static-images.py**: Standard mode with visible browser
- **scrape-image-headless.py**: Headless mode with additional URL logging

## ⚠️ Disclaimer

Please ensure you comply with Google's terms of service and copyright laws when using this script.

## 📄 License

This project is open source and available under the MIT License.
