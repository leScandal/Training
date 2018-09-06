# -*- coding: utf-8 -*-
from model.Contacts import Contacts


def test_Cont4(app):
    app.session.login(username="admin", password="secret")
    app.contact.add(Contacts("Святополк1", "Владимирович3", "Окаянный2", "Рюрик5", "Князь", "Киевскаякая Русь" , "Кремль", "К", "(231) 456-78-90", "Князь =", "(213) 456-78-90", "kiev@gmail.ua", "kremlin@gmail.ua", "", "https://ru.wikipedia.org/wiki/Святополк Владимирович Окаянный", "", "", "был под арестом,бежал"))
    app.session.logout()
    #E
