from selenium import webdriver
from datetime import date
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
    self.driver = None
    # self.driver = webdriver.Chrome(executable_path="./chromedriver.exe", options=self.options)

    self.images_dict = {}
    self.demo_images_dict = {0: {'src': 'https://cvws.icloud-content.com/S/AbjDnPT4gkojdj-EESS_38NzCtph/IMG_0008.JPG?o=AtTsKIACA676F92HIvwuaIrdCQP1VHBHAVzBs_jREhJN&v=1&z=https%3A%2F%2Fp50-content.icloud.com%3A443&x=1&a=CAog7Jw2FcGJ96hbUrDIRUm5t_AKApC3HaH5uXxEFFTg0LESZRDWwpHPkS8Y1tmk1JEvIgEAUgRzCtphaiX_h8AOBGRvWNOcCBXzmk84awu8JNT0p_KQtYd81fSojO9_VBT6ciVLsCZvbe5Pe1f2w9bshKLWlPCIwAc4_gz0KdDL3bbwOdHTdu8x&e=1619647868&r=7f0f76d8-ac99-4646-8d5b-f07c7d816c7f-12&s=7u28rh6ZHDsrjOuOg5OK1cjIjmk', 'text': 'recess time...'}, 1: {'src': 'https://cvws.icloud-content.com/S/Ab2Rgwdj3BOyQCD6_z3tgJnXCW9f/IMG_0007.JPG?o=AglTg-q9ipEv7OgfwBPozzhdRvkhWqGTNsM1iwU7I1Gf&v=1&z=https%3A%2F%2Fp50-content.icloud.com%3A443&x=1&a=CAogSSZE1phk572edS-DdhZmLzJ6rQdccYwmdVUWtTbzpgcSZRDTm5LPkS8Y07Kl1JEvIgEAUgTXCW9faiUk6NLCWSIa0V67UMUZhtGukm1uNvqz6ZnuonrHokrQ39Id5MF1ciWj5jybFBDDXNUOIb6pbiYX131OcLFSsLmwA1kz-vyFZIOCSUHB&e=1619647879&r=3d22c009-eb9c-4e88-b767-abc17ca0a53d-13&s=h-HygGu61nQsyHoHnyl6pIqY2KU', 'text': 'countin grooves...'}, 2: {'src': 'https://cvws.icloud-content.com/S/AZ2UbOfx7JNXsokq4V1KmmypyA1y/IMG_0005.JPG?o=AofSUiq1O4WHb4p8lU2_h6IjxPbTjVORR82X1-HybANJ&v=1&z=https%3A%2F%2Fp50-content.icloud.com%3A443&x=1&a=CAogfvhwH8x72HLi4LOLWvVrz8jGRqm0VB7dfZn1jsmkh6YSZRDM6pLPkS8YzIGm1JEvIgEAUgSpyA1yaiU1TKOypx91QppNZtahBMm0uhR2o_8vXqW_uXV2MtIJ4qT1WjmFciUmQ3bHrccU_F6XLt9fLCiS2JWoAI-UcQkhKiDWUXFBcSPowASp&e=1619647889&r=4316c4d9-498a-46b7-9c88-10b0e2ef6620-9&s=e8FGPFz-oid2J_81KhdzQtrj1LE', 'text': 'finally ready for detailing...'}, 3: {'src': 'https://cvws.icloud-content.com/S/ARYHXiQ_u95UtId_A9uIFwlLQCCv/IMG_0004.JPG?o=Ah8TI7zTeRSWnoq0PcC7l6jesjjCjGWEF9U3mCbp8Hyu&v=1&z=https%3A%2F%2Fp50-content.icloud.com%3A443&x=1&a=CAog7H-pAYreSEu8xDI15K0lO-ZKZ2VsBXpIGWPSVoRji0cSZRCUvZPPkS8YlNSm1JEvIgEAUgRLQCCvaiWTxkCruI-ZFCqN8Rke2WhUXjiYN4-Fo1CpOxQwiu5IxTYBZEeyciU_f3LrCRSHPLBfPrrPW-OVItLN8wnlzVjUItMyJRMMK31oHHPZ&e=1619647900&r=3109fc21-6456-413f-8d1e-01d00c2601e3-13&s=QR_hM4FbGsNs9BAkPG9-4MhakWQ', 'text': 'Prototype cast with a paper mock-up...'}, 4: {'src': 'https://cvws.icloud-content.com/S/AZZNIkmeOWgJ6ZMJ_zgoTYPOLUK4/IMG_0003.JPG?o=AirKanlzFJH70IFbjxOnOu-0fjHddguLvJN0VcUImrnm&v=1&z=https%3A%2F%2Fp50-content.icloud.com%3A443&x=1&a=CAogDJ3ye3leyPYG3vbsV1zaZUyczTJ33oKwnjxENewXoUYSZRCzmpTPkS8Ys7Gn1JEvIgEAUgTOLUK4aiWeDrDOj2BaoK5kSbH6tv1oa6PAX3jttr2hepJZQGAlnPVe43YCciWAMiVQ3XRBOqutSiDMsgU4Fq0bJAA7Y6UOFyI2sl2NpbOurDVd&e=1619647912&r=0c639a8d-5617-40ae-aba0-43c76ec0043d-14&s=8XM_grOyvNSRfd0VbVbgJ3wI27c', 'text': 'Gettin closer...'}, 5: {'src': 'https://cvws.icloud-content.com/S/AZddQ0gIKPDcUbuK46WbwybMgyqZ/IMG_0002.JPG?o=Ag1Gd6qjnAl3x-RHXI-SsfhIv6vLYRo1454XkAPs18x4&v=1&z=https%3A%2F%2Fp50-content.icloud.com%3A443&x=1&a=CAogckVm8HGPmw-ahZrC8QxFYL_KQDeMpBBUv4W8hX7PtbYSZRDW6JTPkS8Y1v-n1JEvIgEAUgTMgyqZaiVg6nBdZmZChIKumKjGVhkTV1ae47S11ZO4MKf0dubuyeta7M5dciX182-Wh6dO_7EkSjjjpkqi8pIaAC2UlRqmy2gYhXOdzbogLEZ9&e=1619647922&r=80eaf2a9-a3bb-4a4b-89a7-3ba546b769ba-12&s=8-EpS7Iwy9KSt8ZQfYGRHMiJgwc', 'text': 'Some mixed material casts...'}, 6: {'src': 'https://cvws.icloud-content.com/S/AS6Y8AqWDe9c8VFV5JLBhvDuqHmR/IMG_0001.JPG?o=An-KnnPKeS_nyVGz0wy6_BptHlUxCoc_DPbn-xtUukjy&v=1&z=https%3A%2F%2Fp50-content.icloud.com%3A443&x=1&a=CAogeD3ennkxqu7dkZ5QLCjWLGlAKssXiNryy6IPH1EjlDESZRDuv5XPkS8Y7tao1JEvIgEAUgTuqHmRaiVtK8dGFDp_a6tXZvqXjLfKhbshYseT6MoXjMDcIte_6ryqSg5JciXqGZbCE27ecSMEXoTxIp_FEb4lrn4QWc3oCGigxs420_kvAkLq&e=1619647933&r=219a70bd-b28c-4baf-9547-807f16b95487-13&s=bNJhgh9tSmrnXaFvdVR_ZjCCy0o', 'text': 'A moment of tranquility...'}}


  def visit_url(self, url, wait=2):
    self.driver = webdriver.Chrome(executable_path="./chromedriver.exe", options=self.options)
    print(f"Running visit_url() for {url}...")
    self.driver.get(url)
    sleep(wait)
    print(self.driver.title)


  def take_screenshot(self, file_name="screenshot.png"):
    print(f"Printing screenshot for {file_name}...")
    self.driver.get_screenshot_as_file(file_name)

  def get_images(self, wait=2):
    images = self.driver.find_elements_by_class_name(
        "x-stream-photo-group-blocks-container-view")
    print(f"Running get_image() for {len(images)} found images...")
    
    for i in range(len(images)):
      images[i].click()
      sleep(wait)

      current_image = self.driver.find_element_by_tag_name("img")
      current_image_source = current_image.get_attribute("src")

      current_image_text_element = self.driver.find_element_by_class_name("main")
      current_image_text = current_image_text_element.get_attribute("innerText")
      print(f"Processing image associated with '{current_image_text}'...")

      self.images_dict[i] = {
        "src": current_image_source,
        "text": current_image_text,
        }

      urllib.request.urlretrieve(current_image_source, f"images/{current_image_text}.png")

      print(self.images_dict)
      self.driver.back()
      sleep(wait)
      images = self.driver.find_elements_by_class_name("x-stream-photo-group-blocks-container-view")


  def output_files(self):
    if self.images_dict == {}:
      self.images_dict = self.demo_images_dict
    print(f"Running output_files()...")
    f = open("index.html", "w")
    readme_file = open("README.md", "w")
    f2 = open("files/header.html", "r")
    readme_header = open("files/header.md", "r")
    header_text = f2.read()
    f.write(header_text)
    readme_file.write(readme_header.read())
    f2.close()

    for thing in self.images_dict:
      current_text = self.images_dict[thing]["text"]
      current_src = self.images_dict[thing]["src"]
      new_html = self.create_html_element(current_src, current_text)
      new_markdown = self.create_markdown_element(current_src, current_text)
      f.write(new_html)
      readme_file.write(new_markdown)
    
    f3 = open("files/footer.html", "r")
    footer_text = f3.read()
    f.write(footer_text)
    f3.close()
    
    f.close()

  def create_html_element(self, src, text):
    image_path = f'''https://raw.githubusercontent.com/tombetthauser/studio_blog/master/images/{text}.png'''
    return f'''
      <div>
        <a target="new" href="{image_path}">
          <img src={image_path}>
        </a>
        <p class="text-p">{text}</p>
      <div>
    '''

  def create_markdown_element(self, src, text):
    image_path = f'''https://raw.githubusercontent.com/tombetthauser/studio_blog/master/images/{text}.png'''
    return f'''\n<img style="max-width: 500px; margin-bottom: 20px" src="{image_path}">\n<p style="margin-bottom: 50px">{text}</p><br>'''
    # return f'''\n<img style="max-width: 500px; margin-bottom: 20px" src="{src}">\n<br><p style="margin-bottom: 50px">{text}</p><br><br><br>'''

  def commit_to_github(self):
    print(f"Running commit_to_github()...")
    os.system("git add -A")
    sleep(5)
    today = date.today()
    current_date = today.strftime("%d/%m/%Y")
    os.system(f"git commit -m 'Sync and update iCloud content for {current_date}'")
    os.system("git push")

new_bot = SiteBot()
# new_bot.visit_url("https://www.icloud.com/sharedalbum/#B0o5oqs3q7vYSt", 5)
# new_bot.get_images(5)
new_bot.output_files()
new_bot.commit_to_github()


























# Heres a bunch of lorem ipsum because GitHub keeps saying this is an HTML project...
# Lorem ipsum dolor sit amet, consectetuer adipiscing elit; Aenean commodo ligula
# eget dolor. Aenean massa? Cum sociis natoque penatibus et magnis dis parturient
# montes, nascetur ridiculus mus; Donec quam felis, ultricies nec, pellentesque
# eu, pretium quis, sem? Nulla consequat massa quis enim? Donec pede justo,
# fringilla vel, aliquet nec, vulputate eget, arcu; In enim justo, rhoncus ut,
# imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium?
# Integer tincidunt; Cras dapibus! Vivamus elementum semper nisi; Aenean vulputate
# eleifend tellus! Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac,
# enim; Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus; Phasellus
# viverra nulla ut metus varius laoreet! Quisque rutrum? Aenean imperdiet! Etiam
# ultricies nisi vel augue; Curabitur ullamcorper ultricies nisi? Nam eget dui;
# Lorem ipsum dolor sit amet, consectetuer adipiscing elit? Aenean commodo ligula
# eget dolor! Aenean massa? Cum sociis natoque penatibus et magnis dis parturient
# montes, nascetur ridiculus mus; Donec quam felis, ultricies nec, pellentesque
# eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo,
# fringilla vel, aliquet nec, vulputate eget, arcu; In enim justo, rhoncus ut,
# imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium.
# Integer tincidunt; Cras dapibus; Vivamus elementum semper nisi? Aenean vulputate
# eleifend tellus; Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac,
# enim. Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus? Phasellus
# viverra nulla ut metus varius laoreet; Quisque rutrum! Aenean imperdiet? Etiam
# ultricies nisi vel augue; Curabitur ullamcorper ultricies nisi; Nam eget dui.
# Lorem ipsum dolor sit amet, consectetuer adipiscing elit; Aenean commodo ligula
# eget dolor? Aenean massa. Cum sociis natoque penatibus et magnis dis parturient
# montes, nascetur ridiculus mus? Donec quam felis, ultricies nec, pellentesque
# eu, pretium quis, sem; Nulla consequat massa quis enim. Donec pede justo,
# fringilla vel, aliquet nec, vulputate eget, arcu! In enim justo, rhoncus ut,
# imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium?
# Integer tincidunt! Cras dapibus; Vivamus elementum semper nisi! Aenean vulputate
# eleifend tellus? Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac,
# enim; Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus! Phasellus
# viverra nulla ut metus varius laoreet; Quisque rutrum! Aenean imperdiet. Etiam
# ultricies nisi vel augue; Curabitur ullamcorper ultricies nisi; Nam eget dui;
# Lorem ipsum dolor sit amet, consectetuer adipiscing elit; Aenean commodo ligula
# eget dolor? Aenean massa! Cum sociis natoque penatibus et magnis dis parturient
# montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque
# eu, pretium quis, sem; Nulla consequat massa quis enim? Donec pede justo,
# fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut,
# imperdiet a, venenatis vitae, justo; Nullam dictum felis eu pede mollis pretium;
# Integer tincidunt. Cras dapibus! Vivamus elementum semper nisi! Aenean vulputate
# eleifend tellus! Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac,
# enim! Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus. Phasellus
# viverra nulla ut metus varius laoreet? Quisque rutrum? Aenean imperdiet! Etiam
# ultricies nisi vel augue! Curabitur ullamcorper ultricies nisi. Nam eget dui?
# Lorem ipsum dolor sit amet, consectetuer adipiscing elit? Aenean commodo ligula
# eget dolor; Aenean massa! Cum sociis natoque penatibus et magnis dis parturient
# montes, nascetur ridiculus mus; Donec quam felis, ultricies nec, pellentesque
# eu, pretium quis, sem; Nulla consequat massa quis enim. Donec pede justo,
# fringilla vel, aliquet nec, vulputate eget, arcu! In enim justo, rhoncus ut,
# imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium?
# Integer tincidunt! Cras dapibus. Vivamus elementum semper nisi! Aenean vulputate
# eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac,
# enim; Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus? Phasellus
# viverra nulla ut metus varius laoreet. Quisque rutrum. Aenean imperdiet? Etiam
# ultricies nisi vel augue! Curabitur ullamcorper ultricies nisi! Nam eget dui?
# Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula
# eget dolor! Aenean massa? Cum sociis natoque penatibus et magnis dis parturient
# montes, nascetur ridiculus mus; Donec quam felis, ultricies nec, pellentesque
# eu, pretium quis, sem? Nulla consequat massa quis enim; Donec pede justo,
# fringilla vel, aliquet nec, vulputate eget, arcu; In enim justo, rhoncus ut,
# imperdiet a, venenatis vitae, justo! Nullam dictum felis eu pede mollis pretium;
# Integer tincidunt; Cras dapibus? Vivamus elementum semper nisi? Aenean vulputate
# eleifend tellus! Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac,
# enim! Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus! Phasellus
# viverra nulla ut metus varius laoreet. Quisque rutrum. Aenean imperdiet! Etiam
# ultricies nisi vel augue! Curabitur ullamcorper ultricies nisi; Nam eget dui!
# Lorem ipsum dolor sit amet, consectetuer adipiscing elit? Aenean commodo ligula
# eget dolor? Aenean massa. Cum sociis natoque penatibus et magnis dis parturient
# montes, nascetur ridiculus mus? Donec quam felis, ultricies nec, pellentesque
# eu, pretium quis, sem; Nulla consequat massa quis enim; Donec pede justo,
# fringilla vel, aliquet nec, vulputate eget, arcu! In enim justo, rhoncus ut,
# imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium;
# Integer tincidunt! Cras dapibus? Vivamus elementum semper nisi? Aenean vulputate
# eleifend tellus? Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac,
# enim; Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus? Phasellus
# viverra nulla ut metus varius laoreet? Quisque rutrum! Aenean imperdiet? Etiam
# ultricies nisi vel augue; Curabitur ullamcorper ultricies nisi! Nam eget dui.
# Lorem ipsum dolor sit amet, consectetuer adipiscing elit; Aenean commodo ligula
# eget dolor? Aenean massa.
# Heres a bunch of lorem ipsum because GitHub keeps saying this is an HTML project...
# Lorem ipsum dolor sit amet, consectetuer adipiscing elit; Aenean commodo ligula
# eget dolor. Aenean massa? Cum sociis natoque penatibus et magnis dis parturient
# montes, nascetur ridiculus mus; Donec quam felis, ultricies nec, pellentesque
# eu, pretium quis, sem? Nulla consequat massa quis enim? Donec pede justo,
# fringilla vel, aliquet nec, vulputate eget, arcu; In enim justo, rhoncus ut,
# imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium?
# Integer tincidunt; Cras dapibus! Vivamus elementum semper nisi; Aenean vulputate
# eleifend tellus! Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac,
# enim; Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus; Phasellus
# viverra nulla ut metus varius laoreet! Quisque rutrum? Aenean imperdiet! Etiam
# ultricies nisi vel augue; Curabitur ullamcorper ultricies nisi? Nam eget dui;
# Lorem ipsum dolor sit amet, consectetuer adipiscing elit? Aenean commodo ligula
# eget dolor! Aenean massa? Cum sociis natoque penatibus et magnis dis parturient
# montes, nascetur ridiculus mus; Donec quam felis, ultricies nec, pellentesque
# eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo,
# fringilla vel, aliquet nec, vulputate eget, arcu; In enim justo, rhoncus ut,
# imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium.
# Integer tincidunt; Cras dapibus; Vivamus elementum semper nisi? Aenean vulputate
# eleifend tellus; Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac,
# enim. Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus? Phasellus
# viverra nulla ut metus varius laoreet; Quisque rutrum! Aenean imperdiet? Etiam
# ultricies nisi vel augue; Curabitur ullamcorper ultricies nisi; Nam eget dui.
# Lorem ipsum dolor sit amet, consectetuer adipiscing elit; Aenean commodo ligula
# eget dolor? Aenean massa. Cum sociis natoque penatibus et magnis dis parturient
# montes, nascetur ridiculus mus? Donec quam felis, ultricies nec, pellentesque
# eu, pretium quis, sem; Nulla consequat massa quis enim. Donec pede justo,
# fringilla vel, aliquet nec, vulputate eget, arcu! In enim justo, rhoncus ut,
# imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium?
# Integer tincidunt! Cras dapibus; Vivamus elementum semper nisi! Aenean vulputate
# eleifend tellus? Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac,
# enim; Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus! Phasellus
# viverra nulla ut metus varius laoreet; Quisque rutrum! Aenean imperdiet. Etiam
# ultricies nisi vel augue; Curabitur ullamcorper ultricies nisi; Nam eget dui;
# Lorem ipsum dolor sit amet, consectetuer adipiscing elit; Aenean commodo ligula
# eget dolor? Aenean massa! Cum sociis natoque penatibus et magnis dis parturient
# montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque
# eu, pretium quis, sem; Nulla consequat massa quis enim? Donec pede justo,
# fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut,
# imperdiet a, venenatis vitae, justo; Nullam dictum felis eu pede mollis pretium;
# Integer tincidunt. Cras dapibus! Vivamus elementum semper nisi! Aenean vulputate
# eleifend tellus! Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac,
# enim! Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus. Phasellus
# viverra nulla ut metus varius laoreet? Quisque rutrum? Aenean imperdiet! Etiam
# ultricies nisi vel augue! Curabitur ullamcorper ultricies nisi. Nam eget dui?
# Lorem ipsum dolor sit amet, consectetuer adipiscing elit? Aenean commodo ligula
# eget dolor; Aenean massa! Cum sociis natoque penatibus et magnis dis parturient
# montes, nascetur ridiculus mus; Donec quam felis, ultricies nec, pellentesque
# eu, pretium quis, sem; Nulla consequat massa quis enim. Donec pede justo,
# fringilla vel, aliquet nec, vulputate eget, arcu! In enim justo, rhoncus ut,
# imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium?
# Integer tincidunt! Cras dapibus. Vivamus elementum semper nisi! Aenean vulputate
# eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac,
# enim; Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus? Phasellus
# viverra nulla ut metus varius laoreet. Quisque rutrum. Aenean imperdiet? Etiam
# ultricies nisi vel augue! Curabitur ullamcorper ultricies nisi! Nam eget dui?
# Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula
# eget dolor! Aenean massa? Cum sociis natoque penatibus et magnis dis parturient
# montes, nascetur ridiculus mus; Donec quam felis, ultricies nec, pellentesque
# eu, pretium quis, sem? Nulla consequat massa quis enim; Donec pede justo,
# fringilla vel, aliquet nec, vulputate eget, arcu; In enim justo, rhoncus ut,
# imperdiet a, venenatis vitae, justo! Nullam dictum felis eu pede mollis pretium;
# Integer tincidunt; Cras dapibus? Vivamus elementum semper nisi? Aenean vulputate
# eleifend tellus! Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac,
# enim! Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus! Phasellus
# viverra nulla ut metus varius laoreet. Quisque rutrum. Aenean imperdiet! Etiam
# ultricies nisi vel augue! Curabitur ullamcorper ultricies nisi; Nam eget dui!
# Lorem ipsum dolor sit amet, consectetuer adipiscing elit? Aenean commodo ligula
# eget dolor? Aenean massa. Cum sociis natoque penatibus et magnis dis parturient
# montes, nascetur ridiculus mus? Donec quam felis, ultricies nec, pellentesque
# eu, pretium quis, sem; Nulla consequat massa quis enim; Donec pede justo,
# fringilla vel, aliquet nec, vulputate eget, arcu! In enim justo, rhoncus ut,
# imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium;
# Integer tincidunt! Cras dapibus? Vivamus elementum semper nisi? Aenean vulputate
# eleifend tellus? Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac,
# enim; Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus? Phasellus
# viverra nulla ut metus varius laoreet? Quisque rutrum! Aenean imperdiet? Etiam
# ultricies nisi vel augue; Curabitur ullamcorper ultricies nisi! Nam eget dui.
# Lorem ipsum dolor sit amet, consectetuer adipiscing elit; Aenean commodo ligula
# eget dolor? Aenean massa.
# Heres a bunch of lorem ipsum because GitHub keeps saying this is an HTML project...
# Lorem ipsum dolor sit amet, consectetuer adipiscing elit; Aenean commodo ligula
# eget dolor. Aenean massa? Cum sociis natoque penatibus et magnis dis parturient
# montes, nascetur ridiculus mus; Donec quam felis, ultricies nec, pellentesque
# eu, pretium quis, sem? Nulla consequat massa quis enim? Donec pede justo,
# fringilla vel, aliquet nec, vulputate eget, arcu; In enim justo, rhoncus ut,
# imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium?
# Integer tincidunt; Cras dapibus! Vivamus elementum semper nisi; Aenean vulputate
# eleifend tellus! Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac,
# enim; Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus; Phasellus
# viverra nulla ut metus varius laoreet! Quisque rutrum? Aenean imperdiet! Etiam
# ultricies nisi vel augue; Curabitur ullamcorper ultricies nisi? Nam eget dui;
# Lorem ipsum dolor sit amet, consectetuer adipiscing elit? Aenean commodo ligula
# eget dolor! Aenean massa? Cum sociis natoque penatibus et magnis dis parturient
# montes, nascetur ridiculus mus; Donec quam felis, ultricies nec, pellentesque
# eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo,
# fringilla vel, aliquet nec, vulputate eget, arcu; In enim justo, rhoncus ut,
# imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium.
# Integer tincidunt; Cras dapibus; Vivamus elementum semper nisi? Aenean vulputate
# eleifend tellus; Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac,
# enim. Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus? Phasellus
# viverra nulla ut metus varius laoreet; Quisque rutrum! Aenean imperdiet? Etiam
# ultricies nisi vel augue; Curabitur ullamcorper ultricies nisi; Nam eget dui.
# Lorem ipsum dolor sit amet, consectetuer adipiscing elit; Aenean commodo ligula
# eget dolor? Aenean massa. Cum sociis natoque penatibus et magnis dis parturient
# montes, nascetur ridiculus mus? Donec quam felis, ultricies nec, pellentesque
# eu, pretium quis, sem; Nulla consequat massa quis enim. Donec pede justo,
# fringilla vel, aliquet nec, vulputate eget, arcu! In enim justo, rhoncus ut,
# imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium?
# Integer tincidunt! Cras dapibus; Vivamus elementum semper nisi! Aenean vulputate
# eleifend tellus? Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac,
# enim; Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus! Phasellus
# viverra nulla ut metus varius laoreet; Quisque rutrum! Aenean imperdiet. Etiam
# ultricies nisi vel augue; Curabitur ullamcorper ultricies nisi; Nam eget dui;
# Lorem ipsum dolor sit amet, consectetuer adipiscing elit; Aenean commodo ligula
# eget dolor? Aenean massa! Cum sociis natoque penatibus et magnis dis parturient
# montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque
# eu, pretium quis, sem; Nulla consequat massa quis enim? Donec pede justo,
# fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut,
# imperdiet a, venenatis vitae, justo; Nullam dictum felis eu pede mollis pretium;
# Integer tincidunt. Cras dapibus! Vivamus elementum semper nisi! Aenean vulputate
# eleifend tellus! Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac,
# enim! Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus. Phasellus
# viverra nulla ut metus varius laoreet? Quisque rutrum? Aenean imperdiet! Etiam
# ultricies nisi vel augue! Curabitur ullamcorper ultricies nisi. Nam eget dui?
# Lorem ipsum dolor sit amet, consectetuer adipiscing elit? Aenean commodo ligula
# eget dolor; Aenean massa! Cum sociis natoque penatibus et magnis dis parturient
# montes, nascetur ridiculus mus; Donec quam felis, ultricies nec, pellentesque
# eu, pretium quis, sem; Nulla consequat massa quis enim. Donec pede justo,
# fringilla vel, aliquet nec, vulputate eget, arcu! In enim justo, rhoncus ut,
# imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium?
# Integer tincidunt! Cras dapibus. Vivamus elementum semper nisi! Aenean vulputate
# eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac,
# enim; Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus? Phasellus
# viverra nulla ut metus varius laoreet. Quisque rutrum. Aenean imperdiet? Etiam
# ultricies nisi vel augue! Curabitur ullamcorper ultricies nisi! Nam eget dui?
# Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula
# eget dolor! Aenean massa? Cum sociis natoque penatibus et magnis dis parturient
# montes, nascetur ridiculus mus; Donec quam felis, ultricies nec, pellentesque
# eu, pretium quis, sem? Nulla consequat massa quis enim; Donec pede justo,
# fringilla vel, aliquet nec, vulputate eget, arcu; In enim justo, rhoncus ut,
# imperdiet a, venenatis vitae, justo! Nullam dictum felis eu pede mollis pretium;
# Integer tincidunt; Cras dapibus? Vivamus elementum semper nisi? Aenean vulputate
# eleifend tellus! Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac,
# enim! Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus! Phasellus
# viverra nulla ut metus varius laoreet. Quisque rutrum. Aenean imperdiet! Etiam
# ultricies nisi vel augue! Curabitur ullamcorper ultricies nisi; Nam eget dui!
# Lorem ipsum dolor sit amet, consectetuer adipiscing elit? Aenean commodo ligula
# eget dolor? Aenean massa. Cum sociis natoque penatibus et magnis dis parturient
# montes, nascetur ridiculus mus? Donec quam felis, ultricies nec, pellentesque
# eu, pretium quis, sem; Nulla consequat massa quis enim; Donec pede justo,
# fringilla vel, aliquet nec, vulputate eget, arcu! In enim justo, rhoncus ut,
# imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium;
# Integer tincidunt! Cras dapibus? Vivamus elementum semper nisi? Aenean vulputate
# eleifend tellus? Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac,
# enim; Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus? Phasellus
# viverra nulla ut metus varius laoreet? Quisque rutrum! Aenean imperdiet? Etiam
# ultricies nisi vel augue; Curabitur ullamcorper ultricies nisi! Nam eget dui.
# Lorem ipsum dolor sit amet, consectetuer adipiscing elit; Aenean commodo ligula
# eget dolor? Aenean massa.
# Heres a bunch of lorem ipsum because GitHub keeps saying this is an HTML project...
# Lorem ipsum dolor sit amet, consectetuer adipiscing elit; Aenean commodo ligula
# eget dolor. Aenean massa? Cum sociis natoque penatibus et magnis dis parturient
# montes, nascetur ridiculus mus; Donec quam felis, ultricies nec, pellentesque
# eu, pretium quis, sem? Nulla consequat massa quis enim? Donec pede justo,
# fringilla vel, aliquet nec, vulputate eget, arcu; In enim justo, rhoncus ut,
# imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium?
# Integer tincidunt; Cras dapibus! Vivamus elementum semper nisi; Aenean vulputate
# eleifend tellus! Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac,
# enim; Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus; Phasellus
# viverra nulla ut metus varius laoreet! Quisque rutrum? Aenean imperdiet! Etiam
# ultricies nisi vel augue; Curabitur ullamcorper ultricies nisi? Nam eget dui;
# Lorem ipsum dolor sit amet, consectetuer adipiscing elit? Aenean commodo ligula
# eget dolor! Aenean massa? Cum sociis natoque penatibus et magnis dis parturient
# montes, nascetur ridiculus mus; Donec quam felis, ultricies nec, pellentesque
# eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo,
# fringilla vel, aliquet nec, vulputate eget, arcu; In enim justo, rhoncus ut,
# imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium.
# Integer tincidunt; Cras dapibus; Vivamus elementum semper nisi? Aenean vulputate
# eleifend tellus; Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac,
# enim. Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus? Phasellus
# viverra nulla ut metus varius laoreet; Quisque rutrum! Aenean imperdiet? Etiam
# ultricies nisi vel augue; Curabitur ullamcorper ultricies nisi; Nam eget dui.
# Lorem ipsum dolor sit amet, consectetuer adipiscing elit; Aenean commodo ligula
# eget dolor? Aenean massa. Cum sociis natoque penatibus et magnis dis parturient
# montes, nascetur ridiculus mus? Donec quam felis, ultricies nec, pellentesque
# eu, pretium quis, sem; Nulla consequat massa quis enim. Donec pede justo,
# fringilla vel, aliquet nec, vulputate eget, arcu! In enim justo, rhoncus ut,
# imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium?
# Integer tincidunt! Cras dapibus; Vivamus elementum semper nisi! Aenean vulputate
# eleifend tellus? Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac,
# enim; Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus! Phasellus
# viverra nulla ut metus varius laoreet; Quisque rutrum! Aenean imperdiet. Etiam
# ultricies nisi vel augue; Curabitur ullamcorper ultricies nisi; Nam eget dui;
# Lorem ipsum dolor sit amet, consectetuer adipiscing elit; Aenean commodo ligula
# eget dolor? Aenean massa! Cum sociis natoque penatibus et magnis dis parturient
# montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque
# eu, pretium quis, sem; Nulla consequat massa quis enim? Donec pede justo,
# fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut,
# imperdiet a, venenatis vitae, justo; Nullam dictum felis eu pede mollis pretium;
# Integer tincidunt. Cras dapibus! Vivamus elementum semper nisi! Aenean vulputate
# eleifend tellus! Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac,
# enim! Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus. Phasellus
# viverra nulla ut metus varius laoreet? Quisque rutrum? Aenean imperdiet! Etiam
# ultricies nisi vel augue! Curabitur ullamcorper ultricies nisi. Nam eget dui?
# Lorem ipsum dolor sit amet, consectetuer adipiscing elit? Aenean commodo ligula
# eget dolor; Aenean massa! Cum sociis natoque penatibus et magnis dis parturient
# montes, nascetur ridiculus mus; Donec quam felis, ultricies nec, pellentesque
# eu, pretium quis, sem; Nulla consequat massa quis enim. Donec pede justo,
# fringilla vel, aliquet nec, vulputate eget, arcu! In enim justo, rhoncus ut,
# imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium?
# Integer tincidunt! Cras dapibus. Vivamus elementum semper nisi! Aenean vulputate
# eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac,
# enim; Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus? Phasellus
# viverra nulla ut metus varius laoreet. Quisque rutrum. Aenean imperdiet? Etiam
# ultricies nisi vel augue! Curabitur ullamcorper ultricies nisi! Nam eget dui?
# Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula
# eget dolor! Aenean massa? Cum sociis natoque penatibus et magnis dis parturient
# montes, nascetur ridiculus mus; Donec quam felis, ultricies nec, pellentesque
# eu, pretium quis, sem? Nulla consequat massa quis enim; Donec pede justo,
# fringilla vel, aliquet nec, vulputate eget, arcu; In enim justo, rhoncus ut,
# imperdiet a, venenatis vitae, justo! Nullam dictum felis eu pede mollis pretium;
# Integer tincidunt; Cras dapibus? Vivamus elementum semper nisi? Aenean vulputate
# eleifend tellus! Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac,
# enim! Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus! Phasellus
# viverra nulla ut metus varius laoreet. Quisque rutrum. Aenean imperdiet! Etiam
# ultricies nisi vel augue! Curabitur ullamcorper ultricies nisi; Nam eget dui!
# Lorem ipsum dolor sit amet, consectetuer adipiscing elit? Aenean commodo ligula
# eget dolor? Aenean massa. Cum sociis natoque penatibus et magnis dis parturient
# montes, nascetur ridiculus mus? Donec quam felis, ultricies nec, pellentesque
# eu, pretium quis, sem; Nulla consequat massa quis enim; Donec pede justo,
# fringilla vel, aliquet nec, vulputate eget, arcu! In enim justo, rhoncus ut,
# imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium;
# Integer tincidunt! Cras dapibus? Vivamus elementum semper nisi? Aenean vulputate
# eleifend tellus? Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac,
# enim; Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus? Phasellus
# viverra nulla ut metus varius laoreet? Quisque rutrum! Aenean imperdiet? Etiam
# ultricies nisi vel augue; Curabitur ullamcorper ultricies nisi! Nam eget dui.
# Lorem ipsum dolor sit amet, consectetuer adipiscing elit; Aenean commodo ligula
# eget dolor? Aenean massa.
