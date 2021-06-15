def add(x,y):
    try:
        return x+y
    except TypeError:
        pass
    return "fail"



def subtract(x,y):
    return x-y


def multiply(x,y):
    return x*y

def divide(x,y):
    try:
        z=x/y
        return z
    except ZeroDivisionError:
        #print('exception zero')
        pass
    return 'fail'
print(add(10,'@'))
print(divide(10,0))
