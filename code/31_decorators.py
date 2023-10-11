# def f1(func):
#     def wrapper(*args, **kwargs):
#         print("Starting...")
#         return func(*args)
#     return wrapper


# @f1
# def f2(a):
#     print(a)
    
    
# @f1
# def f3(a,b):
#     print(a + b)
    
# f2("Hello world")
# f3(3,2)

def get_num(question):
    def decorator(func):
        def wrapper(*args):
            while True:
                try:
                    num = int(input(question))
                    return func(num)
                except ValueError:
                    print("Not a number.")
        return wrapper
    return decorator


@get_num("Give a positive number: ")
def get_pos(x):
    if x > 0:
        return print("You picked:",x)
    else:
        print("That's not a positive number")
        return get_pos()

get_pos()