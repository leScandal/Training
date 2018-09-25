from model.Contacts import Contacts

def test_del_Cont(app):
    if app.contact.count() == 0:
        app.contact.add(Contacts(lastN = "for del"))
    old_cont = app.contact.get_con_list()
    print(list(old_cont))
    app.contact.del_Cont()
    new_cont = app.contact.get_con_list()
    assert len(old_cont) - 1 == len(new_cont)
    old_cont[0:1] = []
    assert old_cont == new_cont


