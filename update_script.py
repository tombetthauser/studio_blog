from selenium import webdriver
from time import sleep
import urllib.request
import os


class SiteBot:
  def __init__(self):
    user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:86.0) Gecko/20100101 Firefox/86.0"

    self.options = webdriver.ChromeOptions()
    self.options.headless = True
    self.options.add_argument(f'user-agent={user_agent}')
    self.options.add_argument("--window-size=1920,1080")
    self.options.add_argument('--ignore-certificate-errors')
    self.options.add_argument('--allow-running-insecure-content')
    self.options.add_argument("--disable-extensions")
    self.options.add_argument("--proxy-server='direct://'")
    self.options.add_argument("--proxy-bypass-list=*")
    self.options.add_argument("--start-maximized")
    self.options.add_argument('--disable-gpu')
    self.options.add_argument('--disable-dev-shm-usage')
    self.options.add_argument('--no-sandbox')
    self.driver = webdriver.Chrome(executable_path="./chromedriver.exe", options=self.options)

    self.images_dict = {}


  def visit_url(self, url, wait=2):
    self.driver.get(url)
    sleep(wait)
    print(self.driver.title)


  def take_screenshot(self, file_name="screenshot.png"):
    print(f"Printing screenshot for {file_name}...")
    self.driver.get_screenshot_as_file(file_name)


  def get_images(self):
    # driver.find_elements_by_class_name()
    images = self.driver.find_elements_by_class_name("x-stream-photo-group-blocks-container-view")
    print(f"Cycling through {len(images)} found images...")
    
    for i in range(len(images)):
      images[i].click()
      sleep(2)
      self.take_screenshot(f"screenshot_{i}.png")

      current_image = self.driver.find_element_by_tag_name("img")
      current_image_source = current_image.get_attribute("src")

      current_image_text_element = self.driver.find_element_by_class_name("main")
      current_image_text = current_image_text_element.get_attribute("innerText")
      print(current_image_text)

      self.images_dict[i] = {
        "src": current_image_source,
        "text": current_image_text,
        }

      urllib.request.urlretrieve(current_image_source, f"images/image_{i}.png")

      print(self.images_dict)
      self.driver.back()
      sleep(2)
      images = self.driver.find_elements_by_class_name("x-stream-photo-group-blocks-container-view")

    # images = self.driver.find_elements_by_tag_name("p")



new_bot = SiteBot()
new_bot.visit_url("https://www.icloud.com/sharedalbum/#B0o5oqs3q7vYSt")
# new_bot.take_screenshot()
new_bot.get_images()
