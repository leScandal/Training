import mysql.connector
from fixture.orm import ORMFixture
from model.group import Group

db = ORMFixture(host="127.0.0.1", database = "addressbook", user = "root", password = "")
#connection = mysql.connector.connect(host="127.0.0.1", database = "addressbook", user = "root", password = "")

try:
    l = db.get_group_list()
    for item in l:
        print(item)
    print(len(l))


    l1 = db.get_cont_in_gr(Group(id="114"))
    for item in l1:
        print(item)
    print(len(l1))
finally:
    pass #db.stop()