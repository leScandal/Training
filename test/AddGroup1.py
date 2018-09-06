# -*- coding: utf-8 -*-
from model.Group import Group


def test_AddGroup1(app):
    app.session.login(username="admin", password="secret")
    app.group.Create(Group("группа 1", "Cослуживцы1", "Коллеги3"))
    app.session.logout()


def test_EmptyGroup(app):
    app.session.login(username="admin", password="secret")
    app.group.Create(Group("1", "2", "3"))
    app.session.logout()