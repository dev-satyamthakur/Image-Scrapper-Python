import os
import io
import time
import base64
import requests
from PIL import Image
from urllib.parse import quote
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# Configuration
query = "whale"
MINIMUM_SIZE_KB = 4  # 4 KB threshold
MAX_IMAGES = 10      # Stop after 10 valid images

# Setup paths and encoding
query_url = quote(query)
folder_name = os.path.join('', query)
os.makedirs(folder_name, exist_ok=True)

# Initialize browser
service = Service(r"C:\Users\Satyam Thakur\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get(f"https://www.google.com/search?q={query_url}&tbm=isch")

# Scroll to load images
for _ in range(2):  # Scroll twice to load more initial images
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1.5)

# Find image elements
img_elements = driver.find_elements(By.CSS_SELECTOR, 'img.YQ4gaf')
print(f"Found {len(img_elements)} potential images")

# Image processing
saved_count = 0

for i, img in enumerate(img_elements):
    if saved_count >= MAX_IMAGES:
        break
        
    try:
        img_url = img.get_attribute("src")
        if not img_url:
            continue

        # HTTP image handling
        if img_url.startswith('http'):
            img_response = requests.get(img_url, timeout=10)
            content = img_response.content
            size_kb = len(content) // 1024
            
            if size_kb < MINIMUM_SIZE_KB:
                print(f"Image {i+1}: {size_kb}KB (Skipped)")
                continue
                
        # Base64 image handling
        elif img_url.startswith('data:image'):
            img_data = img_url.split('base64,')[1]
            content = base64.b64decode(img_data)
            size_kb = len(content) // 1024
            
            if size_kb < MINIMUM_SIZE_KB:
                print(f"Image {i+1}: {size_kb}KB (Skipped)")
                continue
                
        else:
            continue

        # Save the image
        img_name = f"image_{saved_count + 1}.jpg"
        img_path = os.path.join(folder_name, img_name)
        
        if img_url.startswith('http'):
            with open(img_path, "wb") as f:
                f.write(content)
        else:
            Image.open(io.BytesIO(content)).save(img_path)
            
        print(f"Saved {img_name} ({size_kb}KB)")
        saved_count += 1

    except Exception as e:
        print(f"Error processing image {i+1}: {str(e)}")

print(f"\nSuccessfully saved {saved_count} images over {MINIMUM_SIZE_KB}KB")
driver.quit()