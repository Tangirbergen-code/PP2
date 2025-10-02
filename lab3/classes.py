# task-1
class String_Handler:
    def __init__(self):
        self.txt = ""
    
    def get_string(self):
        self.txt = input("Введите строку: ")
    
    def print_string(self):
        print(self.txt.upper())
    
obj = String_Handler()
obj.get_string()
obj.print_string()

# task-2
# class Shape:
#     def __init__(self):
#         pass  

#     def area(self):
#         return 0  

# class Square(Shape):
#     def __init__(self, length):
#         self.length = length  
#     def area(self):
#         return self.length * self.length  

# shape = Shape()
# print("Shape area:", shape.area())  

# square = Square(5)
# print("Square area:", square.area())  

# task-3
# class Shape:
#     def __init__(self):
#         pass
#     def area(self):
#         return 0

# class Rectangle(Shape):
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#     def area(self):
#         return self.length * self.width
    
# length = int(input("Введите длину: "))
# width = int(input("Введите ширину: "))
# rect = Rectangle(length, width)
# print("Rectangle area: ", rect.area())

# task-4
# import math
# class Point:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y

#     def show(self):
#         print(f"Координаты точки: ({self.x}, {self.y})")

#     def move(self, new_x, new_y):
#         self.x = new_x
#         self.y = new_y

#     def dist(self, other):
#         return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

# p1 = Point(2, 3)
# p2 = Point(5, 7)

# p1.show()
# p2.show()

# print("Расстояние между точками:", p1.dist(p2))

# p1.move(10, 10)
# p1.show()

# task-5
# class Account:
#     def __init__(self, owner, balance=0):
#         self.owner = owner
#         self.balance = balance

#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount
#             print(f"На счёт {self.owner} зачислено {amount}. Баланс: {self.balance}")
#         else:
#             print("Сумма должна быть положительной!")

#     def withdraw(self, amount):
#         if amount > self.balance:
#             print(f"Недостаточно средств! Баланс: {self.balance}")
#         elif amount <= 0:
#             print("Сумма должна быть положительной!")
#         else:
#             self.balance -= amount
#             print(f"Со счёта {self.owner} снято {amount}. Баланс: {self.balance}")

#     def __str__(self):
#         return f"Владелец: {self.owner}, Баланс: {self.balance}"


# acc = Account("Эля", 100)   
# print(acc)

# acc.deposit(50)             
# acc.withdraw(30)            
# acc.withdraw(200)          
# acc.deposit(-20)            
# acc.withdraw(-10)           

# task-6
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 20]

# primes = list(filter(
#     lambda x: x > 1 and all(x % i != 0 for i in range(2, int(x**0.5) + 1)),
#     numbers
# ))

# print("Простые числа:", primes)