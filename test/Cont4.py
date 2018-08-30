# -*- coding: utf-8 -*-
from model.Contacts import Contacts


def test_Cont4(app):
    app.session.login(username="admin", password="secret")
    app.contact.add(Contacts("Свят2", "Влад-ч1", "Рюрик3", "Окаянный4", "Князь 5", "Киевская6", "Кремль7", "К8", "(231) 456-78-90", "Князь Т", "(213) 456-78-90", "kiev1@gmail.ua1", "kremlin1@gmail.ua", "", "https://ru.wikipedia.org/wiki/вятополк Владимирович Окаянный", "", "", "был под арестом,бежал"))
    app.session.logout()
    #E
