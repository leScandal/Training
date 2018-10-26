from model.contacts import Contacts
from generator.contacts import testdata
import pytest


@pytest.mark.parametrize("data", testdata, ids=[repr(x) for x in testdata])
def test_Add_Contact(app, data):
    old_cont = app.contact.get_cont_list()
    app.contact.add(data)
    assert len(old_cont) + 1 == app.contact.count()
    new_cont = app.contact.get_cont_list()
    old_cont.append(data)
    assert sorted(old_cont, key=Contacts.id_or_max) == sorted(new_cont, key=Contacts.id_or_max)
