from selenium import webdriver
from time import sleep


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

SiteBot()
