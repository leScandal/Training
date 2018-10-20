from model.group import Group
import pytest
import random
import string

def random_string (prefix, maxilen):
    symbols = string.ascii_letters+string.digits + string.punctuation + ""*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxilen))])


testdata = [Group(name="", header="", footer="")]  + [
    Group(name= name, header=header, footer=footer)
    for name in ["", random_string("name", 10)]
    for header in ["", random_string("header", 20)]
    for footer in ["", random_string("footer", 20)]
]

@pytest.mark.parametrize("data", testdata, ids=[repr(x) for x in testdata])
def test_Add_Group(app, data):
        old_groups = app.group.get_group_list()
        app.group.Create(data)
        assert len(old_groups) + 1 == app.group.count()
        new_groups = app.group.get_group_list()
        old_groups.append(data)
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


