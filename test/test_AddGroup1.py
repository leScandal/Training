# -*- coding: utf-8 -*-
from model.Group import Group


def test_AddGroup1(app):
    old_groups = app.group.get_group_list()
    added = Group("груп7", "Cослуж22", "Коллег12")
    app.group.Create(added)
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(added)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
#
# def test_AddGroup2(app):
#     app.group.Create(Group("12", "2Cж", "2ег"))


def test_EmptyGroup(app):
    old_groups = app.group.get_group_list()
    added = Group("", "", "")
    app.group.Create(added)
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
    old_groups.append(added)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
