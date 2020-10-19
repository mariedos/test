import time

n = 0
continuer = 'o'
while continuer == 'o':
    print("Le compteur est maintenant à {}".format(n))
    print('Voulez-vous continuer? o/n')
    continuer = input()
    n += 1
