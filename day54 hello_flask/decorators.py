##Functions can have input/functionality/output

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide (n1, n2):
    return n1 / n2

## Functions are first-class objects, arguments 인수 (int/string/float) 로 passed around 전달될 수 있다.

def calculate(calculate_function, n1, n2):
    return calculate_function(n1, n2)

result = calculate(add, 2, 3)
print(result)

## Functions can be nested in other functions

def outer_function():
    print("I'm outer")

    def nested_function():
        print("I'm inner")

    nested_function()
outer_function()

# I'm outer
# I'm inner

## Functions can be returned from other functions

def outer_function():
    print("I'm outer")

    def nested_function():
        print("I'm inner")
    return nested_function

inner_function = outer_function()
inner_function
# I'm outer


## Simple Python Decorator Functions
import time

def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        function()
        function()
    return wrapper_function

#With the @ syntactic sugar
@delay_decorator
def say_hello():
    print("hello")

say_hello()
# after 2 seconds
# hello
# hello

@delay_decorator
def say_bye():
    print("bye")

#Without the @ syntactic sugar
def say_greeting():
    print("how are you?")

decorated_function = delay_decorator(say_greeting)
decorated_function()
# how are you?
# how are you?

###### Exercise #####

import time

current_time = time.time()
print(current_time)


def speed_calc_decorator(function):
    def wrapper_function():
        # function() #여기다 넣으면 두 함수 fast_function() & slow_function() 0.00s 결과나옴
        start_time = time.time()
        function()
        end_time = time.time()
        # function() #여기다 넣으면 두함수 모두 9.5367431640625e-07s
        print(f"{function.__name__} run speed: {end_time - start_time}s")
    return wrapper_function

@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i

@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i

fast_function()
slow_function()

# fast_function run speed: 0.4679410457611084s
# slow_function run speed: 4.427232980728149s


#### Advanced Decorators with *args and **kwargs ###