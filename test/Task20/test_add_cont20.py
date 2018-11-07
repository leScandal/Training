#Для задания 20
from model.contacts import Contacts

def test_Add_Contact(app, db, json_contacts, check_ui):
    data = json_contacts
    old_cont = db.get_cont_list()
    app.contact.add(data)
    new_cont = db.get_cont_list()
    assert len(old_cont) + 1 == len(new_cont)
    old_cont.append(data)
    assert sorted(old_cont, key=Contacts.id_or_max) == sorted(new_cont, key=Contacts.id_or_max)
    if check_ui:
        assert sorted(new_cont, key=Contacts.id_or_max) == sorted(app.contact.get_cont_list(), key=Contacts.id_or_max)




