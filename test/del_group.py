from model.Group import Group

def test_Del1Group(app):
    old_groups = app.group.get_group_list()
    if app.group.count() == 0:
        app.group.Create(Group(name="for del"))
    app.group.delete_first_group()
    new_groups = app.group.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    old_groups[0:1] = []
    assert old_groups == new_groups



