def a():
    return 5
print(a())

#5

def a():
    return 5
print(a()+a())

#5+5 prints 10

def a():
    return 5
    return 10
print(a())
#prints only the first return = 5

def a():
    return 5
    print(10)
print(a())
# prints only the return

def a():
    print(5)
x = a()
print(x)
# print 5

def a(b,c):
    return (b+c)
print(a(1,2) + a(2,3))
# i thought it would print 8, but it is an error because
#the functions does not return anything to add to the other
#function.if we change the print to return, it will print 8

def a(b,c):
    return str(b)+str(c)
print(a(2,5))
#25 - I learned that the str disables the number and converts
# it in a string. therefore, the numbers are not added, but the str

def a():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(a())
#first it prints b which is 100
#then checks for if statement - since b > 10, then it does not
#return 5. else, returns 10 - prints 10. the return 7 never gets
# executed


def a(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(a(2,3))
print(a(5,3))
print(a(2,3) + a(5,3))

#prints 7,14,21

def a(b,c):
    return b+c
    return 10
print(a(3,5))

#prints 8

b = 500
print(b)
def a():
    b = 300
    print(b)
print(b)
a()
print(b)  

#prints b outside, then b outside again, then b inside function
# then b outside fuction = 500,500,300,500

b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
a()
print(b)  
#since a() is not to print the return, then the result is the same
#as previous example  500 500 300 500 


b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
b=a()
print(b)

#500 500 300 300 - now it does print b inside and then the return


def a():
    print(1)
    b()
    print(2)
def b():
    print(3)
a()

#prints 1 3 2

def a():
    print(1)
    x = b()
    print(x)
    return 10
def b():
    print(3)
    return 5
y = a()
print(y)

#1 3 5 10