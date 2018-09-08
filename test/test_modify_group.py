# -*- coding: utf-8 -*-
from model.Group import Group


def test_modify_name_group(app):
    if app.group.count() == 0:
        app.group.Create(Group(name="for del"))
    app.group.Modify_first(Group(name="123844"))
    app.session.logout()


def test_modify_header_group(app):
    app.group.Modify_first(Group(header="333"))
##