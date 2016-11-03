import random
#21


random.seed()
print random.randint(1,15)
print random.randint(1,15)

l = range(1,10)
print random.choice(l) #wybiera z l liczbe
random.shuffle(l)  #permutacja l
print l

print random.random()              #losowa 0-1
print random.uniform(10,30)         #losowa rzeczywista 10-30

print random.normalvariate(5,48) #zmienna losowa o rozkladzie 5 i odchyleniu 48

