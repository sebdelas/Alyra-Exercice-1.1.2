#!/usr/bin/env python3

def recherche(saisie, borneMin, borneMax):
   nb = (borneMax // 2) + (borneMin // 2)
   if (nb == saisie):
       return nb;
   if (nb > saisie):
       if (nb < borneMax):
          borneMax = nb
       return recherche(saisie, borneMin, borneMax)
   else:
       if (nb > borneMin):
          borneMin = nb
       return recherche(saisie, borneMin, borneMax)

saisie = int(input("Saisissez un nombre entre 1 et 100, le programme va tenter de le trouver : "))
while saisie > 100 or saisie < 1:
    print("N'essayez pas de tricher, le nombre n'est pas compris entre 1 et 100")
    saisie = int(input("Saisissez un nombre entre 1 et 100, le programme va tenter de le trouver : "))
print("Trop facile, c'était " + str(recherche(saisie, 1, 100)))
print("Merci d'avoir joué :-)")
