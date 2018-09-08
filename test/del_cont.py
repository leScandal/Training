from model.Contacts import Contacts

def test_del_Cont(app):
    if app.contact.count() == 0:
        app.contact.add(Contacts("for del", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""))
    app.contact.del_Cont()


