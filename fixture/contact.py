from model.Contacts import Contacts
class ContactHelper:


   def __init__(self, app):
       self.app = app

   def add(self, Contacts):
       # add_contact
       wd = self.app.wd
       wd.find_element_by_link_text("add new").click()
       self.change_name_value("firstname", Contacts.name)
       wd.find_element_by_name("theform").click()
       self.change_name_value("middlename", Contacts.middleN)
       wd.find_element_by_name("theform").click()
       self.change_name_value("lastname", Contacts.lastN)
       self.change_name_value("nickname", Contacts.nickN)
       #wd.find_element_by_name("photo").click()
       self.change_name_value("title", Contacts.title)
       self.change_name_value("company", Contacts.company)
       wd.find_element_by_name("theform").click()
       self.change_name_value("address", Contacts.address)
       self.change_name_value("home", Contacts.home)
       self.change_name_value("mobile", Contacts.mobile)
       self.change_name_value("work", Contacts.work)
       self.change_name_value("fax", Contacts.fax)
       wd.find_element_by_name("theform").click()
       self.change_name_value("email", Contacts.email1)
       self.change_name_value("email2", Contacts.email2)
       self.change_name_value("email3", Contacts.email3)
       self.change_name_value("homepage", Contacts.HP)
       # if not wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[19]").is_selected():
       #     wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[19]").click()
       # if not wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[2]").is_selected():
       #     wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[2]").click()
       # wd.find_element_by_name("byear").click()
       # wd.find_element_by_name("byear").clear()
       # wd.find_element_by_name("byear").send_keys("2019")
       # if not wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[21]").is_selected():
       #     wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[21]").click()
       # if not wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[5]").is_selected():
       #     wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[5]").click()
       # wd.find_element_by_name("ayear").click()
       # wd.find_element_by_name("ayear").clear()
       # wd.find_element_by_name("ayear").send_keys("2021")
       # empty group
       #self.into_empty_group()
       self.change_name_value("address2", Contacts.address2)
       self.change_name_value("phone2", Contacts.address3)
       self.change_name_value("notes", Contacts.notes)
       wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
       self.return_to_HP()
       #wd.find_element_by_link_text("home").click()
       self.contact_cashe = None

   def into_empty_group(self):
       wd = self.app.wd
       if not wd.find_element_by_xpath("//div[@id='content']/form/select[5]//option[2]").is_selected():
           wd.find_element_by_xpath("//div[@id='content']/form/select[5]//option[2]").click()


   def return_to_HP(self):
       wd = self.app.wd
       wd.find_element_by_link_text("home page").click()


   def del_Cont(self):
       wd = self.app.wd
       wd.find_element_by_name("selected[]").click()
       wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
       wd.switch_to_alert().accept()
       wd.find_element_by_link_text("home").click()
       self.contact_cashe = None


   def del_Cont_by_index(self, index):
       wd = self.app.wd
       self.select_contact_by_index(index)
       wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
       wd.switch_to_alert().accept()
       wd.find_element_by_link_text("home").click()
       self.contact_cashe = None


   def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

   def count(self):
       wd = self.app.wd
       return len(wd.find_elements_by_name("selected[]"))

   def change_name_value(self, field_name, text):
       wd = self.app.wd
       if text is not None:
           wd.find_element_by_name(field_name).click()
           wd.find_element_by_name(field_name).clear()
           wd.find_element_by_name(field_name).send_keys(text)

   contact_cashe = None

   def get_con_list(self):
       if self.contact_cashe is None:
            wd = self.app.wd
            self.contact_cashe = list()
            for element in wd.find_elements_by_name("entry"):
                list2 = element.find_elements_by_tag_name("td")
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.contact_cashe.append(Contacts(lastN = list2[1].text, name=list2[2].text, address = list2[3].text, id=id))
       return list(self.contact_cashe)





