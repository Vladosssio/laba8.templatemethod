
from main import Tea, Coffee

def test_tea_preparation():
    tea = Tea()
    assert tea.is_ready == False
    tea.prepare_recipe()
    assert tea.is_ready == True

def test_coffee_preparation():
    coffee = Coffee()
    assert coffee.is_ready == False
    coffee.prepare_recipe()
    assert coffee.is_ready == True
