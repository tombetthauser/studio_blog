from selenium import webdriver
from time import sleep
import urllib.request
import sys
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
    self.options.add_argument('--disable-dev-shm-usage')
    self.driver = webdriver.Chrome(executable_path="./chromedriver.exe", options=self.options)

    # self.images_dict = {}
    self.images_dict = {0: {'src': 'https://cvws.icloud-content.com/S/AZZNIkmeOWgJ6ZMJ_zgoTYPOLUK4/IMG_0003.JPG?o=Aoq49Z96_JCacx6KmlF2cgBOStMxVeYZyxptf_emqtPm&v=1&z=https%3A%2F%2Fp50-content.icloud.com%3A443&x=1&a=CAogYD7oK8hlR-dk0xPBykDnjSWPIByg7LC0NT27VQWZ1NwSZRCqyNWnkS8Yqt_orJEvIgEAUgTOLUK4aiVawyAbimRxFD_nqLTh6Mz7YVODa0gzjCxtZnavUhxYX75RO5ptciW4Fxt1xz8yoBIcnkdYjB5aJsWjJpVx_RcDMAKt0CkMPrYodlyM&e=1619565096&r=4ba9da4a-f03d-4b9d-b359-ba972aed4a4c-6&s=X7eUFSBDcbGnNLX7i-m0BpENgb8', 'text': 'Gettin closer...'}, 1: {'src': 'https://cvws.icloud-content.com/S/AZddQ0gIKPDcUbuK46WbwybMgyqZ/IMG_0002.JPG?o=AhAVZ-L1ZuciNQOTRFJC-vOztzaNOPe6czWqNK6iUDCV&v=1&z=https%3A%2F%2Fp50-content.icloud.com%3A443&x=1&a=CAogt-IZY56KbwLksBraB-xV2Xvz4AI_F5Jjskj22OPBnNwSZRDM69WnkS8YzILprJEvIgEAUgTMgyqZaiVG01XdBcNem5hch__u2jNj1iyphOdDO3Icietg2cZc7Xs7KwRnciUkWjd9CcvYZBrDxAvZofeTcB7QU_vIXYw89Q1r2CCv1yucVSo3&e=1619565101&r=1a44c790-a0ce-4d9e-99bf-8c3deb37e260-3&s=Z1ODK8UPQL9RIjPvlAcU8WtxWic',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      'text': 'Some mixed material casts...'}, 2: {'src': 'https://cvws.icloud-content.com/S/AS6Y8AqWDe9c8VFV5JLBhvDuqHmR/IMG_0001.JPG?o=AqAqFTKkqi5qhWlaAwWRkAV4Df5bvnhkf34flQmolTAF&v=1&z=https%3A%2F%2Fp50-content.icloud.com%3A443&x=1&a=CAog0bmF-wR6qEClP19qRWqBw0Ds0zv45wn1292TnJILJ9gSZRDVkdankS8Y1ajprJEvIgEAUgTuqHmRaiULhfG1V-vd6eWMdiWRCaT5ogvuBGAnAIH-HCutgdRKRTZcIskmciXN0yB1PrDSDfGoy7c2ClcA5cqii_j6FUbB4WLrbuaTMA9pShm5&e=1619565106&r=c9fbbd78-1572-4d9c-9562-e38aba318933-6&s=idlVyPHP5iI_0pZUUgrHIhhJZrM', 'text': 'A moment of tranquility...'}}


  def visit_url(self, url, wait=2):
    self.driver.get(url)
    sleep(wait)
    print(self.driver.title)


  def take_screenshot(self, file_name="screenshot.png"):
    print(f"Printing screenshot for {file_name}...")
    self.driver.get_screenshot_as_file(file_name)


  def get_images(self):
    images = self.driver.find_elements_by_class_name("x-stream-photo-group-blocks-container-view")
    print(f"Cycling through {len(images)} found images...")
    
    for i in range(len(images)):
      images[i].click()
      sleep(2)

      current_image = self.driver.find_element_by_tag_name("img")
      current_image_source = current_image.get_attribute("src")

      current_image_text_element = self.driver.find_element_by_class_name("main")
      current_image_text = current_image_text_element.get_attribute("innerText")
      print(current_image_text)

      self.images_dict[i] = {
        "src": current_image_source,
        "text": current_image_text,
        }

      urllib.request.urlretrieve(current_image_source, f"images/{current_image_text}.png")

      print(self.images_dict)
      self.driver.back()
      sleep(2)
      images = self.driver.find_elements_by_class_name("x-stream-photo-group-blocks-container-view")


  def create_html_file(self):
    # f = open("index.html", "x")
    # f = open("index.html", "a+")
    f = open("index.html", "w")
    f2 = open("files/header.html", "r")
    f.write(f2.read())
    f2.close()

    # f = open("index.html", "w")

    for thing in self.images_dict:
      print(thing)
      current_text = self.images_dict[thing]["text"]
      current_src = self.images_dict[thing]["src"]
      f.write(self.create_html_element(current_src, current_text))
    
    f3 = open("files/footer.html", "r")
    f.write(f3.read())
    f3.close()
    
    f.close()

  def create_html_element(self, src, text):
    return f'''
      <div>
        <a target="new" href="{src}">
          <img src={src}>
        </a>
        <p>{text}</p>
      <div>
    '''

new_bot = SiteBot()
# new_bot.visit_url("https://www.icloud.com/sharedalbum/#B0o5oqs3q7vYSt")
# new_bot.get_images()
new_bot.create_html_file()
