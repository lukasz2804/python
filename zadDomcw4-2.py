#napisz skrypt ktory bedzie dzialal jak ksiazka adresowa Dodaj,usun,edytuj, wyswietl w tabeli# imie nazwisko adres ,email
import os
from prettytable import PrettyTable

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
baza['0'] = Ksiazka("1234","26413","31634","46116","564136413")
baza['1'] = Ksiazka("2","3","4","5","6")
while(ctn):
    print "Witaj, co chcesz zrobic?"
    print "1 - Dodaj rekord:"
    print "2 - Usun rekord:"
    print "3 - Edytuj rekord:"
    print "4 - wyswietl"
    print "5 - zakoncz"
    do = input("?\n")
    if(do == 1):
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
        del(baza[id])
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
        t = PrettyTable(['ID','Imie', 'Nazwisko','Miasto','Nr Domu','Nr telefonu'])
        for key in baza.keys():
            t.add_row([key, baza[key].imie,baza[key].nazwisko,baza[key].miasto,baza[key].nrDomu,baza[key].nrTel])
            #print key+"\t"+baza[key].imie+"\t | \t"+baza[key].nazwisko+"\t | \t"+baza[key].miasto+"\t | \t"+baza[key].nrDomu+"\t | \t"+baza[key].nrTel+"|"
        print t
    elif(do == 5):
        break
    else:
        print "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
        print "nie wiem co robic"
