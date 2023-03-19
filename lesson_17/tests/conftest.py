import pytest
from lesson_17.Human.human import Human


@pytest.fixture
def create_human_positive():
    return Human("Alice", 16, 'female')


@pytest.fixture
def create_human_negative():
    return Human("Alice", 100, 'female')
