# str="mohammed"
# rev=str[::-1]
# print(rev)
# print(str)

# def Prime(num):
#     if num==0 or num==1:
#         return False
#     else:
#         for i in range(2,int(num**0.5)+1):
#             if num%i==0:
#                 return False
#     return True
# # 
# print("PRIME" if Prime(10) else "not prime")

# num=4
# fact=1
# while num>=1:
#     fact*=num
#     num-=1  
# print(fact)

# inp=[1,2,3,4,5,6,7,8,9]
# res=sorted(set(inp))
# print(res[-2])

# inp=[1,2,4,7,9,2,3,4,5,6,7,8,9]
# res=[]
# inp=sorted(inp)
# for i in range(0,len(inp)-1):
#     if inp[i]!=inp[i+1]:
#         res.append(inp[i])
        
# res.append(inp[-1])
# print(res)

# inp=[1,2,4,7,9,2,3,4,5,6,7,8,9]
# res=[]
# seen=set()
# for i in inp:
#     if i not in seen:
#         res.append(i)
#         seen.add(i)
# print(res)


import array

# fruits=array.array("u","This is an array")
# print(fruits[1])

# class Person:
    
#     def __init__(self, name, age, height, weight):
#         self.name=name,
#         self.age=age,
#         self.height=height,
#         self.weight=weight
    
# person1=Person("A",22,26.4,87)
# print(person1.name)
# print(person1.age)
# print(person1.height)
# print(person1.weight)

# ===============================programming===================================

# list=[1,2,3,4,5,6]
# res=[]
# for i in list:
#     if i%2==0:
#         res.append(i)
# print(res)

# def print_even(lst):
#     return [num for num in lst if num % 2 == 0]

# print(print_even([1, 2, 3, 4, 5, 6]))
# # Output: [2, 4, 6]

# list=[1,2,3,4,5,6]
# res=sum(list)
# print(res)


# num=12345
# rev=int(str(num)[::-1])
# print(rev)

# num=5
# for i in range(1,11):
#     print(f"{num} x {i} = {num*i}")

# str="asdaqw1313124"
# res=str.isdigit()
# if res:
#     print("numaric string")
# else:
#     print("not a ")

# num=3213154
# if num<2:
#     print("not prime")
# else:
#     for i in range(2,int((num**0.5)+1)):
#         if num%i==0:
#             print("not prime")
#             break
#     else:
#         print("prime")    

# str="moam"
# rev=str[::-1]
# if str==rev:
#     print("palidrome")
# else:
#     print("not a palidrome")

# list1=[1,2,3,4,5,10]
# list2=[1,2,3,4,5,6,7,8,9,10]
# res=set(list1) & set(list2)
# print(res)

# num=[0,1]
# fibonacii=10
# for i in range(fibonacii-2):
#     num.append(num[-1]+num[-2])
# print(num)

# list=[5,4,3,2,1]
# for i in range(len(list)):
#     for j in range(i+1,len(list)):
#         if list[i]>list[j]:
#             list[i], list[j]=list[j],list[i]
# print(list)

# str="banana"
# freq={}
# for i in str:
#     freq[i]=freq.get(i, 0)+1
# for j in freq.items():
#     print(j)

# list=[1,1,1,1,2,2,2,4,4,4,4,4,3,3,3,3,3]
# res=(set(list))
# print(res)

# string="qwertyuiopasdfghjklzxcvbnm"
# count=0
# for i in string:
#     if i in ['a','e','i','o','u']:
#         count+=1
# print(count)

# class Parent():
#     def cook(self):
#         print("cooking")

# class child(Parent):
#     def code(self):
#         print("coding")
        
# child1=child()
# child1.cook()
# child1.code()

# class father():
#     name="A"
#     age=36
#     def drive(self):
#         print("driving")
# class mother():
#     name="X"
#     age=30
#     def cook(self):
#         print("cooking")
# class child(father, mother):
#     def code(self):
#         print("coding")
# child1= child()
# child1.drive()
# child1.cook()
# child1.code()
# print(child1.name)

# class animal():
#     def jungle(self):
#         print("many animal in jungle")
#     def run(self):
#         print("running")
# class dog(animal):
#     def run(self):
#         super().run()
#         print("dog is running")
# class lion(animal):
#     def run(self):
#         print("lion is running")
# dog1=dog()
# dog1.run()
# dog1.jungle()

# class student():
#     def __init__(self, name, age, marks):
#         self.name=name
#         self.age=age
#         self.marks=marks
# s1=student("abhi", 22, 'A GRADE')
# s2=student("ram", 25, 'B GRADE')
# print(f"my name is {s1.name} i am {s1.age} years old i scored {s1.marks}")
# print(f"my name is {s2.name} i am {s2.age} years old i scored {s2.marks}")

# class calci():
#     def add(self,a=0,b=0,c=0):
#         return a+b+c
# cal=calci()
# print(cal.add())
# print(cal.add(1))
# print(cal.add(1,2))
# print(cal.add(1,2,3))
        
# class car():
#     def mileage(self):
#         pass
# class honda(car):
#     def mileage(self):
#         print("25 KMPL")
# c1=honda()
# c1.mileage()


# list=[1,2,3,4,5]
# res=[]
# for i in range(len(list)):
#     res.append(list[-i-1])
# print(res)

# numbers = ['a', 'b', 'b', 'a', 'c', 'c', 'c', 'c']

# frequency = {}

# for num in numbers:
#     if num in frequency:
#         frequency[num] += 1
#     else:
#         frequency[num] = 1

# for i,j in frequency.items(): 
#     print(i,j)

# for i in range(3,100):

#     # else:
#         for j in range(2,i-1):
#             if i%j==0:
#                 # print("not prime")
#                 break
#         else:
#             print(i)

# list=[1,2,3,4,5,6,7,8,9,10]
# for i in range(0,len(list)):
#     if list[i]%2!=0:
#         print(i)

# num=4
# res=1
# while num>0:
#     res*=num
#     num-=1
# print(res)

# fibo=[0,1]
# n=5
# for i in range(n-2):
#     fibo.append(fibo[-1]+fibo[-2])
# print(fibo)

# str="mohammed badul rhamna"
# res=str.find("mohammed")
# if res==0:
#     print(str)
# else:
#     print("not matched")
# # print(res)