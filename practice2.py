# class person:
#     def __init__(self, name, age):
#         self.name=name
#         self.age=age
        
#     def greet(self):
#         print("my name is",self.name," i am ",self.age," old")
    
# p1=person("abdul",24)
# p1.greet() 

# import json

# data = '{"name": "Rahman", "age": 24}'
# parsed = json.loads(data)
# print(parsed["name"])  # Output: Rahman

# json_string = json.dumps(parsed)
# print(type(json_string))



# str=input("enter")
# digit=0
# uppercase=0
# lowercase=0
# special=0
# for i in str:
#     if i>='0' and i<='9':
#         digit+=1
#     elif i>='a' and i<='z':
#         lowercase+=1
#     elif i>='A' and i<='Z':
#         uppercase+=1
#     else:
#         special+=1
# print("Digits:", digit)
# print("Lowercase letters:", lowercase)
# print("Uppercase letters:", uppercase)
# print("Special characters:", special)

# import array

# arr1 = array.array('i', [1, 2, 3])
# arr2 = array.array('i', [4, 5, 6])


# res = array.array('i', [0] * (len(arr1) + len(arr2)))


# for i in range(len(arr1)):
#     res[i] = arr1[i]


# for j in range(len(arr2)):
#     res[len(arr1) + j] = arr2[j]

# print(res)      
# print(list(res))


# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True

# matrix = []


# num1 = int(input("Enter num 1 (only prime): "))
# num2 = int(input("Enter num 2 (only prime): "))
# num3 = int(input("Enter num 3 (only prime): "))
# num4 = int(input("Enter num 4 (only prime): "))


# if is_prime(num1) and is_prime(num2) and is_prime(num3) and is_prime(num4):
#     matrix = [[num1, num2], [num3, num4]]
#     print("Prime Number Matrix:")
#     for row in matrix:
#         print(row)
# else:
#     print("Please enter only prime numbers.")
    
    
# year = int(input("Enter a year: "))

# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print(f"{year} is a Leap Year ")
# else:
#     print(f"{year} is NOT a Leap Year ")


# mat=[[1,2],[2,1]]
# transpose = [[mat[j][i] for j in range(len(mat))] for i in range(len(mat[0]))]

# if mat==transpose:
#     print("same same")
# else:
#     print("different")


# input=["flower","flow","flight"]
# output=""
# i=0

# for z in input:
#     if input[i][i]==input[1][i]==input[2][i]:
#         output+=input[i][i]
#         i+=1
    
# print(output)



# nums = ["1", "2", "3"]

# for i in nums:
#     for j in nums:
#         for k in nums:
#             if i != j and j != k and i != k:
#                 print(i + j + k)

# s = "aa"
# p = "aa"

# if s!=p and p.find('*')!=1 and p.find('.')!=0:
#     print("false")
# elif p.find('*'):
#     print("true")
# elif p.find('.'):
#     print("true")
# else:
#     print("false")



# nums = [1,3,6,10,15]
# nums.sort()
# min=max(nums)

# for i in nums:
#     for j in nums:
#         if i != j and j-i<min:
#             min=j-i


# for i in nums:
#     for j in nums:
#         if i != j and j-i==min:
#             print(i , j)


# n = 4421
# sum=0
# prod=1

# while n>0:
#     sum+=n%10
#     prod*=n%10
#     n//=10
    
# res=prod-sum
# print(res)



# nums = [1,2,3,3,4,4,5,6]

# k = 4

# if len(nums) % k != 0:
#     print("false")
# else:
#     for i in range(0, len(nums), k):
#         split = []
#         for j in range(i, i + k):
#             if nums[j] not in split:
#                 split.append(nums[j])
#             print(split)



# def most_frequent(lst):

#     max_count = 0

#     most_common = None

#     for x in lst:

#         count = lst.count(x)

#         if count > max_count:

#             max_count = count

#             most_common = x

#     return most_common

# print(most_frequent([1,2,3,1,43,2,4,2,4,2]))


# def most_frequent(lst):
#     freq = {}
#     for x in lst:
#         freq[x] = freq.get(x, 0) + 1
    
#     most_common = max(freq, key=freq.get)
#     return most_common

# print(most_frequent([1,2,3,1,43,2,4,2,4,2]))

# lst = [1, 2, 3, 4, 5]
# target = 6

# seen = set()
# result = []

# for num in lst:
#     complement = target - num
#     if complement in seen:
#         result.append((complement, num))
#     seen.add(num)

# print(result)


# arr = [5, 2, 9, 1, 3]
# i = 0

# while i < len(arr) - 1:
#     if arr[i] > arr[i + 1]:
#         arr[i], arr[i + 1] = arr[i + 1], arr[i]
#         i = 0
#     else:
#         i += 1

# print(arr)


# import mysql.connector


# conn = mysql.connector.connect(
#     host='localhost',
#     user='root',
#     password='root',
#     database='revature'
# )

# cursor = conn.cursor()


# cursor.callproc('GetMyDetails')


# for result in cursor.stored_results():
#     for row in result.fetchall():
#         print(f"Name: {row[0]}, Age: {row[1]}, Email: {row[2]}")

# cursor.close()
# conn.close()

# def my_decorator(func):
#     def wrapper():
#         print("Before function call")
#         func()
#         print("After function call")
#     return wrapper

# @my_decorator
# def say_hello():
#     print("Hello!")

# say_hello()


# a = [1, 0, 5, 0, 6, 2, 0, 9]
# s = 0
# l = len(a) - 1

# while s < l:
#     if a[s] == 0 and a[l] != 0:
#         a[s], a[l] = a[l], a[s]
#         s += 1
#         l -= 1
#     elif a[s] != 0:
#         s += 1
#     else:
#         l -= 1


# for i in range(s):
#     for j in range(0, s - i - 1):
#         if a[j] > a[j + 1]:
#             a[j], a[j + 1] = a[j + 1], a[j]

# print(a)

# class Car:
#     def __init__(self, brand):
#         self.brand = brand
    
#     class Engine:
#         def __init__(self, power):
#             self.power = power
        
#         def show_power(self):
#             print("Engine power:", self.power, "HP")


# my_car = Car("Toyota")


# my_engine = Car.Engine(150)
# my_engine.show_power()

# import copy

# original = [1, 2, [3, 4]]

# deep_copy = copy.deepcopy(original)
# deep_copy[2][0] = 'changed'

# print("Original:", original)    
# print("Deep copy:", deep_copy) 


# def counter():
#     count = 0
#     def increment():
#         nonlocal count
#         count += 1
#         print(count)
#     increment()
#     increment()

# counter()

# output:

# 1
# 2

# ==================================================================

# from collections import defaultdict

# def group_anagrams(inp):
#     anagram_dict = defaultdict(list)
    
#     for word in inp:
#         sort = ''.join(sorted(word))
#         anagram_dict[sort].append(word)
    
#     return list(anagram_dict.values())


# inp = ["eat", "tea", "tan", "ate", "nat", "bat"]
# print(group_anagrams(inp))

# ==================================================================

# inp="abcabcbb"
# out=""
# for i in inp:
#     if i not in out:
#         out+=i
# print(len(out))

# ==================================================================
# matrix = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
# list=[]
# out = 0

# for i in range(len(matrix)):
#     for j in range(len(matrix[i])):
#         if i-j == 0 or i+j == 2:
#             list.append(matrix[i][j])

# print(out)


# def str(s):
#     sub_str = s.split('0')
#     while '' in sub_str:
#         sub_str.remove('')
#     return {
#         'first_name': sub_str[0],
#         'last_name': sub_str[1],
#         'id': sub_str[2]
#     }


# print(str("mohammed000abdulrahman000123"))


# s1 = "eueiieo"
# s2 = "iieoedue"

# for ch in s2:
#     if s2.count(ch) > s1.count(ch):
#         print(ch)
#         break


# def is_shadow_sentence(s1, s2):
#     w1 = s1.split()
#     w2 = s2.split()

#     if len(w1) != len(w2):
#         return False

#     for i in range(len(w1)):
#         if len(w1[i]) != len(w2[i]):
#             return False
#         for letter in w1[i]:
#             if letter in w2[i]:
#                 return False

#     return True
# print(is_shadow_sentence("they are round", "fold two times")) 
# print(is_shadow_sentence("his friends", "our company"))   


# s = input("Enter a sentence: ")
# words = s.split()

# for word in words:
#     for letter in word:
#         if word.count(letter) > 1:
#             print("True")
#             exit()
# print("False")

# def block_position(p1, p2):
#     lines = [
#         [0, 1, 2], [3, 4, 5], [6, 7, 8],  
#         [0, 3, 6], [1, 4, 7], [2, 5, 8],  
#         [0, 4, 8], [2, 4, 6]              
#     ]

#     for line in lines:
#         if p1 in line and p2 in line:
#             for spot in line:
#                 if spot != p1 and spot != p2:
#                     return spot
#     return None

# print(block_position(0, 1))
# print(block_position(5, 8))
# print(block_position(0, 4))
# print(block_position(6, 7))
# print(block_position(7, 0))


# def ascii_to_hex(s):
#     return ' '.join(format(ord(c), '02x') for c in s)
# print(ascii_to_hex("Hi!"))




# def to_morse_code(text):
#     morse_dict = {
#         'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
#         'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
#         'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
#         'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
#         'Y': '-.--', 'Z': '--..',
#         '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
#         '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
#         ',': '--..--', '.': '.-.-.-', '?': '..--..', '!': '-.-.--', ':': '---...',
#         "'": '.----.', ' ': '/'
#     }

    
#     text = text.upper()

#     morse_code = ' '.join(morse_dict.get(char, '') for char in text)
#     return morse_code

# print(to_morse_code("Hello, World!"))


# import datetime

# def has_friday_13(month, year):
    
#     date = datetime.date(year, month, 13)
#     return date.weekday() == 4

# print(has_friday_13(9, 2025))  
# print(has_friday_13(6, 2025))  



# from pyspark.sql import SparkSession

# # Create a Spark session
# spark = SparkSession.builder.appName("SampleApp").getOrCreate()

# # Create a DataFrame from a list
# data = [("Alice", 25), ("Bob", 30), ("Charlie", 35)]
# columns = ["Name", "Age"]
# df = spark.createDataFrame(data, columns)

# # Show the DataFrame
# df.show()

# # Filter data where age > 28
# df.filter(df.Age > 28).show()


# paragraph = [
#     ["Hello", "world", "hello"],
#     ["this", "is", "a", "test"],
#     ["STOP", "ignore", "this", "line"],
#     ["should", "not", "be", "processed"]
# ]

# out = {}

# for row in paragraph:
#     for word in row:
#         word_lower = word.lower()

#         if word_lower == "stop":
#             break  
#         if len(word_lower) < 3:
#             continue  

#         if word_lower in out:
#             out[word_lower] += 1
#         else:
#             out[word_lower] = 1
#     else:
#         continue  
#     break  

# print(out)


# board = [
#     ["X", "O", "X"],
#     ["O", "X", ""],
#     ["O", "", "X"]
# ]

# winner = ""

# if board[0][0] == board[0][1] == board[0][2] and board[0][0] != "":
#     winner = board[0][0]
# elif board[1][0] == board[1][1] == board[1][2] and board[1][0] != "":
#     winner = board[1][0]
# elif board[2][0] == board[2][1] == board[2][2] and board[2][0] != "":
#     winner = board[2][0]

# elif board[0][0] == board[1][0] == board[2][0] and board[0][0] != "":
#     winner = board[0][0]
# elif board[0][1] == board[1][1] == board[2][1] and board[0][1] != "":
#     winner = board[0][1]
# elif board[0][2] == board[1][2] == board[2][2] and board[0][2] != "":
#     winner = board[0][2]

# elif board[0][0] == board[1][1] == board[2][2] and board[0][0] != "":
#     winner = board[0][0]
# elif board[0][2] == board[1][1] == board[2][0] and board[0][2] != "":
#     winner = board[0][2]

# if winner != "":
#     print("Winner is:", winner)
# else:
#     print("Draw")


# S = "ABCDEFGHIJKLIMNOQRSTUVWXYZ"
# W = 4

# for i in range(0, len(S), W):
#     print(S[i:i+W])


# n = int(input())
# a = "abcdefghijklmnopqrstuvwxyz"
# width = 4 * n - 3
# lines = []

# for i in range(n):
#     s = '-'.join(a[n-1:i:-1] + a[i:n])
#     lines.append(s.center(width, '-'))

# print('\n'.join(lines[::-1] + lines[1:]))

# import calendar

# month, day, year = map(int, input("MM DD YYYY").split())
# day_name = calendar.day_name[calendar.weekday(year, month, day)]
# print(day_name.upper())


# m = int(input())
# set_m = set(map(int, input().split()))
# n = int(input())
# set_n = set(map(int, input().split()))

# result = sorted(set_m ^ set_n)

# for num in result:
#     print(num)


# text = "rise to vote sir"
# reversed_text = text[::-1]
# print(reversed_text)



# text = input("Enter a string: ")
# result = text[::2]
# print(result)



# total_heads = 35
# total_legs = 94


# for chickens in range(total_heads + 1):
#     rabbits = total_heads - chickens 
#     legs = chickens * 2 + rabbits * 4
#     if legs == total_legs:
#         print("Chickens:", chickens)
#         print("Rabbits:", rabbits)
#         break
