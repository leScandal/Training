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
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(Group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(Group.header)
        wd.find_element_by_name("submit").click()
        self.return_to__GP()


    def delete_first_group(self):
        wd = self.app.wd
        self.open_GP()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_name("delete").click()
        self.return_to_GP()

    def return_to_GP(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()
        if not wd.find_element_by_name("selected[]").is_selected():
             wd.find_element_by_name("selected[]").click()
