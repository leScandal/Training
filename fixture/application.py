from selenium import webdriver
from fixture.session import SessionHelper
from fixture.contact import ContactHelper
from fixture.group import GroupHelper


class Application:
   def __init__ (self, browser, base_url):
       if browser == "firefox":
            self.wd = webdriver.Firefox(capabilities={'marionette': False})
       elif browser == "chrome":
            self.wd = webdriver.Chrome()
       elif browser == "ie":
           self.wd = webdriver.Ie()
       else:
           raise ValueError ("Unknown browser %s" %browser)
       self.session = SessionHelper(self)
       self.contact = ContactHelper(self)
       self.group = GroupHelper(self)
       self.base_url = base_url


   def is_valid(self):
       try:
           self.wd.current_url
           return True
       except:
           return False



   def open_HP(self):
       wd = self.wd
       wd.get(self.base_url)


   def stop(self):
       self.wd.quit()


