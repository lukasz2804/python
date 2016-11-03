
class Adres:
    pass


adr1 = Adres()#utworzenie rekordu
adr1.ulica = "stonogi"
adr1.nr = 23
adr1.kod = '445-214'
adr1.miasto = 'dno'

print adr1.ulica
print adr1.__dict__