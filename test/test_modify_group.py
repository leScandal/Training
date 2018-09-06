from model.Group import Group


def test_modify_name_group(app):
    app.session.login(username="admin", password="secret")
    app.group.Modify_first(Group(name="New group"))
    app.session.logout()


def test_modify_name_header(app):
    app.session.login(username="admin", password="secret")
    app.group.Modify_first(Group(header = "New header"))

    app.session.logout()

