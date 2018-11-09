from model.contacts import Contacts
import random


def test_edit_cont_name(app, db, check_ui):
    if len (db.get_cont_list()) == 0:
        app.contact.add(Contacts(lastN = "for del"))
    old_cont = db.get_cont_list()
    contact_edit = random.choice(old_cont) #случайный выбор контакта
    changed = Contacts(name='Task20', lastN='N_Task20', address='Ad_Task20') #изменяемые данные
    changed.id = contact_edit.id #его id
    app.contact.edit_contact_by_id(changed.id, changed)
    new_cont = db.get_cont_list()
    assert len(old_cont) == len (new_cont)
    old_cont.remove(contact_edit)
    old_cont.append(Contacts(name='Task20', lastN='N_Task20', address='Ad_Task20'))
    assert sorted(old_cont, key=Contacts.id_or_max) == sorted(new_cont, key=Contacts.id_or_max)
    if check_ui:
        assert sorted(new_cont, key=Contacts.id_or_max) == sorted(app.contact.get_cont_list(), key=Contacts.id_or_max)



