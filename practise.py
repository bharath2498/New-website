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


class Employee():
    company = "infosys" #class variable
    @classmethod #class methods
    def change_company(cls, new_company):
        cls.company = new_company

    def __init__(self, name,salary,location):# insatance vaiables & init metods
        self.name = name
        self.__salary = salary ## encapsulation uses to hide the sesitive date without calling from oustside the class
        self.location = location

    def show_details(self):# method
        print(self.name,self.location,self.__salary)
    def change_name(self,new_name):
        self.name = new_name
    def get_salary(self):
        print(self.__salary)
    def salary_increment(self,salary_increment):
        self.__salary = self.__salary + salary_increment
    def location_change(self,new_loc):
        self.location = new_loc
    @staticmethod
    def valid_salary(salary):
        return salary > 0
class devolper(Employee):# inheritance
    def __init__(self, name, salary, location,language):
        super().__init__(name, salary, location)# method overriding
        self.language = language 
    def show_details(self):
        super().show_details()
        print(self.language)




# Employee.change_company("Google")
# print(Employee.company)

# dev1 = devolper(
#     "Bharath",
#     50000,
#     "hyd",
#     "Python"
# )
# dev1.show_details()


emp1 = Employee('Bharath',50000,'hyd')
emp1.salary_increment(5000)
emp1.get_salary()

print(emp1.valid_salary(500000))
# emp2 = Employee('Bharath',50000,'hyd')
# print(dev1.change_company("accenture"))
# emp1.change_name("vijay")
# emp1.salary_increment(25000)
# emp1.location_change("banglore")
# emp1.show_details()
# emp2.show_name()

# from abc import ABC,abstractmethod
# # class EmployeeRole(ABC):## abstraction
# #     @abstractmethod
# #     def work(self):
# #         pass
# # class Developer(EmployeeRole): ## polymorphism
# #     def work(self):
# #         print("Writing a code")

# # class Tester(EmployeeRole):
# #     def work(self):
# #         print("testing a code")

# # team_members = [Developer(),Tester()]
# # for team_member in team_members:
# #     team_member.work()
# # emp = EmployeeRole()