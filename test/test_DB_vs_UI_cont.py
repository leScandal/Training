from model.contacts import Contacts

def test_check_cont_lists (app, db):
    ui_list = app.contact.get_cont_list()
    print("ui_list:")
    print(ui_list)
    def clean(contact):
        return Contacts(id = contact.id, lastN = contact.lastN.strip(), name = contact.name.strip(), address = contact.address.strip())
    db_list = list(map(clean, db.get_cont_list()))
    print("db_list:")
    print(db_list)
    assert sorted(ui_list, key = Contacts.id_or_max) == sorted(db_list, key = Contacts.id_or_max)


