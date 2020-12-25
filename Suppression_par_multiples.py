# Exercice du tableau à suppression
N=250
Crible = []
for i in range (2, N+1):
    Crible.append(i)
    i = 0
def SupprMult (Crible,Valeur,IndiceDeb, IndiceFin) :  
    for i in range (IndiceDeb,IndiceFin+1) :
        if Crible[i]!="x" :
            if Crible[i]%Valeur==0 :
                Crible[i]="x"
