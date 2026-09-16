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
class Employee:
    def __init__(self, name,salary,location):
        self.name = name
        self.salary = salary
        self.location = location

    def show_name(self):
        print(self.name,self.location)
    def change_name(self,change_name):
        self.name = change_name
        return  self.name

emp1 = Employee('Bharath',50000,'hyd')

emp1.change_name("vijay")
emp1.show_name()