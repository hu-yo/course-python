def a(w,*h):
    for arg in h:
        print(arg)
        w = w * arg
    return w
y=a(6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
print(y)

def calc(na,**k):
    print(na,k)
calc('q',r=1,b=2,c=3)

