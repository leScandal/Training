from model.group import Group
from random import randrange
import pytest

def test_Del_some_Group(app):
    if app.group.count() == 0:
        app.group.Create(Group(name="for del"))
    old_groups = app.group.get_group_list()
    index = randrange (len(old_groups))
    app.group.delete_group_by_index(index)
    assert len(old_groups) - 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index:index + 1] = []
    assert old_groups == new_groups



