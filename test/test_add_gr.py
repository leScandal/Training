from model.group import Group
#from data.add_const_gr import constant as testdata
#from generator.group import testdata (Task18)


#@pytest.mark.parametrize("data", testdata, ids=[repr(x) for x in testdata])
def test_Add_Group(app, json_groups):
        group = json_groups
        old_groups = app.group.get_group_list()
        app.group.Create(group)
        assert len(old_groups) + 1 == app.group.count()
        new_groups = app.group.get_group_list()
        old_groups.append(group)
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


#1