from fixture.orm import ORMFixture
from model.contacts import Contacts
from model.group import Group
from random import randrange


def test_cont_in_gr(app, db, orm):
    if len (db.get_cont_list()) == 0:
        app.contact.add(Contacts(lastN = "for adding"))
    if len(db.get_group_list()) == 0:
        app.group.Create(Group(name="for adding"))
    list_cont = db.get_cont_list()
    list_groups = orm.get_group_list()
    any_cont = randrange(len(list_cont))
    any_gr = randrange(len(list_groups))
    app.contact.into_group(any_cont, any_gr) #контакт в группу)
    print(list_groups[any_gr])
    print(list_groups[any_gr].id)
    print(any_gr)
    print(list_cont[any_cont])
    print(list_cont[any_cont].id)
    app.group.view_group_id(list_groups[any_gr].id)
    ui_list_gr = app.contact.get_cont_list1()
    print("123")
    print(sorted(ui_list_gr, key = Contacts.id_or_max))
    db_list_gr = orm.get_cont_in_gr(Group(id=list_groups[any_gr].id))
    print(sorted(db_list_gr, key = Contacts.id_or_max))
    assert sorted(ui_list_gr, key = Contacts.id_or_max) == sorted(db_list_gr, key = Contacts.id_or_max)

