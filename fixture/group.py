class GroupHelper:

    def __init__(self, app):
        self.app = app

    def Create(self, Group):
        wd = self.wd
        wd.find_element_by_link_text("groups").click()
        wd.find_element_by_name("new").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(Group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(Group.header)
        wd.find_element_by_name("submit").click()
        wd.find_element_by_link_text("group page").click()
        if not wd.find_element_by_name("selected[]").is_selected():
             wd.find_element_by_name("selected[]").click()
