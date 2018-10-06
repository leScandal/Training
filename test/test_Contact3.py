# -*- coding: utf-8 -*-
from model.Contacts import Contacts


def test_Contact3(app):
    old_cont = app.contact.get_con_list()
    added = Contacts("Святополк", "Владимирович", "Рюрик", "Окаянный", "Князь киевский", "Киевская Русь", "Киев кремль",
             "Кремль", "(123) 456-78-90", "Князь Тартурский", "(123) 456-78-90", "kiev@gmail.ua1", "kremlin@gmail.ua",
             "", "https://ru.wikipedia.org/wiki/Cвятополк Владимирович Окаянный", "", "", "был под арестом")
    app.contact.add(added)
    new_cont = app.contact.get_con_list()
    assert len(old_cont) + 1 == len(new_cont)
    old_cont.append(added)
    assert old_cont == new_cont
    app.contact.add(Contacts())

def test_Contact4(app):
     old_cont = app.contact.get_con_list()
     added = Contacts( name = "Nick18", lastN = "Sonick71")
     app.contact.add(added)
     assert len(old_cont) + 1 == app.contact.count()
     new_cont = app.contact.get_con_list()
     old_cont.append(added)
     assert sorted(old_cont, key = Contacts.id_or_max) == sorted(new_cont, key = Contacts.id_or_max)

