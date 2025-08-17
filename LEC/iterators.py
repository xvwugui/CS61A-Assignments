s = [1,2,3,4,5,6]

it = iter(s)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))

def evens(start, end):
    even = start + (start % 2)
    while even < end:
        yield even
        even += 2

list(evens(1, 10))

t = evens(1,15)#到这里其实都还没有运行过the body of function
next(t)   #到调用next这里才开始运行函数体,并且会一直执行到yield为止

def a_then_b(a, b):
    for x in a:
        yield x
    for y in b:
        yield y
