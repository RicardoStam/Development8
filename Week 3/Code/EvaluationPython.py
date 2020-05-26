##Function Application##
def identity(param1):
    return param1

print(identity(5))

##Function Call##
def fun1(x):
    return lambda y: x + y


def fun2(y):
    return y + 2


t = fun1(1)
u = fun2(1)

print(t(u))

##Function Call; additional information##
def fun1(x):
    print("fun1, param value: "+str(x))
    return lambda y: x + y


def fun2(y):
    print("fun2, param value: "+str(y))
    return y + 2

print("executing  t")
t = fun1(1)

print("executing  u")
u = fun2(3)

print("t = " + str(t) + " u = " + str(u))

print("executing  t(u)")
print(t(u))
