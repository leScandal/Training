# -*- coding: utf-8 -*-
from model.contacts import Contacts


def test_Contact3(app):
    old_cont = app.contact.get_cont_list()
    added = Contacts("Святополк4", "Владимирович4", "Рюрик4", "Окаянный4", "Князь киевский4", "Киевская Русь", "Киев кремль",
             "Кремль", "(123) 456-78-90", "Князь Тартурский", "(123) 456-78-90", "kiev@gmail.ua1", "kremlin@gmail.ua",
             "", "https://ru.wikipedia.org/wiki/Cвятополк Владимирович Окаянный", "", "", "был под арестом")
    app.contact.add(added)
    new_cont = app.contact.get_cont_list()
    assert len(old_cont) + 1 == app.contact.count()
    old_cont.append(added)
    #app.contact.add(Contacts()) #добавление пустого контакта
    assert sorted(old_cont, key=Contacts.id_or_max) == sorted(new_cont, key=Contacts.id_or_max)


def test_Contact4(app):
     old_cont = app.contact.get_cont_list()
     added = Contacts( name = "Nick90", lastN = "Sonick99")
     app.contact.add(added)
     assert len(old_cont) + 1 == app.contact.count()
     new_cont = app.contact.get_cont_list()
     old_cont.append(added)
     assert sorted(old_cont, key = Contacts.id_or_max) == sorted(new_cont, key = Contacts.id_or_max)

