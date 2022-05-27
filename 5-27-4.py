def call(va,fu):
    return fu(va)
a=int(input('輸入'))
b=lambda x:list (range(1,x+1))
c=lambda x:[y for y in range(1,x+1)]
print(call(a,b)) 

s=[(2,2),(5,9),(4,6),(86,0)]
a=sorted(s,key=lambda e:e[1])
s=[(2,2),(5,9),(4,6),(86,0)]
p=sorted(s,key=lambda e:e[0])
s=[(2,2),(5,9),(4,6),(86,0)]
m=sorted(s)
print(a,end='\t\t')
print(p,end='\t\t')
print(m,end='\t\t')
