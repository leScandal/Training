from model.contacts import Contacts

def test_check_cont_lists (app, db):
    ui_list = app.contact.get_contact_list()
    def clean(contact):
        return Contacts(id = contact.id, name = contact.firstname.strip())
    db_list = map(clean, db.get_contact_list())
    assert sorted(ui_list, key = Contacts.id_or_max) == sorted(db_list, key = Contacts.id_or_max)


