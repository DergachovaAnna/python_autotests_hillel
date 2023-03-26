import pytest
from lesson_17.Human.human import Human


@pytest.fixture
def create_human_with_valid_age():
    return Human("Alice", 16, 'female')


@pytest.fixture
def create_human_with_invalid_age():
    return Human("Alice", 100, 'female')


@pytest.fixture(params=[('Ann', 1, "female"), ('Bob', 99, "male")])
def human_data(request):
    return request.param


@pytest.fixture(params=[('Ann', 1, "female"), ('Bob', 98, "male")])
def human_age_boundary_values(request):
    return request.param
