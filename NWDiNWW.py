
def nwd(l1,l2):
    while(l1-l2 != 0):
        if(l1>l2):
            l1=l1-l2
        elif(l2>l1):
            l2=l2-l1
    if(l1<l2):
        return l1
    else:
        return l2

def nww(l1,l2):
    print (l1*l2)/(nwd(l1,l2))

nwd(1989,867)
nww(3,4)

#1989 i 867 jest liczba 51.