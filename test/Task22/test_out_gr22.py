from fixture.orm import ORMFixture
from model.contacts import Contacts
from model.group import Group
from random import randrange


def test_cont_out_gr(app, db, orm):
    if len (db.get_cont_list()) == 0:
        app.contact.add(Contacts(lastN = "for adding"))
    if len(db.get_group_list()) == 0:
        app.group.Create(Group(name="for adding"))
    list_groups = orm.get_group_list()
    any_gr = randrange(len(list_groups))
    idx = list_groups[any_gr].id
    app.group.view_group_id(list_groups[any_gr].id) # вход в случайно выбранную группу
    db_list_gr = orm.get_cont_in_gr(Group(id=idx)) #list_groups[any_gr].id)) #спсиок контактов в гр до
    if len(db_list_gr) == 0:
        print("empty group")
        print (idx)
        list_cont = db.get_cont_list()
        any_cont = randrange(len(list_cont))
        app.group.full_group_list()
        app.contact.into_group(any_cont, any_gr) #контакт в группу)
        app.contact.return_to_HP()
    ui_cont_gr2 = app.contact.get_cont_list1() #  список контактов в гр чз ПИ после добавления , если пустая
    print(ui_cont_gr2[0])
    print(ui_cont_gr2[0].id)
    print("id контактa в группе")
    print("group")
    print("list cont  in gr after adding:")
    print(ui_cont_gr2)
    app.contact.out_group(ui_cont_gr2[0].id, idx) # del 1й контaкт
    app.contact.return_to_HP()
    db_list_gr = orm.get_cont_in_gr(Group(id=list_groups[any_gr].id))
    print(db_list_gr)
    assert Contacts(id=ui_cont_gr2[0].id) not in db_list_gr, "Error"


#
# def test_cont_out_gr114(app, db, orm):
#     app.group.view_group_id(114) # вход в  группу 114 34cd
#     ui_cont_gr = app.contact.get_cont_list1() #список контактов в гр чз ПИ
#     app.contact.out_group(ui_cont_gr[0].id, 114) # del 1й контaкт
#     app.contact.return_to_HP()
#     app.group.view_group_id(114) # вход в случайно выбранную группу
#     db_list_gr = orm.get_cont_in_gr(Group(id=114)) #новый список конт чз орм
#     assert Contacts(id=ui_cont_gr[0].id) not in db_list_gr, "Error"
#
