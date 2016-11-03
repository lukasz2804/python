#gra w losowanie
import random
random.seed()


nbd = input('podaj dolny zakres\n')
nbg = input('podaj gorny zakres\n')

rndnb =random.randrange(nbd,nbg)

rundy = input('podaj ile razy chcesz zgadywac\n')

for i in range(0,rundy):
    l = input('podaj liczbe\n')
    if(l<rndnb):
        print "twoja liczba jest mniejsza\n"
    elif(l>rndnb):
        print "twoja liczba jest wieksza\n"
    else:
        print "brawo, zgadles\n"
        break
print "wylosowana liczba to:%i. Nie poddawaj sie i zagraj jeszcze raz"%rndnb