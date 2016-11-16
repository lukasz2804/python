dziel = lambda x,y,z: (x+y)/z
print dziel(7,4,6)


xyz = (7,4,6)
print apply(dziel,xyz)


#map rzutuje funkcje na kazdy element
print map(lambda x: x*x*x, range(10))
print map(dziel,range(10),range(10),[2]*10)

#zip pakuje liste 1 do 2 kazdy element ma swoj odpowiednik
print zip ("abcdef",[1,2,3,4,5,6])

print zip (range(1,10),range(9,0,-1))
print zip("zip", range(0,9),zip(range(0,9)))


samogloska = lambda x: x.lower() in 'aeiou'
print samogloska("a")
print filter(samogloska,"ala ma kota")

print filter(lambda x: not samogloska(x),"ala ma kota")

#suma elementow
print reduce(lambda x,y: x+y, [1,2,3])
#suma ^2 elementow
print reduce(lambda x,y: x+y, map(lambda x: x*x,range(1,3)))