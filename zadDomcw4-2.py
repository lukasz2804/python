#napisz skrypt ktory bedzie dzialal jak ksiazka adresowa Dodaj,usun,edytuj, wyswietl w tabeli# imie nazwisko adres ,email
import os

class Ksiazka:
    def __init__(self, imie, nazwisko, miasto, nrDomu,nrTel):
        self.imie = imie
        self.nazwisko = nazwisko
        self.miasto = miasto
        self.nrDomu = nrDomu
        self.nrTel = nrTel


ctn = True;
ctnid = True;
baza = {}
while(ctn):
    print "Witaj, co chcesz zrobic?"
    print "1 - Dodaj rekord:"
    print "2 - Usun rekord:"
    print "3 - Edytuj rekord:"
    print "4 - wyswietl"
    print "5 - zakoncz"
    do = input("?\n")
    if(do == 1):
        howManyADD = input("podaj ile chcesz dodac rekordow")
        for z in range(howManyADD):
            ctnid=True
            while(ctnid):
                id = raw_input("podaj swoj identyfikator(pesel)\n")
                if id in baza.keys():
                    print 'taki klucz juz istnieje'
                else:
                    ctnid=False
                    break
            im = raw_input("podaj swoje imie")
            nz = raw_input("podaj swoje nazwisko")
            mi = raw_input("podaj miasto")
            nrDomu = raw_input("podaj numer domu")
            nrTel = raw_input("podaj numer telefonu")
            baza[id] = Ksiazka(im,nz,mi,nrDomu,nrTel)
    elif(do == 2):
        id = raw_input("podaj swoj identyfikator(pesel)")
        if(baza.has_key(id)):
            del(baza[id])
        else:
            print "nie ma takiego peselu w bazie"
    elif(do == 3):
        id = raw_input("podaj swoj identyfikator(pesel)")
        print 'ktore pole chcesz edytowac?'
        print "1 - Imie"
        print "2 - Nazwisko"
        print "3 - Miasto"
        print "4 - nr. domu"
        print "5 - nr. Telefonu"
        do1 = input("?")
        if(do1 == 1):
            dane = raw_input("Podaj nowe imie")
            baza[id].imie = dane
        elif(do1 == 2):
            dane = raw_input("Podaj nowe nazwisko")
            baza[id].nazwisko = dane
        elif (do1 == 3):
            dane = raw_input("Podaj nowe miasto")
            baza[id].miasto = dane
        elif (do1 == 4):
            dane = raw_input("Podaj nowy nr. domu")
            baza[id].nrDomu = dane
        elif (do1 == 5):
            dane = raw_input("Podaj nowy nr. telefonu")
            baza[id].nrTel = dane
        else:
            break;
    elif(do == 4):
        if(len(baza.keys()) != 0):
            print "{:<8} {:<15} {:<10} {:<10} {:<10} {:<10}".format('KLUCZ', 'IMIE', 'NAZWISKO','MIASTO','NR.DOMU',"NR.TELEFONU")
            for k in baza.keys():
                print "{:<8} {:<15} {:<10} {:<10} {:<10} {:<10}".format(k, baza[k].imie, baza[k].nazwisko,baza[k].miasto,baza[k].nrDomu,baza[k].nrTel)
        else:
            print'Baza jest pusta'
    elif(do == 5):
        break
    else:
        print "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
        print "nie wiem co robic"
