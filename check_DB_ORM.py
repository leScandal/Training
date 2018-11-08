import mysql.connector
from fixture.orm import ORMFixture

db = ORMFixture(host="127.0.0.1", database = "addressbook", user = "root", password = "")
#connection = mysql.connector.connect(host="127.0.0.1", database = "addressbook", user = "root", password = "")

try:
    l = db.get_group_list()
    for item in l:
        print(item)
    print(len(l))
finally:
    pass #db.stop() ОСТАНОВИЛАСЬ 13м18сек 7_7!!!!