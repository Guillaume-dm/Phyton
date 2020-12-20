print("Suite du Héron d'Alexandre")#Exercice des racines carrées de 2
n=int(input("Saisir n : "))
u=2
for k in range(n) :
    u=0.5*(u+(2/u))
print (u)
