class Beverage:
    def __init__(self):
        self.is_ready = False
    
    def prepare_recipe(self):
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        self.add_condiments()
        self.is_ready = True
    
    def boil_water(self):
        print("Кипятим воду")
    
    def pour_in_cup(self):
        print("Наливаем в кружку")
    
    def brew(self):
        raise NotImplementedError("Нужно переопределить метод brew")
    
    def add_condiments(self):
        raise NotImplementedError("Нужно переопределить метод add_condiments")

class Tea(Beverage):
    def brew(self):
        print("Завариваем чай")
    
    def add_condiments(self):
        print("Добавляем лимон")

class Coffee(Beverage):
    def brew(self):
        print("Завариваем кофе")
    
    def add_condiments(self):
        print("Добавляем сахар")

if __name__ == "__main__":
    tea = Tea()
    coffee = Coffee()
    
    print("=== Чай ===")
    tea.prepare_recipe()
    
    print("\n=== Кофе ===")
    coffee.prepare_recipe()
