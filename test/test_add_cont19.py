#Для задания 19
from model.contacts import Contacts

def test_Add_Contact(app, json_contacts):
    data = json_contacts
    old_cont = app.contact.get_cont_list()
    app.contact.add(data)
    assert len(old_cont) + 1 == app.contact.count()
    new_cont = app.contact.get_cont_list()
    old_cont.append(data)
    assert sorted(old_cont, key=Contacts.id_or_max) == sorted(new_cont, key=Contacts.id_or_max)


#w