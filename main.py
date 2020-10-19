class Uporabnik:
    def __init__(self, ime):
        self.ime = ime
        self.score = 0
        self.zadetek = 0

    def dodaj_tocke(self, num):
        if num == 5:
            self.score += num
            self.zadetek += 1
        else: 
            self.score += num

class Tekma:
    def __init__(self, ekipa1, ekipa2):
        self.ekipa1 = ekipa1
        self.ekipa2 = ekipa2
        self.goli1 = None
        self.goli2 = None
        self.status = "nedokončana"
    
    def vpisi_rezultat(self, goli1, goli2):
        self.goli1 = int(goli1)
        self.goli2 = int(goli2)
        self.status = "dokončana"

class Napoved:
    def __init__(self, ekipa1, ekipa2):
        self.ekipa1 = int(ekipa1)
        self.ekipa2 = int(ekipa2)

    def num(self, tekma):
        if tekma.status == "nedokončana":
            return None
        else:
            seznam = [-1,1]
            #točen zadetek:
            if self.ekipa1 == tekma.ekipa1 and self.ekipa2 == tekma.ekipa2:
                return 50
            #netočen zadetek:
            else:
                tocke = 0
                #pravilna napoved zmagovalca:
                if ((self.ekipa1 - self.ekipa2 > 0 and tekma.goli1 - tekma.goli2 > 0) or
                    (self.ekipa1 - self.ekipa2 < 0 and tekma.goli1 - tekma.goli2 < 0) or
                    (self.ekipa1 - self.ekipa2 == 0 and tekma.goli1 - tekma.goli2 == 0)):
                    tocke += 10
                #točni goli ene ekipe:
                if (self.ekipa1 == tekma.goli1 or self.ekipa2 == tekma.goli2):
                    tocke += 15
                #točna razlika v golih:
                if (self.ekipa1 - self.ekipa2 == tekma.goli1 - tekma.goli2):
                    tocke += 20
                #točno število vseh zadetkov:
                if (self.ekipa1 + self.ekipa2 == tekma.goli1 + tekma.goli2):
                    tocke += 10
                #goli ene ekipe zgrešeni za 1:
                if (self.ekipa1 - tekma.goli1) in seznam:
                    tocke += 5
                if (self.ekipa2 - tekma.goli2) in seznam:
                    tocke += 5
                #razlika zgrešena za 1:
                if (self.ekipa1 - self.ekipa2 -  (tekma.goli1 - tekma.goli2)) in seznam:
                    tocke += 5
                #število zadetkov zgrešeno za 1:
                if (self.ekipa1 + self.ekipa2 - (tekma.goli1 + tekma.goli2)) in seznam:
                    tocke += 5
                return tocke

class Tabela:
    def __init__(self):
        self.uporabniki = []
    
    def dodaj_uporabnika(self, uporabnik):
        self.uporabniki.append(uporabnik)

    def izpisi_uporabnike(self):
        for uporabnik in self.uporabniki:
            print(uporabnik.ime)
            print(str(uporabnik.score))



