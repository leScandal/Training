import pymysql
import mysql.connector
from model.group import Group
from model.contacts import Contacts


class DbFixture:

    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        #self.connection = mysql.connector.connect(host="127.0.0.1", database = "addressbook", user = "root", password = "")
        self.connection = pymysql.connect(host="127.0.0.1", database="addressbook", user="root", password="")

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header,footer) = row
                list.append(Group (id = str (id), name = name, header = header, footer=footer))
        finally:
            cursor.close()
        return list


    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, middlename, lastname, company, tittle, address, home, mobile, work, fax, email, email2, email3, homepage, notes from addressbook where 'deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, middlename, lastname, company, tittle, address, home, mobile, work, fax, email, email2, email3, homepage, notes) = row
                list.append(Contacts (id = str (id), name = firstname, lastN = lastname, work = work))
        finally:
            cursor.close()
        return list


    def stop(self):
        self.connection.close


    #
    #
    # def __init__(self, name=None, middleN=None, lastN=None, nickN=None, title=None, company=None, address=None, home=None,
    #              mobile=None, work=None, fax=None, email1=None, email2=None, email3=None, HP=None, address2=None, phone2=None,
    #              notes=None, id=None,  all_phones_from_HP=None, all_mails_from_HP=None):
    #     self.name = name
    #     self.middleN = middleN
    #     self.lastN = lastN
    #     self.nickN = nickN
    #     self.title = title
    #     self.company = company
    #     self.address = address
    #     self.home = home
    #     self.mobile = mobile
    #     self.work = work
    #     self.fax = fax
    #     self.email1 = email1
    #     self.email2 = email2
    #     self.email3 = email3
    #     self.HP = HP
    #     self.address2 = address2
    #     self.phone2 = phone2
    #     self.notes = notes
    #     self.id = id
    #     self.all_phones_from_HP =  all_phones_from_HP
    #     self.all_mails_from_HP = all_mails_from_HP