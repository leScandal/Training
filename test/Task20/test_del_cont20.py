from model.contacts import Contacts
import random
from random import randrange

def test_del_Cont(app, db, check_ui):
    if len (db.get_cont_list()) == 0:
        app.contact.add(Contacts(lastN = "for del"))
    old_cont = db.get_cont_list()
    contact = random.choice(old_cont)
    #index = randrange (len(old_cont))
    print(list(old_cont))
    app.contact.del_Cont_by_id(contact.id)
    new_cont = db.get_cont_list()
    assert len(old_cont) - 1 == len(new_cont)
    old_cont.remove(contact)
    assert old_cont == new_cont
    if check_ui:
        assert sorted(new_cont, key=Contacts.id_or_max) == sorted(app.contact.get_cont_list(), key=Contacts.id_or_max)


