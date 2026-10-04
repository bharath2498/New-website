# def add_func(a,b):
#     add = a+b
#     return add
# def mul_func(a,b):
#     mul = a*b
#     return mul
# result=mul_func(10,20)
# print(result)

# def calculate_sal(basic,bonus):
#     return basic + bonus

# print(calculate_sal(35000,15000))


# def create_user(name,role="user"):
#     return f"{name} is {role}"
# print (create_user("ravi", role="admin"))

# def calculate_total(*args):
#     # add all the numbers
#     for num in args:
         
#          c = num + c
#     return c

# print(calculate_total(100, 200, 300, 400))
# def create_employee(**kwargs):
#     for key,val in kwargs.items():
#         print(key ,":", val)
# create_employee(
#     name="Bharath",
#     salary=50000,
#     role="Python Developer"
# )

# def employee(name, *skills, **details):
#     print("Name:", name)
#     print("Skills:", skills)
#     print("Details:", details)
# employee(
#     "bharath",
#     "python",
#     "django",
#     "flask",
#     salary=1000,
#     loc="hyd"
# )
# def square(x):
#     return x * x

# numbers = [1, 2, 3, 4, 5]

# result = map(square, numbers)

# print(list(result))
# numbers = [10, 15, 20, 25, 30, 35]
# result = filter(lambda x:x>20,numbers)
# print(list(result))
# employees = [
#     {"name": "A", "salary": 40000},
#     {"name": "B", "salary": 60000},
#     {"name": "C", "salary": 50000}
# ]

# result = sorted(employees, key=lambda x: x["salary"],reverse=True)

# print(result)
# numbers = [10, 15, 20, 25, 30]
# result= [num for num in numbers if num>20]
# print(result)

# users = [
#     {"name": "A", "active": True},
#     {"name": "B", "active": False},
#     {"name": "C", "active": True}
# ]

# active_users = [user for user in users if not user["active"]==False]
# print(active_users)

# employees = [
#     {"name": "A", "salary": 40000},
#     {"name": "B", "salary": 60000},
#     {"name": "C", "salary": 50000}
# ]

# dict_com = { employee["name"]:employee["salary"] for employee in employees }
# print(dict_com)

class InvalidSalaryError(Exception):# craeting an custom exception
    pass
class Employee():

    company = "infosys" #class variable

    @classmethod #class methods
    def change_company(cls, new_company):
        cls.company = new_company

    def __init__(self, name,salary,location):# insatance vaiables & init metods
        self.name = name
        self.salary = salary ## encapsulation uses to hide the sesitive date without calling from oustside the class
        self.location = location

    def show_details(self):# method
        print(self.name,self.location,self.salary)

    def change_name(self,new_name):
        self.name = new_name
    @property                #  getter method
    def salary(self):
        return self.__salary
    @salary.setter            
    def salary(self, new_salary): # setter method
        if new_salary <= 0:
            raise InvalidSalaryError("salary must be greater than 0")
        self.__salary = new_salary

    def salary_increment(self,salary_increment):
        self.salary = self.salary + salary_increment

    def location_change(self,new_loc):
        self.location = new_loc

    @staticmethod #python STATIC METHOD doesnt call call  cls or self when we use static it will take 1 argumet 
    def valid_salary(salary):
        return salary > 0
    
class devolper(Employee):# inheritance
    def __init__(self, name, salary, location,language):
        super().__init__(name, salary, location)#calling parent intilization values
        self.language = language 

    def show_details(self):# method overriding
        super().show_details()
        print(self.language)




# # Employee.change_company("Google")
# # print(Employee.company)

# # dev1 = devolper(
# #     "Bharath",
# #     50000,
# #     "hyd",
# #     "Python"
# # )
# # dev1.show_details()


# emp1 = Employee(50000)
# print (emp1.salary) 
# emp1.salary_increment(5000)
# emp1.get_salary()

# # print(emp1.valid_salary(500000))
# emp2 = Employee('Bharath',-50000,'hyd')
# print(emp2.salary)
# print(emp2.salary)
# emp2.salary = 70000
# print(emp2.salary)
# emp2.salary_increment(-100000)
# print(emp2.salary)
# # print(dev1.change_company("accenture"))
# # emp1.change_name("vijay")
# # emp1.salary_increment(25000)
# # emp1.location_change("banglore")
# # emp1.show_details()
# # emp2.show_name()

# # from abc import ABC,abstractmethod
# # # class EmployeeRole(ABC):## abstraction
# # #     @abstractmethod
# # #     def work(self):
# # #         pass
# # # class Developer(EmployeeRole): ## polymorphism
    # def work(self):
    #     print("Writing a code")

# # # class Tester(EmployeeRole):
# # #     def work(self):
# # #         print("testing a code")

# # # team_members = [Developer(),Tester()]
# # # for team_member in team_members:
# # #     team_member.work()
# # # emp = EmployeeRole()

# class Employee: # using setter and getter class controls the values
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary

#     @property
#     def salary(self):
#         return self.__salary

#     @salary.setter
#     def salary(self, new_salary):
#         if new_salary <= 0:
#             print("Invalid salary")
#         else:
#             self.__salary = new_salary
# s = Employee('B',-50000)
# print(s.salary)


# class Employee: ## these are the __str__ & __repr__ mainly used for the user print and devolpers debugging
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary

#     def __str__(self):
#         return f"{self.name} earns {self.salary}"

#     def __repr__(self):
#         return f"Employee(name='{self.name}', salary={self.salary})"

# emp1 =  Employee('bharath',50000)
# print(emp1)
# print(repr(emp1))

# class Database:#composite method
#     def connect(self):
#         print("Database connected")


# class UserService:
#     def __init__(self, database):
#         self.database = database

#     def get_users(self):
#         self.database.connect()
#         print("Fetching users")


# db = Database()
# user_service = UserService(db)

# user_service.get_users()

# try:
#     num1 = int(2.0)
#     num2 = 2

#     c = num1//num2

# except ZeroDivisionError as e: #ecxeption handling
#     print("invalid division", e)
# except ValueError as e:
#     print("invalid number", e)
# else:
#     print("result :" ,c)
# finally:
#     print("code executed")

# def validate_age(age):
#     if age < 18:
#         raise ValueError("you are not ready yet")# raising an error 
#     else:
#         print("Welcome")
# validate_age(17)

# from utils.calculator import add

# ac=add(10,20,30,40,50)
# print(ac)
# def log_function(func):

#     def wrapper():
#         print("starting func")

#         func()

#         print("finished func")

#     return wrapper
# @log_function
# def add():
#     print(10 + 20)

# def log_function(func):
#     print("Decorator received:", func)
#     def wrapper():
#         func()
#     return wrapper
# @log_function
# def add():
#     print(10 + 20)
# add()

# def logger(func): #decorator 
#     print("logger executed")
#     def wrapper(*args,**kwargs):
#         print("wrapper execute")
#         func(*args,**kwargs)
#         print("done")
#     return wrapper
# @logger
# def add(a,b):
#     print(a+b)
# add(10,20)
# def even_numbers(list1):
#     for num in list1:
#         if num%2 ==0 :
#             yield num
        
# x=even_numbers([2,3,4,5,6])
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))

# path = r"C:\Users\maddu\OneDrive\Desktop\Bharathpython\localapp\sample.txt"

# with open(path, "w") as file:
#     file.write("Python Backend Developer")
# with open("sample.txt", "r") as file:
#     data = file.read()
    
# print(data)

# from utils.calculator import add

# def calculate_salary(basic:int,bonus:str):
#     x=add(basic,bonus)
#     print(x)
# calculate_salary(50000,25000)


# def get_names(users: list[dict]) -> list[str]:
#     return users 

# print(get_names([{'name':'a','value':'b'},{'name':'c','value':'d'}]))

# from dataclasses import dataclass

# @dataclass
# class Employee:
#     name: str
#     email: str
#     role: str = "user"
#     active: bool = True



# emp1 = Employee(
#     "Bharath",
#     "bharath@jdv.",
    
# )

# print(emp1)

# from enum import Enum

# class OrderStatus(Enum):
#     PENDING = "pending"
#     SHIPPED = "shipped"
#     DELIVERED = "delivered"
#     CANCELLED = "cancelled"
    
# # print(OrderStatus.SHIPPED)
# order = OrderStatus.SHIPPED.value
# print(order)

# from typing import TypedDict

# class UserData(TypedDict):
#     name: str
#     age: int
#     active: bool

# def show_user(user: UserData):
#     print(user["name"])
#     print(user["age"])
# user1: UserData = {
#     "name": "Bharath",
#     "age": 28,
#     "active": True
# }

# show_user(user1)

# from dataclasses import dataclass

# @dataclass
# class User:
#     id: int
#     name: str
#     active: bool


# def get_user(user_id: int) -> User | None:
#     if user_id == 1:
#         return User(1, "Bharath", True)

#     return None
# def show_user(user_id: int) -> None:
#     user = get_user(user_id)

#     if user is None:
#         print("User not found")
#         return

#     print(user.name)
# get_user(2)

# import logging

# logging.basicConfig(level=logging.INFO)
# from dataclasses import dataclass


# @dataclass
# class User:
#     id: int
#     name: str
#     active: bool

# def get_employee(employee_id: int) -> str|None:
#     if employee_id == 1:
#         logging.info("User found")
        
#         employee_data=User(1, "Bharath", True)

#         return employee_data.name
#     else:
#         logging.warning("Employee not found")
# x = get_employee(1)
# print(x)


# import os

# APP_NAME = os.getenv("APP_NAME", "BackendApp")
# PORT = os.getenv("PORT", "5000")

# print(APP_NAME)
# print(PORT)

# import json

# employee = {
#     "name": "Bharath",
#     "salary": 50000,
#     "active": True
# }

# json_data = json.dumps(employee)

# print(json_data)
# print(type(json_data))


# import json

# json_C_data = {"name": "Bharath", "age": 30,"city":"rjy"}


# with open("users.json", "w") as file:
#     json.dump(json_C_data, file)

# with open("users.json", "r") as file:
#    x = json.load(file)    
# print(x["city"])
# from datetime import datetime

# formatted= datetime.now()

# n_formatted = formatted.strftime("%d/%m/%Y %H:%M")

# print(n_formatted)

# date_object = datetime.strftime(
  
#     "%d-%m-%Y"
# )

# print(date_object)
# print(type(date_object))

# from datetime import datetime, timedelta

# now = datetime.now()

# deadline = now + timedelta(days=5)

# print(now)
# print(deadline)

# from datetime import datetime, timedelta

# now = datetime.now()
# expiry_time = now + timedelta(minutes=30)

# if now < expiry_time:
#     print("Token is still valid")
# else:
#     print("Token expired")

# from datetime import datetime, timedelta

# now = datetime.now()
# expiry_time = now - timedelta(minutes=30)

# if now > expiry_time:
#     print("Token expired")

#Small task: create created_at using the current UTC time and print it


# user1 = {
#     "name": "Bharath",
#     "skills": ["Python", "Django"]
# }

# user2 = user1.copy()

# user2["skills"].append("Flask")
# user2["skills"].append("java")

# user2['name'] = "ravi"
# print(user1)
# print(user2)

# from copy import deepcopy

# employee1 = {
#     "name": "Bharath",
#     "skills": ["Python", "SQL"]
# }

# employee2 = deepcopy(employee1)
# employee2["skills"].append("Django")
# print(employee1)
# print(employee2)
# skills = ["Python", "Django", "SQL"]

# for index, user in enumerate(skills, start=1):
#     print(index,user)
# employees = ["Bharath", "Ravi", "Kiran"]
# locations = ["Hyderabad", "Bangalore", "Chennai"]

# for employee,location in zip(employees,locations):
#     print(employee,location)

permissions = [True, True, False]

result = any(permissions)
result1 = all(permissions)

print(result,result1)