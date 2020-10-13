# 4 Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:speed, color, name, is_police (булево)
# А также методы:go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
# который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.
class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = float(speed)
        self.color = color
        self.name = name
        self.is_police = bool(is_police)

    def go(self):
        print(f'машина {self.name} поехала')

    def stop(self):
        print(f'машина {self.name} остановилась')

    def turn(self, direction):
        print(f'машина {self.name} повернула {direction}')

    def show_speed(self):
        print(f'Скорость автомобиля {self.name} - {self.speed}')

    def police_test(self):
        if self.is_police:
            print(f'{self.name} - полицейская машина')
        else:
            print(f'{self.name} - не принадлежит полиции')

class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print('Скорость превышена!')


class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print('Скорость превышена!')


class SportCar(Car):
    pass


class PoliceCar(Car):
    pass


town_car_1 = TownCar(70, 'black', 'Audi Q3')
print(f'Автомобиль {town_car_1.name}, цвет - {town_car_1.color}, скорость - {town_car_1.speed}')
town_car_1.go()
town_car_1.show_speed()
town_car_1.turn('налево')
town_car_1.stop()
print(town_car_1.is_police)

town_car_2 = TownCar(50, 'green', 'Seat Lion')
town_car_2.show_speed()

work_car_1 = WorkCar(50, 'white', 'Kia Rio')
work_car_1.show_speed()

work_car_2 = WorkCar(40, 'black', 'Volkswagen Polo')
work_car_2.show_speed()

sport_car_1 = SportCar(110, 'red', 'Lamborghini Aventador')
sport_car_1.go()
sport_car_1.show_speed()
sport_car_1.turn('направо')
sport_car_1.stop()
sport_car_1.police_test()

sport_car_1 = PoliceCar(120, 'white', 'Ford Mondeo', True)
sport_car_1.show_speed()
sport_car_1.police_test()



