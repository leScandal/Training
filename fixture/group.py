class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_GP(self):
        wd=self.app.wd
        wd.find_element_by_link_text("groups").click()

    def Create(self, Group):
        wd = self.app.wd
        self.open_GP()
        wd.find_element_by_name("new").click()
        self.fill_group_form(Group)
        wd.find_element_by_name("submit").click()
        self.return_to_GP()


    def change_name_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)


    def fill_group_form(self, Group):
        wd = self.app.wd
        self.change_name_value("group_name", Group.name)
        self.change_name_value("group_header", Group.header)
        self.change_name_value("group_footer", Group.footer)


    def delete_first_group(self):
        wd = self.app.wd
        self.open_GP()
        self.select_first_group(wd)
        wd.find_element_by_name("delete").click()
        self.return_to_GP()

    def modify_first(self, new_group_data):
        wd = self.app.wd
        self.open_GP()
        self.select_first_group(wd)
        wd.find_element_by_name("edit").click()
        self.fill_group_form(new_group_data)
        wd.find_element_by_name("update").click()
        self.return_to_GP()

    def select_first_group(self, wd):
        wd.find_element_by_name("selected[]").click()

    def return_to_GP(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()
        if not wd.find_element_by_name("selected[]").is_selected():
            self.select_first_group(wd)
