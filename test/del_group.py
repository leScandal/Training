from model.Group import Group

def test_Del1Group(app):
    # while not app.group.count()<2:
    if app.group.count() == 0:
        app.group.Create(Group(name="for del"))
    app.group.delete_first_group()



 #
 # def test_Del1Group(app):
 #      if app.group.count() == 0:
 #         app.group.create(Group(name = "for del"))
 #      app.group.delete_first_group()




