import time
def decor(flag):
    def timer(fn):
        def inner(*args,**kwargs):
            start= time.time()
            fn(*args,**kwargs)
            stop=time.time()
            print(f'the process takes {stop-start: .12f}s')
            return fn(*args,**kwargs)
        return inner
    return timer
@decor('+')
def sum(*args,**kwargs):
    result=0
    for i in args:
        result+=i
    for j in kwargs.values():
        result+=j
    return result
print(sum(1, 2, 3, a=4, b=50))
@decor('-')
def sub(a,b):
    return a-b



print(sub(20, 10))