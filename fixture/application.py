from selenium.webdriver.chrome.webdriver import WebDriver
from fixture.session import SessionHelper
from fixture.contact import ContactHelper
from fixture.group import GroupHelper
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

class Application:
   def __init__ (self):
       self.wd = WebDriver()
       self.wd.implicitly_wait(61)
       self.session = SessionHelper(self)
       self.contact = ContactHelper(self)
       self.group = GroupHelper(self)

   def open_HP(self):
       wd = self.wd
       wd.get("http://localhost/addressbook/")


   def stop(self):
       self.wd.quit()
