##wczesniej instalowalem pyCHarm (nowa pracownia)
#17
slownik = {1:9}
print slownik

c=set([5,4,9])
c.add(1)
print c

d = set()
print d

print len(c),len(d)

print 5 in c, 5 in d

print not(5 in c), not(5 in d)
#czy 5,4 jest podzbiorem c
print set([5,4]) <= c

print d.issubset(c)
#czy 1,4 jest nadzbiorem c
print set([1,4])>= c
#isupperset robi to samo
print set([1,1]).issuperset(c)

print "\n\n\n"
#laczenie zbiorow
E = c | d
print E
print '\n'

#czesc wspolna
print c&d
print '\n'
#roznica
print c-d
print '\n'
#roznica symetryczna
print c^d
print '\n'



