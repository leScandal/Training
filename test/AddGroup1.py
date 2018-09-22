# -*- coding: utf-8 -*-
from model.Group import Group



def test_AddGroup1(app):
    old_groups = app.group.get_group_list()
    app.group.Create(Group("груп", "Cослуж", "Коллег"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)

# def test_AddGroup2(app):
#     app.group.Create(Group("11", "C1ж", "1ег"))


def test_EmptyGroup(app):
    old_groups = app.group.get_group_list()
    app.group.Create(Group("", "", ""))
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
