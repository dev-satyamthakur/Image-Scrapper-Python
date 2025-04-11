import os
import io
import time
import base64
import requests
from PIL import Image
from urllib.parse import quote
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service  # Import Service

# Enter query for Google search
query = "dog"
# Convert the query into URL format
query_url = quote(query)
# Specify the desired folder path on the desktop
folder_name = os.path.join('', query)

# Create folder if it doesn't exist (no error if exists)
os.makedirs(folder_name, exist_ok=True)  # Fix for WinError 183

# Initialize Chrome with Service
service = Service(executable_path=r"C:\Users\Satyam Thakur\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service)  # Pass service as argument

# URL for Google Images search
url = f"https://www.google.com/search?q={query_url}&tbm=isch"
driver.get(url)

# Simulate scrolling to load more images
for _ in range(1):  # Adjust scroll count
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)  # Wait for images to load

try:
    # Find all image elements using updated method
    img_elements = driver.find_elements(By.CSS_SELECTOR, 'img.YQ4gaf')  # Fix deprecated method
    print(img_elements)
except Exception as e:
    print(f"An error occurred: {str(e)}")

# Download and save images
for i, img in enumerate(img_elements):
    img_url = img.get_attribute("src")
    if img_url and img_url.startswith('http'):
        img_response = requests.get(img_url)
        img_name = f"{i + 1}.jpg"
        img_path = os.path.join(folder_name, img_name)
        with open(img_path, "wb") as img_file:
            img_file.write(img_response.content)
    elif img_url and img_url.startswith('data:image/jpeg;base64'):
        img_data = img_url.split('base64,')[1]
        img = Image.open(io.BytesIO(base64.b64decode(img_data)))
        img_name = f"{i + 1}.jpg"
        img_path = os.path.join(folder_name, img_name)
        img.save(img_path)

print(f"Images saved to: {folder_name}")
driver.quit()