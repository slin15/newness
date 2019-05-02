'''
Susan Lin and Sophia Xia
SoftDev2 pd08
K#22 Closure
2019-05-01
'''

def repeat(s):
    def nest(n):
        if(n == 1):
            return s
        else:
            return nest(n-1) +s
    return nest

r1 = repeat("hello")
r2 = repeat("goodbye")

print(r1(2))
print(r2(2))
print(repeat("cool")(2))

def make_counter():
    x = 0
    def incr():
        nonlocal x
        x += 1
        print(x)
    return incr

ctr1 = make_counter()
ctr1()
ctr1()

ctr2 = make_counter()
ctr2()
ctr1()
ctr2()
