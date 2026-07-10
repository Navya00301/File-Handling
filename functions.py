# def add_numbers(a,b):
#     sum=a+b
#     print('sum:',sum)
# add_numbers(2,3)

# def add_numbers(a=7,b=8):
#     sum=a+b
#     print("Sum:",sum)

# add_numbers(2,3)
# add_numbers(a=2)
# add_numbers()

# def display_info(first_name,last_name):
#     print("First Name:",first_name)
#     print("Last Name:", last_name)
# display_info(last_name="Cartman",first_name="Eric")

# def find_sum(*numbers):
#     result=0
#     for num in numbers:
#         result=result+num
#     print("Sum=",result)
        
# find_sum(1,2,3)
# find_sum(4,9)

# square=lambda x:x*x
# print(square(5))

# nums=[1,2,3,4]
# result=list(map(lambda x:x*x,nums))
# print(result)

# nums=[1,2,3,4,5,6]
# result=list(filter(lambda x:x%2==0,nums))
# print(result)

# from functools import reduce
# nums=[1,2,3,4]
# result=reduce(lambda x,y:x+y,nums)
# print(result)

# def numbers():
#     return[1,2,3]
# print(numbers())

# def numbers():
#     yield 1
#     yield 2
#     yield 3
#     gen=numbers()
#     print(gen)
# gen=numbers()

# print(next(gen))
# print(next(gen))
# print(next(gen))

# def my_decorator(func):
#     def wrapper():
#         print("Before function runs")
#         func()
#         print("After function runs")
#     return wrapper
# @my_decorator
# def say_hello():
#     print("Hello Sister")
# say_hello()

# def new_decorator(func):
#     def wrapper():
#         print("Starting Function")
#         func()
#         print("Function finished")
#     return wrapper
# @new_decorator
# def say_hello():
#     print("Learning Python")
# say_hello()

# def numbers():
#     yield 1
#     yield 2
#     yield 3
#     yield 4
#     yield 5
#     gen=numbers()
#     print(gen)
# gen=numbers()

# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))

cube=lambda x:x*x
print(cube(3))

# nums=[1,2,3,4]
# result=list(map(lambda x:x**x,nums))
# print(result)

# nums=[10,20,35,45,60,77]
# result=list(filter(lambda x:x>50,nums))
# print(result)