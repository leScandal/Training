#2й тест падает при наличии пустых значений
# Задание 14  проверкa для всех полей контакта на главной странице
import re
from random import randrange


def test_any_contact_on_HP(app):
    list_cont = app.contact.get_cont_list()
    any = randrange(len(list_cont))
    any_cont_from_HP = app.contact.get_cont_list()[any]
    any_cont_from_edit_page = app.contact.get_cont_info_from_edit_page(any)
    print(any_cont_from_edit_page)
    print (any)
    print(any_cont_from_HP)
    assert any_cont_from_HP.all_phones_from_HP == merge_phones_like_HP(any_cont_from_edit_page)
    assert any_cont_from_HP.all_mails_from_HP == merge_mails_like_HP(any_cont_from_edit_page)
    assert any_cont_from_HP.name == any_cont_from_edit_page.name
    assert any_cont_from_HP.lastN == any_cont_from_edit_page.lastN
    assert any_cont_from_HP.address == any_cont_from_edit_page.address


def clear(string):
    return re.sub("[() -]", "", string)


def merge_phones_like_HP(contact):
    return "\n".join(filter (lambda y: y != "",
                             map(lambda x: clear(x),
                                 filter(lambda z:  z is not None,
                                        [contact.home, contact.mobile, contact.work, contact.phone2]))))

def merge_mails_like_HP(contact):
    return "\n".join(filter (lambda y: y != "",
                             map(lambda x: clear(x),
                                 filter(lambda z:  z is not None,
                                        [contact.email1, contact.email2, contact.email3]))))

