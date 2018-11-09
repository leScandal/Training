from model.contacts import Contacts
import re

def test_check_cont_lists (app, db):
    ui_list = app.contact.get_cont_list()
    print("ui_list:")
    print(ui_list)
    def clean(contact):
        return Contacts(id = contact.id, lastN = contact.lastN.strip(), name = contact.name.strip(), address = contact.address.strip(),
                        mobile = contact.mobile, email1=contact.email1, email2=contact.email2, email3=contact.email3,
                        home=contact.home, work=contact.work,phone2=contact.phone2)
    db_list = list(map(clean, db.get_cont_list()))
    print("db_list:")
    print(db_list)
    assert sorted(ui_list, key = Contacts.id_or_max) == sorted(db_list, key = Contacts.id_or_max)
    ui_mails_tels = []
    db_mails_tels = []
    for item_db in db_list:
        all_phones_HP = merge_phones_like_HP(item_db)
        all_mails_HP = merge_mails_like_HP(item_db)
        db_mails_tels.append(all_phones_HP and all_mails_HP)
    for item_ui in ui_list:
        ui_mails_tels.append(item_ui.all_phones_from_HP and item_ui.all_mails_from_HP)
    assert sorted(ui_mails_tels) == sorted(db_mails_tels)


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
