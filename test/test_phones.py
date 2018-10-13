from model.contacts import Contacts
from random import randrange

def test_phones_on_HP(app):
    first_cont_from_HP = app.contact.get_cont_list()[0]
    first_cont_from_edit_page = app.contact.get_cont_info_from_edit_page(0)
    print(first_cont_from_edit_page)
    print ('123')
    print(first_cont_from_HP)
    #assert first_cont_from_HP.home == first_cont_from_edit_page.home
    #assert first_cont_from_HP.mobile == first_cont_from_edit_page.mobile
    #assert first_cont_from_HP.work == first_cont_from_edit_page.work
    #assert first_cont_from_HP.fax == first_cont_from_edit_page.fax
    #assert first_cont_from_HP.phone2 == first_cont_from_edit_page.phone2