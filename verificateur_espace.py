print("INDIQUEUR DE PREMIER ESPACE DANS UNE CHAINE DE CARACTERE- ")
print(" ")
i=0
chaine=input("Saisir la chaine : ")
while chaine[i]!= " " and i<(len(chaine)-1):
    i=i+1
if chaine[i]==" " :
    print ("Premier espace au  : ",i,"caractère(s).")
else :
    print ("Il n'y a pas d'espace pour la chaine de caractère saisie.")
