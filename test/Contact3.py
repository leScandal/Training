# -*- coding: utf-8 -*-
from test.model.Contacts import Contacts


def test_Contact3(app):
    app.session.login(username="admin", password="secret")
    app.contact.add(Contacts("Святополк", "Владимирович", "Рюрик", "Окаянный", "Князь киевский", "Киевская Русь", "Киев кремль", "Кремль", "(123) 456-78-90", "Князь Тартурский", "(123) 456-78-90", "kiev@gmail.ua1", "kremlin@gmail.ua", "", "https://ru.wikipedia.org/wiki/вятополк Владимирович Окаянный", "", "", "был под арестом"))
    app.session.logout()

