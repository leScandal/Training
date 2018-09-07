# -*- coding: utf-8 -*-
from model.Group import Group


def test_modify_name_group(app):
    app.group.Modify_first(Group(name="123844"))



def test_modify_header_group(app):
    app.group.Modify_first(Group(header="333"))
