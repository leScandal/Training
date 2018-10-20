import re

# def test_phones_on_HP_old(app):
#     first_cont_from_HP = app.contact.get_cont_list()[0]
#     first_cont_from_edit_page = app.contact.get_cont_info_from_edit_page(0)
#     print(first_cont_from_edit_page)
#     print ('fix')
#     print(first_cont_from_HP)
#     assert first_cont_from_HP.home == clear(first_cont_from_edit_page.home)
#     assert first_cont_from_HP.mobile == clear(first_cont_from_edit_page.mobile)
#     assert first_cont_from_HP.work == clear(first_cont_from_edit_page.work)
#    # assert first_cont_from_HP.fax == clear(first_cont_from_edit_page.fax)
#     assert first_cont_from_HP.phone2 == clear(first_cont_from_edit_page.phone2)

#2й тест падает при наличии пустых значений

def test_phones_on_HP(app):
    first_cont_from_HP = app.contact.get_cont_list()[0]
    first_cont_from_edit_page = app.contact.get_cont_info_from_edit_page(0)
    print(first_cont_from_edit_page)
    print ('fix')
    print(first_cont_from_HP)
    assert first_cont_from_HP.all_phones_from_HP == merge_phones_like_HP(first_cont_from_edit_page)


def clear(string):
    return re.sub("[() -]", "", string)


def merge_phones_like_HP(contact):
    return "\n".join(filter (lambda y: y != "",
                             map(lambda x: clear(x),
                                 filter(lambda z:  z is not None,
                                        [contact.home, contact.mobile, contact.work, contact.phone2]))))



def test_phones_on_view_page(app):
    first_cont_from_view_page = app.contact.get_cont_from_view_page(0)
    first_cont_from_edit_page = app.contact.get_cont_info_from_edit_page(0)
    print(first_cont_from_edit_page)
    print ('fix2')
    print(first_cont_from_view_page)
    assert first_cont_from_view_page.home == first_cont_from_edit_page.home
    assert first_cont_from_view_page.mobile == first_cont_from_edit_page.mobile
    assert first_cont_from_view_page.work == first_cont_from_edit_page.work
    assert first_cont_from_view_page.phone2 == first_cont_from_edit_page.phone2