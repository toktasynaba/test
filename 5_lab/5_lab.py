class Person:
    def __init__(self, full_name, driving_experience):
        self.full_name = full_name
        self.driving_experience = driving_experience

    def __str__(self):
        return f'Person: {self.full_name}, Driving Experience: {self.driving_experience} years'

class Engine:
    def __init__(self, power, manufacturer):
        self.power = power
        self.manufacturer = manufacturer

    def __str__(self):
        return f'Engine: Power - {self.power} HP, Manufacturer - {self.manufacturer}'

class Car:
    def __init__(self, brand, car_class, weight, driver, engine):
        self.brand = brand
        self.car_class = car_class
        self.weight = weight
        self.driver = driver
        self.engine = engine

    def start(self):
        print('Поехали')

    def stop(self):
        print('Останавливаемся')

    def turn_right(self):
        print('Поворот направо')

    def turn_left(self):
        print('Поворот налево')

    def __str__(self):
        return f'Car: {self.brand}, Class: {self.car_class}, Weight: {self.weight} kg\n{self.driver}\n{self.engine}'

class Truck(Car):
    def __init__(self, brand, car_class, weight, driver, engine, carrying_capacity):
        super().__init__(brand, car_class, weight, driver, engine)
        self.carrying_capacity = carrying_capacity

    def __str__(self):
        return f'Truck: {self.brand}, Class: {self.car_class}, Weight: {self.weight} kg, Carrying Capacity: {self.carrying_capacity} kg\n{self.driver}\n{self.engine}'

class SportCar(Car):
    def __init__(self, brand, car_class, weight, driver, engine, max_speed):
        super().__init__(brand, car_class, weight, driver, engine)
        self.max_speed = max_speed

    def __str__(self):
        return f'SportCar: {self.brand}, Class: {self.car_class}, Weight: {self.weight} kg, Max Speed: {self.max_speed} km/h\n{self.driver}\n{self.engine}'

# Пример использования классов
driver1 = Person("Asanali Aidosov", 10)
engine1 = Engine(200, "Toyota")
car1 = Car("Toyota Camry", "Sedan", 1500, driver1, engine1)

driver2 = Person("Alibek Kanatov", 5)
engine2 = Engine(300, "Audi")
sport_car = SportCar("Audi R8", "Coupe", 1400, driver2, engine2, 330)

driver3 = Person("Zhaibek Alibekov", 8)
engine3 = Engine(400, "Volvo")
truck = Truck("Volvo FH", "Truck", 12000, driver3, engine3, 20000)

print(car1)
print("\n---")
print(sport_car)
print("\n---")
print(truck)