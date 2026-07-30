def a(i):
    def b(j):
        return i+j
    return b

hanshuB = a(1)
result= hanshuB(2) #3
print(f"result:{result}") 


def my_decorator(func):
    def wrapper(*args,**kwargs):
        print("111111111111")
        func(*args,**kwargs)
        print("222222222222")
    return wrapper


def sum(a,b):
    print(f"a:{a}+b:{b} = {a+b}")

sum1 = my_decorator(sum)
sum1(10,20)


@my_decorator
def sum(a,b):
    print(f"a:{a}+b:{b} = {a+b}")

sum(10,20)
