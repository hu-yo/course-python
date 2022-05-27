def prnSum(name, *args):
    print(name,args,'=',sum(args))
       
a={'a':1,'b':2}
a1={'c':3}
a2={**a,**a1}
a.update(a1)
a3={*a,*a1}

def d(n,**k):
    print(f'{n}',k)
d('陳',a=1,b=2)

dict4={'red':3,'green':2,'blue':1}
d('pp',**dict4)

