# -*- coding: utf-8 -*-
from model.Group import Group


def test_AddGroup1(app):
    app.session.login(username="admin", password="secret")
    app.group.Create(Group("группа 5", "Знакомые6"))
    app.session.logout()
