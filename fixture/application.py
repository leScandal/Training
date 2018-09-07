from selenium.webdriver.chrome.webdriver import WebDriver
from fixture.session import SessionHelper
from fixture.contact import ContactHelper
from fixture.group import GroupHelper


class Application:
   def __init__ (self):
       self.wd = WebDriver()
       self.wd.implicitly_wait(61)
       self.session = SessionHelper(self)
       self.contact = ContactHelper(self)
       self.group = GroupHelper(self)


   def is_valid(self):
       try:
           self.wd.current_url
           return True
       except:
           return False



   def open_HP(self):
       wd = self.wd
       wd.get("http://localhost/addressbook/")


   def stop(self):
       self.wd.quit()


