# -*- coding: utf-8 -*-
from model.Group import Group
from random import randrange


def test_modify_name_group(app):
    if app.group.count() == 0:
        app.group.Create(Group(name="for mod"))
    old_groups = app.group.get_group_list()
    index = randrange (len(old_groups))
    changed = Group(name="1asd")
    changed.id = old_groups[index].id
    app.group.Modify_group_by_index(index, changed)
    assert len(old_groups)  == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index] = changed
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)



def test_modify_header_group(app):
    if app.group.count() == 0:
        app.group.Create(Group(name="for mod"))
    old_groups = app.group.get_group_list()
    app.group.Modify_first(Group(header="329"))
    new_groups = app.group.get_group_list()
    assert len(old_groups)  == len(new_groups)




##