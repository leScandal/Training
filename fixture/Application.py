from selenium.webdriver.chrome.webdriver import WebDriver
from fixture.session import SessionHelper
from fixture.contact import ContactHelper

class Application:
   def __init__ (self):
       self.wd = WebDriver()
       self.wd.implicitly_wait(60)
       self.application = SessionHelper(self)
       self.contact = ContactHelper(self)


   def open_HP(self):
       wd = self.wd
       wd.get("http://localhost/addressbook/")


   def stop(self):
       self.wd.quit()