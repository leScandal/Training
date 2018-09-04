
def test_del_Cont(app):
    app.session.login(username="admin", password="secret")
    app.contact.del_Cont()
    app.session.logout()

