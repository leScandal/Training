# -*- coding: utf-8 -*-
import pytest
from Contacts import Contacts
from Application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalazire(fixture.stop)
    return fixture


def test_Contact3(app):
    app.open_HP()
    app.login(username="admin", password="secret")
    app.open_cont_page()
    app.add_cont(Contacts("Святополк", "Владимирович", "Рюрик", "Окаянный", "Князь киевский", "Киевская Русь", "Киев кремль", "Кремль", "(123) 456-78-90", "Князь Тартурский", "(123) 456-78-90", "kiev@gmail.ua1", "kremlin@gmail.ua", "", "https://ru.wikipedia.org/wiki/вятополк Владимирович Окаянный", "", "", "был под арестом"))
    app.logout()

