print ("Suite du Fibonaci ")
o=int(input("Saisir votre nombre : "))
u=0
v=1
if o==0 :
    v=0
n=0
n=n+2
while (n<=o) :
    if (u<v) :        
        u=v+u
    else :
        v=u+v
    n=n+1
n=n-1
print ("n=",n)
if u>v :
    print(u)
else :
    print (v)
