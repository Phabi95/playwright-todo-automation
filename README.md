# Playwright TodoMVC Automation

This project demonstrates UI (User Interface) automation using `pytest` and `playwright`. It includes structured test cases for the [TodoMVC website](https://todomvc.com/examples/react/dist/), organized using the Page Object Model (POM) pattern.

## Project Goal

The goal of this project is to create a reliable and maintainable automation script for the TodoMVC application. It tests the core "CRUD" (Create, Read, Update, Delete) functionality of a to-do list, serving as a practical example of how to use `pytest` and `playwright` together.

## Technologies Used

* **Language:** Python
* **Libraries:** `pytest`, `playwright`, `pytest-playwright`
* **Tools:** Git, GitHub, VSCode

## Installation

Install the dependencies and start the automation.

1.  **Clone the repository:**
    *(Replace with your repository's URL)*
    ```bash
    git clone [https://github.com/YOUR_USERNAME/playwright-todo-automation.git](https://github.com/YOUR_USERNAME/playwright-todo-automation.git)
    cd playwright-todo-automation
    ```

2.  **Create a virtual environment:**
    ```bash
    python -m venv .venv
    source .venv/bin/activate
    ```
    *(On Windows, use: `.venv\Scripts\activate`)*

3.  **Install Python dependencies:**
    ```bash
    pip install pytest pytest-playwright
    ```

4.  **Install Playwright's browsers:**
    *(This is a required one-time setup for Playwright)*
    ```bash
    playwright install
    ```

## Running the Automation

This project includes automated scripts to test the TodoMVC website's functionality.

1.  **Run all automations (Headless):**
    This runs all tests in the background. This is the fastest method.
    ```bash
    pytest
    ```

2.  **Run and Watch (Headed Mode):**
    This opens a browser window so you can watch the automation run live.
    ```bash
    pytest --headed
    ```

3.  **Run a specific test:**
    To run only the "edit item" test, for example:
    ```bash
    pytest -k "edit_item" --headed
    ```

## Project Structure

* `tests/test_todo.py`: The main test file containing all automation tasks.
* `conftest.py`: Contains the `pytest` fixtures that set up the test environment.
* `pages/`: A directory for Page Object Model (POM) classes.
    * `todo_page.py`: A class that defines the locators and actions fo