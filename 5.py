import json

# X='{"name":"xyx","age":35}'
# Z=json.loads(X)
# print(Z["name"])
# print(Z["age"])

# x={
#     "name":"xyz",
#     "age":35
# }
# y=json.dumps(x)
# print(y)

import re

# x="The rain in spain"
# y=re.search("The .*spain$",x)
# if y:
#     print("Yes Matched")
# else:
#     print("Not Matched")

# x="The rain in spain"
# y=re.findall("ai",x)
# print(y)

# z=re.search("\s",x)
# z1=re.split("\s",x)
# z2=re.sub("\s","$",x)

# print(z)

# pattern=r"\d+"
# text="There are 123 apples"
# match=re.search(pattern,text)
# if match:
#     print("Match found:",match.group())

# pattern=r"\d+"
# text="There are 123 apples and 456 oranges"
# match=re.findall(pattern,text)
# print(match)

# pattern=r"(\d+)-(\d+)-(\d+)"
# text="The event is on 2025-03-26"
# match=re.search(pattern,text)
# if match:
#     print(match.group(1))
#     print(match.group(2))
#     print(match.group(3))

# import re

# text = "Please contact me at example@example.com"
# email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

# match = re.search(email_pattern, text)

# if match:
#     print("Email found:", match.group())
# else:
#     print("No email found.")

import logging

# logging.basicConfig(level=logging.DEBUG)

# logging.debug("hello, Debug!")
# logging.info("hello, info!")
# logging.warning("hello, warning!")
# logging.error("hello, error!")
# logging.critical("hello, critical!")

# logging.basicConfig(
#     level=logging.DEBUG,
#     filename='app.log',
#     filemode='a',
#     format='%(name)s - %(levelname)s - %(message)s'
#     )

# logging.debug("hello, Debug!")
# logging.info("hello, info!")
# logging.warning("hello, warning!")
# logging.error("hello, error!")
# logging.critical("hello, critical!")


# ==============Exception Handling===========

# try:
#     x=10/0
# except ZeroDivisionError:
#     print("cant Divide by Zero")
# finally:
#     print("completed execution")

# try:
    
#     num=int(input("enter the number"))
#     res=10/num
# except Exception as e:
#     print("an unexpected")
# except ValueError as e:
#     print(f"invalid input:{e}")
# except ZeroDivisionError as e:
#     print("cannot divide by zero")

# else:
#     print(f"Result:{res}")
# finally:
#     print("completed execution")

# def checkage(age):
#     if age>=18:
#         print("eligible for vote")
#     else:
#         raise ValueError("Age must be 18")
# try:
#     checkage(18)
# except ValueError as e:
#     print("error")

# class NotEligible(Exception):
#     pass
# def checkage(age):
#     if age>=18:
#         print("eligible")
#     else:
#         raise NotEligible("age must be 18")
# try:
#     checkage(17)
# except NotEligible as e:
#     print("error")
#     print(e)

# ============file handling==========

# file=open('file.txt','r')
# content=file.read()
# print(content)
# file.seek(0)
# content1=file.readline()
# content2=file.readlines()
# file.close()
# print(content1)

# file=open('file.txt','w')
# file.write("hello world\n")
# file.write("===============")

# file=open('file.txt','r')
# content=file.read()
# file.close()
# print(content)

import os

# if os.path.exists("file.txt"):
#     with open('file.txt','r') as file:
#         content=file.read()
#         print(content)
# else:
#     print("file not exist")

# try:
#     with open('file.txt','r') as file:
#         content=file.read()
#     with open('file1.txt','w') as fw:
#         fw.write(content)
#         print("file copied")
# except FileNotFoundError:
#     print("input or output operation file")
# except IOError as e:
#     print(f"I\O exception:{e}")
# except Exception as e:
#     print("an unexpected error")

# os.remove("file1.txt")






