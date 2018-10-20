from model.contacts import Contacts
import pytest
import random
import string

def random_string (prefix, maxilen):
    symbols = string.ascii_letters+string.digits + string.punctuation + ""*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxilen))])


testdata = [Contacts(name = "", lastN="", address="", email1="")]  + [
    Contacts (name = random_string("name", 10), lastN = random_string("lastname", 10), address = random_string("address", 10), home = random_string("home phone", 10))
    for i in range (5)
]


@pytest.mark.parametrize("data", testdata, ids=[repr(x) for x in testdata])
def test_Add_Contact(app, data):
    old_cont = app.contact.get_cont_list()
    app.contact.add(data)
    assert len(old_cont) + 1 == app.contact.count()
    new_cont = app.contact.get_cont_list()
    old_cont.append(data)
    assert sorted(old_cont, key=Contacts.id_or_max) == sorted(new_cont, key=Contacts.id_or_max)
