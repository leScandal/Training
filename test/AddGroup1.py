# -*- coding: utf-8 -*-
import pytest
from model.Group import Group
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.stop)
    return fixture

    
def test_AddGroup1(app):
    app.Login(username="admin", password="secret")
    app.open_group_page()
    app.Create_group(Group("группа 5", "Знакомые6"))
    app.Return_to_PG()
    app.logout()
