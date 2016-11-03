#1 napisz skrypt ktory losuje 6 niepowtarzajacych sie liczb z zakresu od 1 do 49
import random
random.seed()
m = []

while (len(m)<6):
    l = range(1,49)
    rnd = random.choice(l)
    if(not m.__contains__(rnd)):
        m.append(rnd)
print m#wybiera z l liczbe