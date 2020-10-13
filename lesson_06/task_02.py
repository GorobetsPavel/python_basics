# 2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина). Значения данных
# атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными. Определить метод расчета
# массы асфальта, необходимого для покрытия всего дорожного полотна. Использовать формулу: длина * ширина * масса
# асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см * чи сло см толщины полотна. Проверить работу.
# Например: 20м * 5000м * 25кг * 5см = 12500 т
class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calculate_mass(self, thickness=5, mass_on_1m=25):
        return round(self._length * self._width * thickness * mass_on_1m / 1000, 2)


test_road = Road(5000, 20)
print(test_road.calculate_mass(6, 20))
