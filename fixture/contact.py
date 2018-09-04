from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
class ContactHelper:

   def __init__(self, app):
       self.app = app

   def add(self, Contacts):
       # add_contact
       wd = self.app.wd
       wd.find_element_by_link_text("add new").click()
       wd.find_element_by_name("firstname").click()
       wd.find_element_by_name("firstname").clear()
       wd.find_element_by_name("firstname").send_keys(Contacts.name)
       wd.find_element_by_name("theform").click()
       wd.find_element_by_name("middlename").click()
       wd.find_element_by_name("middlename").clear()
       wd.find_element_by_name("middlename").send_keys(Contacts.middleN)
       wd.find_element_by_name("theform").click()
       wd.find_element_by_name("lastname").click()
       wd.find_element_by_name("lastname").clear()
       wd.find_element_by_name("lastname").send_keys(Contacts.lastN)
       wd.find_element_by_name("nickname").click()
       wd.find_element_by_name("nickname").clear()
       wd.find_element_by_name("nickname").send_keys(Contacts.nickN)
       #wd.find_element_by_name("photo").click()
       wd.find_element_by_name("title").click()
       wd.find_element_by_name("title").clear()
       wd.find_element_by_name("title").send_keys(Contacts.title)
       wd.find_element_by_name("company").click()
       wd.find_element_by_name("company").clear()
       wd.find_element_by_name("company").send_keys(Contacts.company)
       wd.find_element_by_name("theform").click()
       wd.find_element_by_name("address").click()
       wd.find_element_by_name("address").clear()
       wd.find_element_by_name("address").send_keys(Contacts.address)
       wd.find_element_by_name("home").click()
       wd.find_element_by_name("home").clear()
       wd.find_element_by_name("home").send_keys(Contacts.home)
       wd.find_element_by_name("mobile").click()
       wd.find_element_by_name("mobile").clear()
       wd.find_element_by_name("mobile").send_keys(Contacts.mobile)
       wd.find_element_by_name("work").click()
       wd.find_element_by_name("work").clear()
       wd.find_element_by_name("work").send_keys(Contacts.work)
       wd.find_element_by_name("fax").click()
       wd.find_element_by_name("fax").clear()
       wd.find_element_by_name("fax").send_keys(Contacts.fax)
       wd.find_element_by_name("theform").click()
       wd.find_element_by_name("email").click()
       wd.find_element_by_name("email").clear()
       wd.find_element_by_name("email").send_keys(Contacts.email1)
       wd.find_element_by_name("email2").click()
       wd.find_element_by_name("email2").clear()
       wd.find_element_by_name("email2").send_keys(Contacts.email2)
       wd.find_element_by_name("email3").click()
       wd.find_element_by_name("email3").clear()
       wd.find_element_by_name("email3").send_keys(Contacts.email3)
       wd.find_element_by_name("homepage").click()
       wd.find_element_by_name("homepage").clear()
       wd.find_element_by_name("homepage").send_keys(Contacts.HP)
       if not wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[19]").is_selected():
           wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[19]").click()
       if not wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[2]").is_selected():
           wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[2]").click()
       wd.find_element_by_name("byear").click()
       wd.find_element_by_name("byear").clear()
       wd.find_element_by_name("byear").send_keys("2019")
       if not wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[21]").is_selected():
           wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[21]").click()
       if not wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[5]").is_selected():
           wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[5]").click()
       wd.find_element_by_name("ayear").click()
       wd.find_element_by_name("ayear").clear()
       wd.find_element_by_name("ayear").send_keys("2021")
       # empty group
       self.into_empty_group()

       wd.find_element_by_name("address2").click()
       wd.find_element_by_name("address2").clear()
       wd.find_element_by_name("address2").send_keys(Contacts.address2)
       wd.find_element_by_name("phone2").click()
       wd.find_element_by_name("phone2").clear()
       wd.find_element_by_name("phone2").send_keys(Contacts.address3)
       wd.find_element_by_name("notes").click()
       wd.find_element_by_name("notes").clear()
       wd.find_element_by_name("notes").send_keys(Contacts.notes)
       wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

   def into_empty_group(self):
       wd = self.app.wd
       if not wd.find_element_by_xpath("//div[@id='content']/form/select[5]//option[2]").is_selected():
           wd.find_element_by_xpath("//div[@id='content']/form/select[5]//option[2]").click()

   def del_Cont(self):
       # open_contact_page
       wd = self.app.wd
       wd.find_element_by_name("selected[]").click()
       wd.find_element_by_xpath ((By.XPATH, '//button[text="delete"]')).click()
       wd.switch_to_alert().accept()


