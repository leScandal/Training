# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

success = True
wd = WebDriver()
wd.implicitly_wait(60)

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

try:
    wd.get("http://localhost/addressbook/")
    wd.find_element_by_name("pass").click()
    wd.find_element_by_name("pass").send_keys("\\undefined")
    wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()
    if not wd.find_element_by_id("140").is_selected():
        wd.find_element_by_id("140").click()
    wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[12]/td[8]/a/img").click()
    wd.find_element_by_link_text("groups").click()
    if not wd.find_element_by_xpath("//div[@id='content']/form/span[2]/input").is_selected():
        wd.find_element_by_xpath("//div[@id='content']/form/span[2]/input").click()
    wd.find_element_by_name("edit").click()
    wd.find_element_by_link_text("home").click()
    if not wd.find_element_by_xpath("//div[@class='right']/select//option[2]").is_selected():
        wd.find_element_by_xpath("//div[@class='right']/select//option[2]").click()
    if not wd.find_element_by_id("155").is_selected():
        wd.find_element_by_id("155").click()
    if not wd.find_element_by_id("153").is_selected():
        wd.find_element_by_id("153").click()
    if wd.find_element_by_id("155").is_selected():
        wd.find_element_by_id("155").click()
    if wd.find_element_by_id("153").is_selected():
        wd.find_element_by_id("153").click()
    if not wd.find_element_by_id("142").is_selected():
        wd.find_element_by_id("142").click()
    if not wd.find_element_by_id("152").is_selected():
        wd.find_element_by_id("152").click()
    wd.find_element_by_name("add").click()
finally:
    wd.quit()
    if not success:
        raise Exception("Test failed.")
