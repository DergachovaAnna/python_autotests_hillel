import pytest
from lesson_17.Human.human import Human


@pytest.mark.parametrize("name,age,gender", [('Ann', 1, "female"), ('Bob', 99, "male")])
@pytest.mark.positive
def test_create_human(name, age, gender):
    human = Human(name, age, gender)
    assert hasattr(human, '_Human__status')
    assert hasattr(human, '_Human__age_limit')


@pytest.mark.positive
def test_change_gender(create_human_positive):
    # Change to a different gender
    new_gender = "male" if create_human_positive.gender == "female" else "female"
    create_human_positive.change_gender(new_gender)
    assert create_human_positive.gender == new_gender


@pytest.mark.negative
def test_change_to_existed_gender(create_human_positive):
    # Try to change to the same gender
    new_gender = "male" if create_human_positive.gender == "male" else "female"
    with pytest.raises(Exception):
        create_human_positive.change_gender(new_gender)


@pytest.mark.positive
def test_grow_human_below_limit(create_human_positive):
    for number in range(create_human_positive.age, 99):
        initial_age = create_human_positive.age
        create_human_positive.grow()
        assert create_human_positive.age == initial_age + 1
        assert create_human_positive._Human__status == "alive"  # below age limit


@pytest.mark.negative
def test_grow_human_above_limit(create_human_negative):
    assert create_human_negative.age == 100
    create_human_negative.grow()  # above age limit
    assert create_human_negative._Human__status == "dead"


@pytest.mark.negative
def test_grow_human_equal_to_limit():
    human = Human('Test', 99, 'male')
    human.grow()
    assert human.age == 100
    assert human._Human__status == "dead"  # age is same as age limit


@pytest.mark.negative
def test_grow_human_age_below_zero():
    human = Human('Test', -1, 'male')
    with pytest.raises(Exception):
        human.grow()


@pytest.mark.positive
def test_human_is_alive(create_human_positive):
    assert create_human_positive._Human__is_alive() is True


@pytest.mark.negative
def test_create_human_invalid_age(create_human_negative):
    # Check that age affects whether human is created, alive or not
    assert create_human_negative._Human__status is 'dead'


@pytest.mark.parametrize("name,age,gender", [('Ann', 0, "female"), ('Bob', -1, "male")])
@pytest.mark.negative
def test_create_human_invalid_age_value(name, age, gender):
    with pytest.raises(Exception):
        Human(name, age, gender)


@pytest.mark.parametrize("name,age,gender", [(123, 25, "female"), ('Bob', "13", "male")])
@pytest.mark.negative
def test_create_human_invalid_attribute_type(name, age, gender):
    with pytest.raises(TypeError):
        Human(name, age, gender)


@pytest.mark.parametrize('gender', [12, 'MALE', 'transgender'])
@pytest.mark.negative
def test_change_gender_invalid_attributes(gender):
    with pytest.raises(Exception) as info_message:
        human = Human("Io", 20, "male")
        human.change_gender(gender)
    assert str(info_message.value) == "Not correct name of gender"


@pytest.mark.negative
def test_dead_human_change_gender():
    with pytest.raises(Exception):
        human = Human('Test', 99, "female")
        human.grow()
        human.change_gender('male')
