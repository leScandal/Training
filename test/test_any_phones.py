#2й тест падает при наличии пустых значений
import re
from random import randrange


def test_phones_on_HP(app):
    list_cont = app.contact.get_cont_list()
    any = randrange(len(list_cont))
    any_cont_from_HP = app.contact.get_cont_list()[any]
    any_cont_from_edit_page = app.contact.get_cont_info_from_edit_page(any)
    print(any_cont_from_edit_page)
    print (any)
    print(any_cont_from_HP)
    assert any_cont_from_HP.all_phones_from_HP == merge_phones_like_HP(any_cont_from_edit_page)


def clear(string):
    return re.sub("[() -]", "", string)


def merge_phones_like_HP(contact):
    return "\n".join(filter (lambda y: y != "",
                             map(lambda x: clear(x),
                                 filter(lambda z:  z is not None,
                                        [contact.home, contact.mobile, contact.work, contact.phone2]))))


def test_phones_on_view_page(app):
    any_cont_from_view_page = app.contact.get_cont_from_view_page(any)
    any_cont_from_edit_page = app.contact.get_cont_info_from_edit_page(any)
    print(any_cont_from_edit_page)
    print (any+' fix2')
    print(any_cont_from_view_page)
    assert any_cont_from_view_page.home == any_cont_from_edit_page.home
    assert any_cont_from_view_page.mobile == any_cont_from_edit_page.mobile
    assert any_cont_from_view_page.work == any_cont_from_edit_page.work
    assert any_cont_from_view_page.phone2 == any_cont_from_edit_page.phone2