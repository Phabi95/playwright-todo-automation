class Todopage:

    def __init__(self,page):
        self.page=page
        self.input_placeholder=page.get_by_placeholder("What needs to be done?")
        self.todo_list=page.locator(" li")
    
    def navigate(self):
        self.page.goto("https://todomvc.com/examples/react/dist/")

    def add_item(self,text):
        self.input_placeholder.fill(text)
        self.input_placeholder.press("Enter")

    def get_list_item(self,text):
        return self.todo_list.filter(has_text=text)
    
    def complete_item(self,text):
        item=self.page.locator("li",has_text=text)
        item.get_by_role("checkbox").check()





