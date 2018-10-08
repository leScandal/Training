from model.Contacts import Contacts
from random import randrange


def test_edit_cont_name(app):
    if app.contact.count() == 0:
        app.contact.add(Contacts(lastN = "for del"))
    old_cont = app.contact.get_cont_list()
    index = randrange(len(old_cont))
    changed = Contacts(lastN='123а')
    changed.id = old_cont[index].id
    # added = Contacts("Святополк", "Владимирович", "Рюрик", "Окаянный", "Князь киевский", "Киевская Русь", "Киев кремль",
    #          "Кремль", "(123) 456-78-90", "Князь Тартурский", "(123) 456-78-90", "kiev@gmail.ua1", "kremlin@gmail.ua",
    #          "", "https://ru.wikipedia.org/wiki/Cвятополк Владимирович Окаянный", "", "", "был под арестом")
    app.contact.edit_contact_by_index(index, changed)
    new_cont = app.contact.get_cont_list()
    assert len(old_cont) == app.contact.count()
    old_cont[index] = changed
    assert sorted(old_cont, key=Contacts.id_or_max) == sorted(new_cont, key=Contacts.id_or_max)

