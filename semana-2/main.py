from abc import ABC, abstractmethod

class Department:
    def __init__(self, name, code):
        self.name = name
        self.code = code


class Employee(ABC):
    work_hours = 8
    def __init__(self, code, name, salary, department):
        self.code = code
        self.name = name
        self.salary = salary
        self.__department = department

    @abstractmethod
    def calc_bonus(self):
        pass

    def get_hours(cls):
        return cls.work_hours

    def get_department(self):
        return self.__department.name

    def set_department(self, department_name):
        self.__department.name = department_name


class Manager(Employee):
    def __init__(self, code, name, salary):
        department = Department('managers', 1)
        super().__init__(code, name, salary, department)

    def calc_bonus(self):
        return self.salary * 0.15


class Seller(Employee):
    def __init__(self, code, name, salary):
        department = Department('sellers', 2)
        super().__init__(code, name, salary, department)
        self.__sales = 0

    def calc_bonus(self):
        return self.__sales * 0.15

    def get_sales(self):
        return self.__sales

    def put_sales(self, sales):
        self.__sales += sales
