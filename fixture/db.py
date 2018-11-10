import pymysql
import mysql.connector
from model.group import Group
from model.contacts import Contacts
from fixture.orm import ORMFixture

class DbFixture:

    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        #self.connection = mysql.connector.connect(host="127.0.0.1", database = "addressbook", user = "root", password = "")
        #self.connection = mysql.connector.connect(host=host, database=database, user=user, password=password)
        self.connection = pymysql.connect(host="127.0.0.1", database="addressbook", user="root", password="")
        self.connection.autocommit = True

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


    def get_cont_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, middlename, lastname, company, title, address, home, mobile, work, email, email2, email3, phone2 from addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, middlename, lastname, company, title, address, home, mobile, work, email, email2, email3, phone2) = row
                list.append(Contacts (id = str (id), name = firstname, lastN = lastname, address = address, home=home, mobile=mobile, work=work, email1=email, email2=email2, email3=email3, phone2=phone2))
        finally:
            cursor.close()
        return list


    def stop(self):
        self.connection.close




