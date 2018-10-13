from model.contacts import Contacts
from random import randrange


def test_edit_cont_name(app):
    if app.contact.count() == 0:
        app.contact.add(Contacts(lastN = "for del"))
    old_cont = app.contact.get_cont_list()
    index = randrange(len(old_cont))
    changed = Contacts(name='456', lastN='123', address='789')
    changed.id = old_cont[index].id
    # added = Contacts("Святополк", "Владимирович", "Рюрик", "Окаянный", "Князь киевский", "Киевская Русь", "Киев кремль",
    #          "Кремль", "(123) 456-78-90", "Князь Тартурский", "(123) 456-78-90", "kiev@gmail.ua1", "kremlin@gmail.ua",
    #          "", "https://ru.wikipedia.org/wiki/Cвятополк Владимирович Окаянный", "", "", "был под арестом")
    app.contact.edit_contact_by_index(index, changed)
    new_cont = app.contact.get_cont_list()
    assert len(old_cont) == app.contact.count()
    old_cont[index] = changed
    assert sorted(old_cont, key=Contacts.id_or_max) == sorted(new_cont, key=Contacts.id_or_max)


# def test_modify_firstname(app):
#     if app.contact.count_contacts() == 0:
#         app.contact.add_new_contact(Contacts(firstname="test"))
#     old_contacts = app.contact.get_contact_list()
#     index = randrange(len(old_contacts))
#     contact = Contacts(firstname="New contact")
#     contact.id = old_contacts[index].id
#     app.contact.modify_contact_by_index(index, contact)
#     new_contacts = app.contact.get_contact_list()
#     assert len(old_contacts) == app.contact.count_contacts()
#     old_contacts[index] = contact
#     assert sorted(old_contacts, key=Contacts.id_or_max) == sorted(new_contacts, key=Contacts.id_or_max)
