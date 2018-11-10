from fixture.orm import ORMFixture
from model.contacts import Contacts
from model.group import Group
from random import randrange
from fixture.db import DbFixture

db = ORMFixture(host="127.0.0.1", database = "addressbook", user = "root", password = "")

def test_cont_in_gr(app, db, check_ui):
    if len (db.get_cont_list()) == 0:
        app.contact.add(Contacts(lastN = "for adding"))
    if len(db.get_group_list()) == 0:
        app.group.Create(Group(name="for adding"))
    list_cont = db.get_cont_list()
    list_groups = db.get_group_list()
    any_cont = randrange(len(list_cont))
    any_gr = randrange(len(list_groups))
    app.contact.into_group(any_cont, any_gr) #контакт в группу)
    print(list_groups[any_gr])
    print(list_groups[any_gr].id)
    print(any_gr)
    print(list_cont[any_cont])
    print(list_cont[any_cont].id)
    app.group.view_group(list_groups[any_gr].id)
    ui_list_gr = app.contact.get_cont_list()
    db_list_gr = db.get_cont_in_gr(Group(id=any_gr))
    assert ui_list_gr == db_list_gr

