import os
import io
import time
import base64
import json  # Added for JSON formatting
import requests
from PIL import Image
from urllib.parse import quote
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Configuration
QUERY = "dog"
MINIMUM_SIZE_KB = 4
MAX_IMAGES = 10
CHROMEDRIVER_PATH = r"C:\Users\Satyam Thakur\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe"

def main():
    # Setup directories
    folder_name = os.path.join(os.getcwd(), QUERY)
    os.makedirs(folder_name, exist_ok=True)
    saved_urls = []  # List to store URLs of saved images

    # Configure headless browser
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36")

    # Initialize browser
    service = Service(executable_path=CHROMEDRIVER_PATH)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        # Open Google Images
        driver.get(f"https://www.google.com/search?q={quote(QUERY)}&tbm=isch")
        print("Loaded Google Images page")

        # Scroll to load initial images
        for _ in range(2):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1.5)

        # Find image elements
        img_elements = driver.find_elements(By.CSS_SELECTOR, 'img.YQ4gaf')
        print(f"Found {len(img_elements)} potential images")

        # Process images
        saved_count = 0
        for i, img in enumerate(img_elements):
            if saved_count >= MAX_IMAGES:
                break

            try:
                img_url = img.get_attribute("src")
                if not img_url:
                    continue

                # Handle different image types
                if img_url.startswith('http'):
                    response = requests.get(img_url, timeout=10)
                    content = response.content
                    size_kb = len(content) // 1024
                elif img_url.startswith('data:image'):
                    img_data = img_url.split('base64,')[1]
                    content = base64.b64decode(img_data)
                    size_kb = len(content) // 1024
                else:
                    continue

                if size_kb < MINIMUM_SIZE_KB:
                    print(f"Image {i+1}: {size_kb}KB (too small)")
                    continue

                # Save image
                img_name = f"image_{saved_count + 1}.jpg"
                img_path = os.path.join(folder_name, img_name)
                
                if img_url.startswith('http'):
                    with open(img_path, "wb") as f:
                        f.write(content)
                else:
                    Image.open(io.BytesIO(content)).save(img_path)

                print(f"Saved {img_name} ({size_kb}KB)")
                saved_urls.append(img_url)  # Store the URL
                saved_count += 1

            except Exception as e:
                print(f"Error processing image {i+1}: {str(e)}")

        # Print results
        print(f"\nSuccessfully saved {saved_count} images (>{MINIMUM_SIZE_KB}KB) to: {folder_name}")
        
        # Print JS array of URLs
        if saved_urls:
            print("\n// JavaScript array of saved image URLs:")
            print(f"const imageUrls = {json.dumps(saved_urls, indent=2)};")
        else:
            print("\nNo image URLs were saved.")

    finally:
        driver.quit()
        print("Browser closed")

if __name__ == "__main__":
    main()