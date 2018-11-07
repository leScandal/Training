from model.group import Group
#from data.add_const_gr import constant as testdata
#from generator.group import testdata (Task18)


#@pytest.mark.parametrize("data", testdata, ids=[repr(x) for x in testdata])
def test_Add_Group(app, db, json_groups, check_ui):
        group = json_groups
        old_groups = db.get_group_list()
        app.group.Create(group)
        new_groups = db.get_group_list()
        assert len(old_groups) + 1 == len(new_groups)
        old_groups.append(group)
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
        if check_ui:
                assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


#1