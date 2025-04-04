# # 1. Single Inheritance
# print("----- Single Inheritance -----")
# class Animal:
#     def sound(self):
#         print("Animal makes sound")

# class Dog(Animal):
#     def bark(self):
#         print("Dog barks")

# dog = Dog()
# dog.sound()
# dog.bark()


# # 2. Multiple Inheritance
# print("\n----- Multiple Inheritance -----")
# class Father:
#     def skills(self):
#         print("Father: Singing")

# class Mother:
#     def skills(self):
#         print("Mother: Cooking")

# class Child(Father, Mother):
#     def extra_skills(self):
#         Mother.skills(self)
#         print("Child: Dancing")

# child = Child()
# child.skills() 
# child.extra_skills()


# # 3. Multilevel Inheritance
# print("\n----- Multilevel Inheritance -----")
# class Grandfather:
#     def legacy(self):
#         print("Grandfather: Landowner")

# class Parent(Grandfather):
#     def job(self):
#         print("Parent: Engineer")

# class Son(Parent):
#     def hobby(self):
#         print("Son: Gamer")

# son = Son()
# son.legacy()
# son.job()
# son.hobby()


# # 4. Hierarchical Inheritance
# print("\n----- Hierarchical Inheritance -----")
# class Vehicle:
#     def start(self):
#         print("Vehicle starts")

# class Car(Vehicle):
#     def drive(self):
#         print("Car is being driven")

# class Bike(Vehicle):
#     def ride(self):
#         print("Bike is being ridden")

# car = Car()
# car.start()
# car.drive()

# bike = Bike()
# bike.start()
# bike.ride()


# # 5. Hybrid Inheritance
# print("\n----- Hybrid Inheritance -----")
# class A:
#     def method_A(self):
#         print("Class A")

# class B(A):
#     def method_B(self):
#         print("Class B")

# class C(A):
#     def method_C(self):
#         print("Class C")

# class D(B, C):  # Hybrid: combination of Multiple + Multilevel
#     def method_D(self):
#         print("Class D")

# d = D()
# d.method_A()
# d.method_B()
# d.method_C()
# d.method_D()

# ========================Overloading========================

# class Calculator:
#     def add(self, a=0, b=0, c=0):
#         return a + b + c

# calc = Calculator()
# print(calc.add(5, 10))         
# print(calc.add(1, 2, 3))       
# print(calc.add(7))        

# ========================Overriding========================

# class Animal:
#     def speak(self):
#         print("Animal speaks")

# class Dog(Animal):
#     def speak(self):
#         print("Dog barks")

# class Cat(Animal):
#     def speak(self):
#         print("Cat meows")

# dog = Dog()
# cat = Cat()

# dog.speak()   # Dog barks
# cat.speak()   # Cat meows

# =================Public Modifier===================

# class Car:
#     def __init__(self):
#         self.brand = "Toyota"

#     def show(self):
#         print(f"Brand: {self.brand}")


# c = Car()
# print(c.brand) 

# =================protected Modifier===================

# class Employee:
#     def __init__(self):
#         self._salary = 50000 

# class Manager(Employee):
#     def show_salary(self):
#         print(f"Manager's Salary: {self._salary}")

# m = Manager()
# m.show_salary()       #accessable
# print(m._salary)      #not accessable

# =================private Modifier===================

# class BankAccount:
#     def __init__(self):
#         self.__balance = 10000  # Private

#     def show_balance(self):
#         print(f"Balance: ₹{self.__balance}")

#     def deposit(self, amount):
#         self.__balance += amount

# # Accessing
# acc = BankAccount()
# acc.show_balance()
# acc.deposit(2000)
# acc.show_balance()

# # Direct access (will fail)
# # print(acc.__balance)        #  Error

# print("Accessing using name mangling:", acc._BankAccount__balance)



