# -*- coding: utf-8 -*-
from model.Contacts import Contacts


def test_Contact3(app):
    app.contact.add(Contacts("Святополк", "Владимирович", "Рюрик", "Окаянный", "Князь киевский", "Киевская Русь", "Киев кремль", "Кремль", "(123) 456-78-90", "Князь Тартурский", "(123) 456-78-90", "kiev@gmail.ua1", "kremlin@gmail.ua", "", "https://ru.wikipedia.org/wiki/вятополк Владимирович Окаянный", "", "", "был под арестом"))
    app.contact.add(Contacts("Fолк", "Владимирович", "Рюрик", "Окаянный", "Князь киевский", "Киевская Русь", "Киев кремль",
                  "Кремль", "(123) 456-78-90", "Князь Тартурский", "(123) 456-78-90", "kiev@gmail.ua1",
                  "kremlin@gmail.ua", "", "https://ru.wikipedia.org/wiki/вятополк Владимирович Окаянный", "", "",
                  "был под арестом"))
    app.contact.add(Contacts())
    app.contact.add(Contacts(name = "Киря", lastN = "Владимирович", address3 = "Мск"))
