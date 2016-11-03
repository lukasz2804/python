#sito
import math

class SitoErastotelesa:
    def start(self,n):
        l = []
        for i in range(0,n):
            l.append(True)
        r = math.sqrt(n)
        for i in range(2,int(r)):
            if(l[i]== True):
                for j in range(0,n):
                    z = int(math.pow(i,2)+(j*i))
                    if(z<n):
                        l[z]=False
        for i in range(0,n):
            if(l[i]==True and i<n and i!=0 and i!= 1):
                print i

x = SitoErastotelesa()
x.start(30)

