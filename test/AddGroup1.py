# -*- coding: utf-8 -*-
from model.Group import Group


def test_AddGroup1(app):
    app.group.Create(Group("груп", "Cослуж", "Коллег"))
    app.session.logout()


def test_EmptyGroup(app):
    app.group.Create(Group("23", "12", "83"))
