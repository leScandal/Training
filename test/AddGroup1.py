# -*- coding: utf-8 -*-
from test.model.Group import Group


def test_AddGroup1(app):
    app.session.login(username="admin", password="secret")
    app.group.Create(Group("группа 3", "Cослуживцы4", "Коллеги3"))
    app.session.logout()


def test_EmptyGroup(app):
    app.session.login(username="admin", password="secret")
    app.group.Create(Group("", "", ""))
    app.session.logout()