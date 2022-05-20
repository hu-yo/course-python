def mul(x):
    z=1
    for a in range(1,x+1):
        z=z*a
    return z

z=mul(10)
print(z)

def add(x):
    t=0
    for a in range(1,x+1):
        t=t+a
    return t

def calcall(value, func):
    return func(value)
t=add(10)
print(t)
print(calcall(10,add))
print(calcall(10,mul))




def mu(x):
    z=1
    for a in x:
        z=z*a
    return z

def ad(x):
    t=0
    for a in x:
        t=t+a
    return t
x=[1,2,5]
funcs=[ad,mu]
for f in funcs:
    print(calcall(x,f))