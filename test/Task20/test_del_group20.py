from model.group import Group
import random
import pytest

def test_Del_some_Group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.Create(Group(name="for del"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    #index = randrange (len(old_groups))
    app.group.delete_group_by_id(group.id)
    app.group.count()
    new_groups = db.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    old_groups.remove(group)
    assert old_groups == new_groups
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)



