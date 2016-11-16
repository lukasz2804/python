###djvkdsio
###24 skrypt
l = range(1,21,2)
print l;

print [2*x for x in l]

print [(x, x*x)for x in range(1,5)]

print [(x, ord(x))for x in "ABCDEF"]

print [[]for x in range(10)]

print [x for x in l if x>10]

print [x for x in range(1,20)if not (x%3) or not (x%5)]

print [(x,ord(x))for x in "ABCDEF" if x in "AEIOUY"]


#x i y para kazdy z kazdym
print [(x,y)for x in range(1,5)
    for y in range(4,0,-1)]

#roznica miedzy wart z 1 i 2 listy
print[x-y for x in range(1,5)
    for y in range(4,0,-1)]

#slejanie napisu z wartosci z 3 list
print  [`x`+y+`z` for x in [1,2]
        for y in ['A','B']
        for z in[0,3]]

#para kazdy z kazdym jesli x<y
print  [(x,y) for x in range(1,5)
        for y in range(6,3,-1)
        if x<y]

# para jesli x+y<7
print  [(x,y) for x in range(1,5)
        for y in range(6,3,-1)
        if x+y<7]

#para kazdy z kazdym 1 pazysty 2 nieparzysty
print [(x,y) for x in range(1,5)
       if x%2!=0 and
        y%2==0]

#para kazdy z kazdym 1 parzysty 2 nieparzysty
print [(x,y) for x in range(1,5) if not (x%2)
       for y in range(6,2,-1) if y%2]