# -*- coding: utf-8 -*-
from model.group import Group
import random


def test_modify_name_group(app, db):
    if len(db.get_group_list()) == 0:
        app.group.Create(Group(name="for mod"))
    old_groups = db.get_group_list()
    group_data = random.choice(old_groups) # случайный выбор группы
    id = group_data.id
    data_edit = Group(name="Task20")
    app.group.Modify_group_by_id(id, data_edit)
    new_groups = db.get_group_list()
    assert len(old_groups)  == len (new_groups)
    old_groups.remove(data_edit)
    old_groups.append(Group(id = id, name="Task20"))
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

