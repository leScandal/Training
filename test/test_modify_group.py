# -*- coding: utf-8 -*-
from model.Group import Group


def test_modify_name_group(app):
    old_groups = app.group.get_group_list()
    changed = Group(name="14844")
    changed.id = old_groups[0].id
    if app.group.count() == 0:
        app.group.Create(Group(name="for mod"))
    app.group.Modify_first(changed)
    assert len(old_groups)  == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[0] = changed
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)



def test_modify_header_group(app):
    old_groups = app.group.get_group_list()
    app.group.Modify_first(Group(header="223"))
    new_groups = app.group.get_group_list()
    assert len(old_groups)  == len(new_groups)




##