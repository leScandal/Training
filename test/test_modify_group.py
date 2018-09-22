# -*- coding: utf-8 -*-
from model.Group import Group


def test_modify_name_group(app):
    old_groups = app.group.get_group_list()
    if app.group.count() == 0:
        app.group.Create(Group(name="for mod"))
    app.group.Modify_first(Group(name="14677844"))
    new_groups = app.group.get_group_list()
    assert len(old_groups)  == len(new_groups)



def test_modify_header_group(app):
    old_groups = app.group.get_group_list()
    app.group.Modify_first(Group(header="223"))
    new_groups = app.group.get_group_list()
    assert len(old_groups)  == len(new_groups)




##