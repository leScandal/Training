# -*- coding: utf-8 -*-
from model.Group import Group


def test_modify_name_group(app):
    app.session.login(username="admin", password="secret")
    app.group.Modify_first(Group(name="New group1", header="New header1",footer="New header1"))
    app.session.logout()


def test_modify_header_group(app):
    app.session.login(username="admin", password="secret")
    app.group.Modify_first(Group(header="header"))
    app.session.logout()