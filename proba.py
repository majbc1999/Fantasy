from main import Uporabnik, Tekma, Napoved, Tabela

majbc1999 = Uporabnik("majbc1999")
dejanbc = Uporabnik("dejanbc")

#Ustvarimo turnir in vanj dodamo uporabnika

turnir = Tabela()
turnir.dodaj_uporabnika(majbc1999)
turnir.dodaj_uporabnika(dejanbc)

#majbc1999 napove 0:0, dejanbc pa 1:3
#Napovedi
majbc1999ATLBAY = Napoved(0,0)
dejanbcATLBAY = Napoved(1,3)
majbc1999BARREA = Napoved(2,2)
dejanbcBARREA = Napoved(1,0)
majbc1999MAROLI = Napoved(2,2)
dejanbcMAROLI = Napoved(1,1)

#Tekma se konča z 1:1, 3:0, 2:3
ATLBAY = Tekma("Atletico", "Bayern")
ATLBAY.vpisi_rezultat(1,1)

BARREA = Tekma("Barca", "Real")
BARREA.vpisi_rezultat(3,0)

MAROLI = Tekma("Maribor", "Olimpija")
MAROLI.vpisi_rezultat(2,3)

majbc1999.dodaj_tocke(majbc1999ATLBAY.num(ATLBAY))
dejanbc.dodaj_tocke(dejanbcATLBAY.num(ATLBAY))
majbc1999.dodaj_tocke(majbc1999BARREA.num(BARREA))
dejanbc.dodaj_tocke(dejanbcBARREA.num(BARREA))
majbc1999.dodaj_tocke(majbc1999MAROLI.num(MAROLI))
dejanbc.dodaj_tocke(dejanbcMAROLI.num(MAROLI))

#Prištejemo točke in izpis

turnir.izpisi_uporabnike()