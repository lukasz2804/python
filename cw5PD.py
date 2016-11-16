#pracadomowa
#utworzy liste o podanych rozmiarach
#uzupelni randem
#wyswietli
#wyszuka wielokrotnosc liczby 2,3,5 i zapisze kazda do nowej listy
#wyszuka duplikaty i stworzy nowa
#zastapi duplikaty znakiem 'x'
#usunie duplikaty z listy a
#obliczy srednia i podniesie kazda wartos do potegi 3
#zastapi wielogrotnosic 2 lietera a ,3 litera e, 5 litera l
import random
random.seed(421431)
class List:
    tab = None
    def create(self, a):
        self.tab = [None] * a
        return self.tab

    def fillWithRand(self,a,b):
        for x in range(0,len(self.tab)):
            self.tab[x] =random.randint(a, b)

    def printTab(self):
        print self.tab
    def multipications(self,value):
        a = []
        for x in range(0,len(self.tab)):
            if(self.tab[x]%value==0):
                a.append(self.tab[x])
        return a
    def duplicates(self):
        a = []
        for x in range(0,len(self.tab)):
            if(self.tab.count(self.tab[x])>1):
                if(self.tab[x] not in a):
                    a.append(self.tab[x])
        return a
    def removeDuplicates(self):
        a = []
        for x in range(0,len(self.tab)):
            if(self.tab[x] not in a):
                a.append(self.tab[x])
        return a
    def duplicatesToX(self):
        a = []
        for x in range(0,len(self.tab)):
            if(self.tab[x] not in a):
                a.append(self.tab[x])
            else:
                a.append('x')
        return a
    def average(self):
        aver = 0
        a=[]
        for x in range(0,len(self.tab)):
            aver = aver + self.tab[x]
            a.append(self.tab[x]*self.tab[x]*self.tab[x])
        print aver/len(self.tab)
        return a
    def chngetoletters(self):
        for x in range(0,len(self.tab)):
            if(self.tab[x]%2==0):
                self.tab[x]='A'
            elif(self.tab[x]%3==0):
                self.tab[x]='E'
            elif(self.tab[x]%5==0):
                self.tab[x]='L'
        return self.tab
    def maketext(self,lenofTEXT):
        a = []
        for x in range(0, len(self.tab)):
            if (isinstance(self.tab[x], str)):
                a.append(self.tab[x])
        for i in range(0,lenofTEXT):
            test = random.randint(0, len(a))
            print a[test],
l = List()
l.create(12)
print l.tab
l.fillWithRand(1,300)
print l.tab
l.printTab()
print l.multipications(4)
print l.chngetoletters()
l.maketext(5)