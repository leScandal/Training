from model.Contacts import Contacts
from random import randrange

def test_del_Cont(app):
    if app.contact.count() == 0:
        app.contact.add(Contacts(lastN = "for del"))
    old_cont = app.contact.get_con_list()
    index = randrange (len(old_cont))
    print(list(old_cont))
    app.contact.del_Cont_by_index(index)
    assert len(old_cont) - 1 == app.contact.count()
    new_cont = app.contact.get_con_list()
    old_cont[ index : index + 1] = []
    assert old_cont == new_cont


