from selenium import webdriver
from time import sleep
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

  def visit_url(self, url, wait=2):
    self.driver.get(url)
    sleep(wait)
    print(self.driver.title)

  def take_screenshot(self, file_name="screenshot.png"):
    self.driver.get_screenshot_as_file(file_name)

  def get_images(self):
    # driver.find_elements_by_class_name()
    images = self.driver.find_elements_by_class_name("x-stream-photo-group-blocks-container-view")
    
    for i in range(len(images)):
      images[i].click()
      sleep(2)
      self.take_screenshot(f"screenshot_{i}.png")
      self.driver.back()
      sleep(2)
      images = self.driver.find_elements_by_class_name("x-stream-photo-group-blocks-container-view")

    # images = self.driver.find_elements_by_tag_name("p")
    print(len(images))



new_bot = SiteBot()
new_bot.visit_url("https://www.icloud.com/sharedalbum/#B0o5oqs3q7vYSt")
# new_bot.take_screenshot()
new_bot.get_images()
