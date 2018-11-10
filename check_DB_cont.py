from fixture.db import DbFixture

db = DbFixture (host="127.0.0.1", database = "addressbook", user = "root", password = "")
#connection = mysql.connector.connect(host="127.0.0.1", database = "addressbook", user = "root", password = "")

try:
    contacts = db.get_cont_list()
    for contact in contacts:
        print(contact)
    print(len(contacts))
finally:
    db.stop()




