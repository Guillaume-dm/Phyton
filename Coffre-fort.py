from random import *

print("GAME - COFFRE FORT ALEATOIRE A 3 CHIIFFRES:")
chiffre1= randrange(0,10)
chiffre2= randrange(0,10)
chiffre3= randrange(0,10)
compteur_essai = 1;
recherche1=float(input("Selon vous, le chiffre 1 est le : "))
while recherche1 != chiffre1 :
    if recherche1 > chiffre1 : 
        recherche1 = float(input("Le chiffre 1 est plus petit, veillez retentez :  "))
        compteur_essai += 1
    else :
        recherche1 = float(input("Le chiffre 1 est plus grand, veillez retentez :  "))
        compteur_essai += 1
print("Chiffre n°1 OK - recap : ", chiffre1,"- ? - ?")
recherche2 = float(input("Selon vous, le chiffre 2 est le : "))
while recherche2 != chiffre2 :
        if recherche2 > chiffre2 : 
            recherche2 = float(input("Le chiffre 2 est plus petit, veillez retentez :  "))
            compteur_essai += 1
        else :
            recherche2 = float(input("Le chiffre 2 est plus grand, veillez retentez :  "))
            compteur_essai += 1
print("Chiffre n°1 et n°2 OK - recap : ", chiffre1,"-", chiffre2,"- ?")
recherche3=float(input("Selon vous, le chiffre 3 est le : "))
while recherche3 != chiffre3 :
        if recherche3> chiffre3 : 
            recherche3 = float(input("Le chiffre 3 est plus petit, veillez retentez :  "))
            compteur_essai += 1
        else :
            recherche3 = float(input("Le chiffre 3 est plus grand, veillez retentez :  "))
            compteur_essai += 1
print("Le code était : ", chiffre1,"-",chiffre2,"-", chiffre3)
if compteur_essai < 2 :
    print("Vous avez trouvé en ", compteur_essai, "essai.")
else :
    print("Vous avez trouvé en ", compteur_essai, "essais.")
if compteur_essai < 9 :
    print("Félicitations, vous êtes un big boss de la logique et du décodage !!!")
else :
    print("Vous ^pouvez encore vous améliorer avec un peu d'entrainement...")
