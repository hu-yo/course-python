def a(a,b,c=3):
     print(a,b,c,0)
def ppt(a,b='QQ'):
    print(f'a={a},b={b}')
def caic(w,h):
    return [((w+h)*2,w*h),'正方' if w==h else '長方']
ppt('qq','pp')
((x,b),c)=caic(9,9)
print(x,b,c)




s=[(3,4),(2,4),(5,3)]
def calc(w,h):
    return w*h
def calcAll(c,f):
    for r in c:
        print(f(r[0],r[1]),end=' ')
calcAll(s,calc)

