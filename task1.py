# Most Used String Function In Python.

'''str="My Name Is Mohammed Abdul Rahman"

print(len(str))
print(str.lower())
print(str.upper())
print(str.strip())
print(str.split())
print(str.replace("Is","is"))
print(str.find("a"))
print(str.count("a"))
print(str.startswith("M"))

print(str.capitalize())
print(str.title())
print(str.lstrip())
print(str.rstrip())
print(str.zfill(100))
print(str.center(100,'.'))
print(str.ljust(100,'.'))
print(str.rjust(100,'.'))
print(str.partition("A"))
print(str.isalpha())
print(str.isdigit())
print(str.isalnum())
print(str.isspace())
print(str.isupper())
print(str.islower())

encoded=str.encode()
print(encoded)
print(encoded.decode())

name="Mohammed Abdul Rahman"
age=22
print("my name is {} and i am {} years old".format(name,age))

trans=str.maketrans('a','x')
print(str.translate(trans))'''

# END =============================================================================

# Most Used List(Array) Functions

# numbers=[1,2,3,4,5,6,7,8,9,10]

# print(len(numbers))

# numbers.append(11)
# numbers.append(12)
# print(numbers)

# numbers.extend([13,14,15])
# print(numbers)

# numbers.insert(0,'a')
# print(numbers)

# numbers.remove(1)
# print(numbers)

# print(numbers.pop(1))
# print(numbers)

# print(numbers.index(5))

# print(numbers.count(5))

# numbers.sort()
# print(numbers)

# numbers.reverse()
# print(numbers)

# copy=numbers.copy()
# print(copy)

# numbers.clear()
# print(numbers)

# print(max(numbers))
# print(min(numbers))

# print(sum(numbers))

# even=[x*2 for x in range(5)]
# print(even)

# for i,n in enumerate(numbers):
#     print(i,n)

# char=['a','b','c','d','e','f','g','h','i','j']
# merge=list(zip(numbers,char))
# print(merge)

# square=list(map(lambda x:x**2,numbers))
# print(square)

# even=list(filter(lambda x:x%2==0,numbers))
# print(even)

# odd=list(filter(lambda x:x%2!=0,numbers))
# print(odd)

# del numbers[1]
# print(numbers)

# ---------------------------------------END----------------------------------------------

# Tuple Functions

# numbers=(1,2,3,4,5,6,7,8,9,10)

# print(len(numbers))
# print(numbers.count(2))
# print(numbers.index(5))
# print(max(numbers))
# print(min(numbers))
# print(sum(numbers))
# print(numbers[1:5])

# num1=(1,2,3)
# num2=(4,5,6)
# concat=num1+num2
# print(concat)

# print(numbers*2)

# person=("Mohammed Abdul Rahman",22,"13-6-823/A/2")
# name,age,address=person
# print(name)
# print(age)
# print(address)

# list=[1,2,3]
# tuple=tuple(list)
# print(tuple)

# name=('a','b')
# score=(80,90)
# merge=tuple(zip(name,score))
# print(merge)

# print(sorted(numbers))


# for i,numbers in enumerate(numbers):
#     print(i,numbers)

# square=tuple(map(lambda x: x**2,numbers))
# print(square)

# even=tuple(filter(lambda x: x%2==0,numbers))
# print(even)

# ========================================END================================================

# marks=int(input(("enter the grade ")))
# if marks>=90 and marks<=100: print("Grade A")
# elif marks>=80 and marks<90: print("Grade B")
# elif marks>=70 and marks<80: print("Grade C")
# elif marks>=60 and marks<70: print("Grade D")
# else: print("FAIL")

# string="mohammed abdul rahman"
# rev_string=string[::-1]
# print(rev_string)

# string="mohammed abdul rahman"
# rev_string=""
# for i in string:
#     rev_string=i+rev_string
# print(rev_string)

# string="mom"
# rev_string=""
# for i in string:
#     rev_string=i+rev_string
# if string==rev_string:
#     print("Palidrome")
# else: 
#     print("Not Palidrome")

# def is_prime(n):
#     if n < 2:
#         return False 
#     for i in range(2, n-1):
#         if n % i == 0:
#             return False
#     return True

# num = int(input("Enter a number: "))

# if is_prime(num):
#     print("Prime number.")
# else:
#     print("NOT a Prime number.")

# def fibonacci(n):
#         fib_series = [0,1]
#         for i in range (2,n):
#                 fib_series.append(fib_series[-1]+fib_series[-2])
#         return fib_series[:n]


# print(fibonacci(10))

# num=int(input("enter the number "))
# if num%2==0:
#     print("even number")
# else:
#     print("odd number")

# num=1
# if num==1 or num==0: print("not prime")
# for i in range(2,num-1):
#     if num%i==0:
#         print("not prime")
#         break
#     else: print("prime")

# for i in range(1,100):
#     if i % 2 == 0:
#         print("@")
#     else:
#         print(i)

# col = [1,2,3,4,5]
# for i in range(0,len(col)):
#     col[i] = col[i]*col[i]
# print(col)


# OR

# col = [1,2,3,4,5]
# square=list(map(lambda x:x**2,col))
# print(square)


# data = {
#     "name": "Abdul Rahman",
#     "age": 22,
#     "city": "HYD",
#     "profession": "Software Engineer"
# }

# print("Available keys:", list(data.keys()))

# key = input("Enter a key to retrieve its value: ")

# if key in data:
#     print("The value for",key, "is :",data[key])
# else:
#     print("Key not found in dictionary.")

# def get_details():
#     details = {}
#     details["name"] = input("Enter your name: ")
#     details["age"] = int(input("Enter your age: "))
#     details["city"] = input("Enter your city: ")
#     details["profession"] = input("Enter your profession: ")
#     return details

# def display_details(details):
#     print("\nUser Details:")
#     for key, value in details.items():
#         print(f"{key.capitalize()}: {value}")

# user_details = get_details()
# display_details(user_details)









