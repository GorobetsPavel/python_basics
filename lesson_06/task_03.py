# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
# income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
# например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker. В классе Position
# реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения
# атрибутов, вызвать методы экземпляров).
class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self.__income = income

    def get_wage(self):
        return float(self.__income.get('wage'))

    def get_bonus(self):
        return float(self.__income.get('bonus'))


class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return self.get_wage() + self.get_bonus()


new_position = Position('Jhon', 'Smith', 'worker', {"wage": 50000, "bonus": 5000})
print(new_position.get_full_name())
print(new_position.get_total_income())
