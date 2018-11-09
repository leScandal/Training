from pony.orm import *
from datetime import datetime
from model.group import Group
from model.contacts import Contacts
from pymysql.converters import  decoders

class ORMFixture:
    db = Database()

    class ORMGroup(db.Entity):
        _table_ = "group_list"
        id = PrimaryKey(int, column = 'group_id')
        name = Optional (str, column = 'group_name')
        header = Optional(str, column='group_header')
        footer = Optional(str, column='group_footer')



    class ORMContacts(db.Entity):
        _table_ = "addressbook"
        id = PrimaryKey(int, column = 'id')
        firstname = Optional (str, column = 'firstname')
        lastname = Optional(str, column='lastname')
        deprecated = Optional(datetime, column='deprecated')


    def __init__(self, host, database, user, password):
        self.db.bind('mysql', host=host, database=database, user=user, password=password, conv=decoders)
        self.db.generate_mapping()
        sql_debug(True)

    def convert_groups_to_model(self, groups):
        def convert(group):
            return Group (id = str (group.id), name = group.name, header = group.header, footer = group.footer)
        return list(map(convert, groups))

    def convert_contacts_to_model(self, contacts):
        def convert(contact):
            return Contacts(id = str (contact.id), name = contact.firstname, lastN = contact.lastname) #, footer = contact.footer)
        return list(map(convert, contacts))

    # cursor.execute(
    #     "select id, firstname, middlename, lastname, company, title, address, home, mobile, work, fax, email, email2, email3, homepage, notes from addressbook where deprecated='0000-00-00 00:00:00'")


    @db_session
    def get_group_list(self):
        return self.convert_groups_to_model(select(g for g in ORMFixture.ORMGroup))

    @db_session
    def get_cont_list(self):
        return self.convert_contacts_to_model(select(c for c in ORMFixture.ORMContacts if c.deprecated is None))