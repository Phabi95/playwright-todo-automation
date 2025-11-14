from pages.to_do_page import Todopage
from playwright.sync_api import expect

def test_add_two_items_and_complete_one(to_do_page:Todopage):
    # 1. Add the first item
    to_do_page.add_item("Task 1")
    
    # 2. Add the second item
    to_do_page.add_item("Task 2")
    
    # 3. Complete "Task 1"
    to_do_page.complete_item("Task 1")
    # 4. VERIFY: Check that "Task 1" is completed
    task_1_item = to_do_page.get_list_item("Task 1")
    expect(task_1_item).to_have_class("completed")

    task_2_item=to_do_page.get_list_item("Task 2")
    expect(task_2_item).not_to_have_class("completed")