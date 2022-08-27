class Person:  # Объявления класса
    def __init__(self, name, age): # Метод инициализации
        self.age = age   # Установка значений атрибутов
        self.name = name

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def function(self, arg1, ):
        self.name, self.age = arg, self.name


person = Person('John', 20)  # Создание экземпляра

print(person.name, person.age)

person.name = 'James' # Установка значения атрибута

print(person)

print(person.name, person.age)

person1 = Person('LALALA', 2000)

print(person1)

figure1 = Person(100, 100)

print(figure1.name)

figure2 = Person(200, 250)

print(figure2.name)

figure2.name += 100
figure2.age += 100

print(figure2)

figure2.function()

print(figure2)

