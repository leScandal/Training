from model.contacts import Contacts
import re
class ContactHelper:


   def __init__(self, app):
       self.app = app

   def add(self, contacts):
       # add_contact
       wd = self.app.wd
       wd.find_element_by_link_text("add new").click()
       self.change_name_value("firstname", contacts.name)
       wd.find_element_by_name("theform").click()
       self.change_name_value("middlename", contacts.middleN)
       wd.find_element_by_name("theform").click()
       self.change_name_value("lastname", contacts.lastN)
       self.change_name_value("nickname", contacts.nickN)
       #wd.find_element_by_name("photo").click()
       self.change_name_value("title", contacts.title)
       self.change_name_value("company", contacts.company)
       wd.find_element_by_name("theform").click()
       self.change_name_value("address", contacts.address)
       self.change_name_value("home", contacts.home)
       self.change_name_value("mobile", contacts.mobile)
       self.change_name_value("work", contacts.work)
       self.change_name_value("fax", contacts.fax)
       wd.find_element_by_name("theform").click()
       self.change_name_value("email", contacts.email1)
       self.change_name_value("email2", contacts.email2)
       self.change_name_value("email3", contacts.email3)
       self.change_name_value("homepage", contacts.HP)
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
       self.change_name_value("address2", contacts.address2)
       self.change_name_value("phone2", contacts.phone2)
       self.change_name_value("notes", contacts.notes)
       wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
       self.return_to_HP()
       #wd.find_element_by_link_text("home").click()
       self.contact_cache = None


   def add_form(self, contacts):
       # add_contact
       wd = self.app.wd
       wd.find_element_by_link_text("add new").click()
       self.fill_contact_form(contacts)
       wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
       self.return_to_HP()
       #wd.find_element_by_link_text("home").click()
       self.contact_cache = None


   def into_empty_group(self):
       wd = self.app.wd
       if not wd.find_element_by_xpath("//div[@id='content']/form/select[5]//option[2]").is_selected():
           wd.find_element_by_xpath("//div[@id='content']/form/select[5]//option[2]").click()


   def return_to_HP(self):
       wd = self.app.wd
       wd.find_element_by_link_text("home").click()
       #wd.find_element_by_link_text("home page").click()

   def del_Cont(self):
       wd = self.app.wd
       wd.find_element_by_name("selected[]").click()
       wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
       wd.switch_to_alert().accept()
       wd.find_element_by_link_text("home").click()
       self.contact_cache = None


   def del_Cont_by_index(self, index):
       wd = self.app.wd
       self.select_contact_by_index(index)
       wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
       wd.switch_to_alert().accept()
       wd.find_element_by_link_text("home").click()
       self.contact_cache = None


   def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()


   def del_Cont_by_id(self, id):
       wd = self.app.wd
       self.select_contact_by_id(id)
       wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
       wd.switch_to_alert().accept()
       wd.find_element_by_link_text("home").click()
       self.contact_cache = None


   def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value = '%s']" %id).click()


   def count(self):
       wd = self.app.wd
       return len(wd.find_elements_by_name("selected[]"))


   def change_name_value(self, field_name, text):
       wd = self.app.wd
       if text is not None:
           wd.find_element_by_name(field_name).click()
           wd.find_element_by_name(field_name).clear()
           wd.find_element_by_name(field_name).send_keys(text)

   contact_cache = None

   def get_cont_list(self):
       if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_HP()
            self.contact_cache = list()
            for element in wd.find_elements_by_name("entry"):
                list2 = element.find_elements_by_tag_name("td")
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.contact_cache.append(Contacts(lastN = list2[1].text,
                                                   name=list2[2].text,
                                                   address = list2[3].text,
                                                   id=id,
                                                   all_phones_from_HP = list2[5].text,
                                                   all_mails_from_HP = list2[4].text))
                                                   # home=all_phones[0]
                                                   # mobile=all_phones[1],
                                                   # work=all_phones[2],
                                                   # phone2 = all_phones[3]))
       return list(self.contact_cache)


   def open_cont_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_HP()
        list2 = wd.find_elements_by_name("entry")[index]
        pencil = list2.find_elements_by_tag_name("td")[7]
        pencil.find_element_by_tag_name("a").click()


   def open_cont_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_HP()
        list2 = wd.find_elements_by_name("entry")[index]
        details = list2.find_elements_by_tag_name("td")[6]
        details.find_element_by_tag_name("a").click()


   def get_cont_from_view_page(self, index):
        wd = self.app.wd
        self.open_cont_view_by_index(index)
        list1 = wd.find_element_by_id("content").text
        home = re.search( "H: (.*)", list1).group(1)
        work = re.search("W: (.*)", list1).group(1)
        mobile = re.search("M: (.*)", list1).group(1)
        secondary = re.search("P: (.*)", list1).group(1)
        return Contacts(home = home, mobile = mobile, work = work, phone2=secondary)


   def get_cont_info_from_edit_page(self, index):
       wd = self.app.wd
       self.open_cont_to_edit_by_index(index)
       firstname = wd.find_element_by_name("firstname").get_attribute("value")
       lastname = wd.find_element_by_name("lastname").get_attribute("value")
       middlename = wd.find_element_by_name("middlename").get_attribute("value")
       id = wd.find_element_by_name("id").get_attribute("value")
       address = wd.find_element_by_name("address").get_attribute("value")
       home = wd.find_element_by_name("home").get_attribute("value")
       mobile = wd.find_element_by_name("mobile").get_attribute("value")
       work = wd.find_element_by_name("work").get_attribute("value")
       fax = wd.find_element_by_name("fax").get_attribute("value")
       secondary = wd.find_element_by_name("phone2").get_attribute("value")
       email1 = wd.find_element_by_name("email").get_attribute("value")
       email2 = wd.find_element_by_name("email2").get_attribute("value")
       email3 = wd.find_element_by_name("email3").get_attribute("value")
       return Contacts(lastN = lastname, name=firstname, middleN = middlename, id=id, address=address, home = home,
                       mobile = mobile, work = work, fax = fax, phone2=secondary, email1 = email1 , email2 = email2, email3 = email3)


   def edit_contact_by_index(self, index, new_data):
        wd = self.app.wd
        self.app.open_HP()
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[" +str(index+2) + "]/td[8]/a/img").click()
        self.fill_contact_form(new_data)
        wd.find_element_by_name("update").click()
        self.app.open_HP()
        self.contact_cache = None


   def edit_contact_by_id(self, id, new_data):
        wd = self.app.wd
        self.app.open_HP()
        self.select_cont_by_id(id)
        wd.find_element_by_tag_name("a").click()
        self.fill_contact_form(new_data)
        wd.find_element_by_name("update").click()
        self.app.open_HP()
        self.contact_cache = None


   def select_cont_by_id(self, id):
       wd = self.app.wd
       #wd.find_element_by_id(id).click()
       wd.find_element_by_css_selector("input[value='%s']" % id).click()
       #wd.find_element_by_xpath("//*[@id='%s']" % id).click()

       # find_elements_by_xpath(".//*[@title='Edit']"))
       # row = wd.find_elements_by_name("entry")[index]
       # cell = row.find_elements_by_tag_name("td")[7]
       # cell.find_element_by_tag_name("a").click()


   def fill_contact_form(self, contacts):
       wd = self.app.wd
       self.change_name_value("firstname", contacts.name)
       self.change_name_value("middlename", contacts.middleN)
       self.change_name_value("lastname", contacts.lastN)
       self.change_name_value("nickN", contacts.nickN)
       self.change_name_value("title", contacts.title)
       self.change_name_value("company", contacts.company)
       self.change_name_value("address", contacts.address)
       self.change_name_value("home", contacts.home)
       self.change_name_value("mobile", contacts.mobile)
       self.change_name_value("work", contacts.work)
       self.change_name_value("fax", contacts.fax)
       self.change_name_value("email", contacts.email1)
       self.change_name_value("email2", contacts.email2)
       self.change_name_value("email3", contacts.email3)
       self.change_name_value("homepage", contacts.HP)
       self.change_name_value("address2", contacts.address2)
       self.change_name_value("phone2", contacts.phone2)
       self.change_name_value("notes", contacts.notes)
       self.contact_cache = None


   def into_group(self, index_cont, index_gr):
        wd = self.app.wd
        self.select_contact_by_index(index_cont)
        wd.find_element_by_name("to_group").click()
        if not wd.find_element_by_xpath("//div[@class='right']/select//option[" + str(index_gr) + "]").is_selected():
            wd.find_element_by_xpath("//div[@class='right']/select//option[" + str(index_gr) + "]").click()
        wd.find_element_by_name("add").click()

