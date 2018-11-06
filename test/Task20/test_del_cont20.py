from model.contacts import Contacts
import random
from random import randrange

def test_del_Cont(app, db):
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


