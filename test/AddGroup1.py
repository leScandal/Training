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
    app.session.login(username="admin", password="secret")
    app.group.Create(Group("группа 5", "Знакомые6"))
    app.session.logout()
