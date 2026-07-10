# class MyClass:
#     x=5
# p1=MyClass()
# print(p1.x)

# class Person:
#     def__init__(self,name,age):
#     self.name=NameError
#     self.age=age

#     p1=Person("Emil",36)

#     print(p1.name)
#     print(p1.age)

# class Car:
#     def __init__(self,brand,year):
#         self.brand=brand
#         self.year=year
#     def printname(self):
#         print(self.brand,self.year)
# x=Car("KIA",2025)
# x.printname()

# class Employee:
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
#     def printname(self):
#         print(self.name,self.salary)
# x=Employee("Navya",10000)
# x.printname()
# class Manager:
#     def __init__(self,department):
#         self.department=department
#     def printname(self):
#         print(self.department)
# x=Manager("IT")
# x.printname()

# class Person:
#     def __init__(self,name):
#         self.name=name
# class Student(Person):
#     def __init__ (self,name,marks):
#         super(). __init__(name)
#         self.marks=marks

#     def grade(self):
#         if self.marks > 90:
#             return "A"
#         elif self.marks > 75:
#             return "B"
#         else:
#             return "C"

#     def display(self):
#         print("Name:", self.name)
#         print("Marks:", self.marks)
#         print("Grade:", self.grade())

# s1=Student("Navya",55)
# s1.display()

# class Employee:
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
#     def printname(self):
#         print(self.name,self.salary)

# class Manager(Employee):
#         def __init__(name,salary,department):
#          super(). __init(name,salary)
#         self.department= department 


# def display(self):
#      print("Name:",self.name)
#      print("Salary:",self.salary)
#      print("Department:",self.department)
# emp=Employee("Navya",30000)
# mgr=Manager("Farsad",50000,"IT")

# print("Employee Details:")
# emp.display()

# print("/nManager Details:")
# mgr.display()

# Create Employee class
# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary

#     def display(self):
#         print("Name:", self.name)
#         print("Salary:", self.salary)

# class Manager(Employee):
#     def __init__(self, name, salary, department):
#         super().__init__(name, salary)
#         self.department = department

#     def display(self):
#         print("Name:", self.name)
#         print("Salary:", self.salary)
#         print("Department:", self.department)


# emp = Employee("Anu", 30000)
# mgr = Manager("Rahul", 50000, "IT")

# print("Employee Details:")
# emp.display()

# print("\nManager Details:")
# mgr.display()


# class Calculator:
#     def add(self,a,b,c=0):
#         return a+b+c
# obj= Calculator()
# print(obj.add(5,10))
# print(obj.add(5,10,20))


# class Calculator:
#     def add(self,*numbers):
#         return sum(numbers)
# obj=Calculator()
# print(obj.add(2,3))
# print(obj.add(2,3,4,5))


# class Animal:
#     def sound(self):
#      print("Animal makes a sound")
#      obj=Dog(Animal)
#     def sound(self):
#         print("Dog barks")
#         obj=Dog()
#         obj.sound()

# class Bank:
#     def interest_rate(self):
#         return 5
# class SBI(Bank):
#     def interest_rate(self):
#         return 7
# obj=SBI()
# print(obj.interest_rate())
    

# class Student:
#     def __init__(self,name):
#         self.name=name

#     def display(self):
#      print(self.name)
# obj=Student("Jiji")
# print(obj.name)
# obj.display


# class Student:
#     def __init__(self,name):
#      self._name=name

# class child(Student):
#     def show(self):
#      print(self._name)
# obj=child("Jiji")
# obj.show()
# print(obj._name)

# class Student:
#     def __init__(self,name):
#         self.__name=name
#     def display(self):
#         print(self.__name)
# obj=Student("Jiji")
# obj.display()
