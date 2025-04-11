
# ======================================Lamda Function=======================================

# s1="hello from lamda function"
# s2=lambda x:x.upper()
# print(s2(s1))

# num=lambda x: "positive" if x>0 else "negative" if x<0 else "zero"
# print(num(5))
# print(num(-5))
# print(num(0))

# sqr=lambda x: x**2
# print(sqr(3))

# li=[lambda arg=x: arg*10 for x in range(1,10)]
# for i in li:
#     print(i())

# check=lambda x: "even" if x%2==0 else "odd"
# print(check(4))
# print(check(7))

# calcii=lambda x,y: (x+y,x*y,x-y,x%y,x/y)
# print(calcii(2,3))

# n=[1,2,3,4,5,6,7,8,9,10]
# even=filter(lambda x: x%2==0,n)
# print(list(even))

# n=[1,2,3,4,5]
# x=map(lambda x: x*2,n)
# print(list(x))

# from functools import reduce
# a=[1,2,3,4,5]
# b=reduce(lambda x,y: x*y, a)
# print(b)

# name="Mohammed Abdul Rahman"
# age=22
# print("my name is {} and i am {} years old".format(name,age))
# print("my name is {0} and i am {1} years old".format("a",25))
# print(f"my name is {name} and i am {age} years old")

# def fun1(msg):
#     def fun2():
#         print(msg)
#     fun2()
# fun1("hello")

# import inspect
# def decorator(greet):
#     def wrapper():
#         print("before calling the function")
#         greet()
#         print("after calling the function")
#     return wrapper

# @decorator
# def greet():
#     print("hello world")
# greet()

# print(inspect.signature(greet))

# ===========================OOPS==================================

# class Dog:
#     sound="barking"
#     walk="walking"
#     run="running"

# dog1=Dog()

# print(dog1.sound)
# print(dog1.walk)
# print(dog1.run)

# class Dog:
#     species="Canine"
    
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

# dog1=Dog("puppy",5)

# print(dog1.name)
# print(dog1.age)
# print(dog1.species)

# class Dog:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
        
#     def __str__(self):
#         return f"{self.name} is {self.age} years old"
    
# dog1=Dog("buddy",3)
# dog2=Dog("puppy",5)

# print(dog1)
# print(dog2)

# class Dog:
#     species="canine"
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

# dog1=Dog("buddy",3)
# dog2=Dog("puppy",5)

# print(dog1.species)
# print(dog1.name)
# print(dog1.age)
# dog1.species="max"
# print(dog1.species)
# dog1.name="abc"
# print(dog1.name)


# ==============Inheritance================

# class Animal:
#     def __init__(self, name):
#         self.name = name
    
#     def sound(self):
#         raise NotImplementedError("error")
    
# class dog(Animal):
#     def sound(self):
#         return "boouuuu!"
    
# a=Animal("generic animal")
# dog1=dog("puppy")

# print(a.name)
# print(dog1.sound())
# print(dog1.name)

# ==========================

# class Color:
#     def __init__(self):
#         self.name="green"
#         self.lg=self.Lightgreen()
        
#     def show(self):
#         print('name',self.name)
        
#     class Lightgreen:
#         def __init__(self):
#             self.name='light green'
#             self.code='1234'
#         def display(self):
#             print('name',self.name)
#             print('code',self.code)
            
# outer=Color()
# outer.show()

# g=outer.lg
# g.display()

# class Parent():
#     def show(self):
#         print("inside parent")
        
# class Child(Parent):
#     def show(self):
#         super().show()
#         print("inside child")
        
# obj=Child()
# obj.show()

# class Private:
#     def __init__(self):
#         self.__salary=5000
#     def salary(self):
#         return self.__salary
    
# obj=Private()
# print(obj.salary())
# # print(obj.__salary)

# class protected:
#     def __init__(self):
#         self._salary=5000
#     def salary(self):
#         return self._salary
    
# obj=protected()
# print(obj.salary())
# print(obj._salary)

# ==========iterator=============

# num=[1,2,3,4,5]
# iter=iter(num)
# print(next(iter))
# print(next(iter))
# print(next(iter))
# print(next(iter))
# print(next(iter))

# ============scope============

# def fun():
#     x=300
#     print(x) # LOCAL SCOPE
    
# fun()

# def fun1():
#     x=300         #Enclosing Scope
#     def fun2():
#         print(x) 
#     fun2()
# fun1()


# x=300

# def fun():
#     print(x)  # Global function
# fun()
# print(x)

# =============sample.py and sample2.py===================

# =============Math==========

import math

# x=math.ceil(2.1)
# print(x)

# x=math.floor(2.1)
# print(x)

# x=math.sqrt(25)
# print(x)

# x=math.pow(2,3)
# print(x)

# x=math.pi
# print(x)
