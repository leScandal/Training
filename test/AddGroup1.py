# -*- coding: utf-8 -*-
from model.Group import Group


def test_AddGroup1(app):
    app.group.Create(Group("группа 56", "Cослуживцы17", "Коллеги33"))


def test_EmptyGroup(app):
    app.group.Create(Group("1", "2", "3"))
