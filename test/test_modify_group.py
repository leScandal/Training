# -*- coding: utf-8 -*-
from model.Group import Group


def test_modify_name_group(app):
    app.session.login(username="admin", password="secret")
    app.group.Modify_first(Group(name="New group", header="New header",footer="New header")
    #app.session.logout()

#
# def test_modify_header_group(app):
#     app.session.login(username="admin", password="secret")
#     app.group.Modify_first(Group(None,header="New header",None))
#     app.session.logout()