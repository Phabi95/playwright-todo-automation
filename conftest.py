from pages.to_do_page import Todopage
import pytest
from typing import Generator

@pytest.fixture
def to_do_page(page) -> Generator[Todopage, None, None]:

    todo=Todopage(page)

    todo.navigate()

    yield todo
    