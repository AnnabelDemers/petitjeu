from Crypto.Random.random import randrange #pour le chiffre au hazard
from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets


print('hello bienvenue sur mosti.ca')

#on va demander le nombre max
print ("dis moi le nombre le plus haut")
#nombremax=input("->")
nombremax = widgets.Text(value='',
                         placeholder = 'type here',
                         description = 'nombre max:',
                         disabled    = False)
interact(nombremax)
#nombremax

#on va demander les nombre de vie
print ("dis moi le nombre de vies que tu desires")
vies=input("->")

#choisir un nombre au hazard selon le max
nombrehazard = randrange(1,int(nombremax))

for i in range(int(vies)):
    #demander l'essay
    print("entrer votre essai (vie numéro "+ str(i+1) +")")
    essai=input("->")
    #lui si il est trop haut trop bas ou c'est bien
    if nombrehazard==int(essai):
        print("bravo t'as réussi avec seulement "+str(i+1) +" vies")
        break
    elif nombrehazard>int(essai):
        print("trop petit")
    else:
        print("trop grand")
    #on recommence jusqu'a temps qu'il l'a  ou qu'il n'y a plus de vie

# bravo ou fail epic fail
if nombrehazard!=int(essai):
    print("fail epic fail")
