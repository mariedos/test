import time

n = 0
continuer = 'o'

while continuer == 'o':
    print("Le compteur est maintenant à {}".format(n))
    continuer = input("Voulez-vous continuer ? o/n")
    n += 1
