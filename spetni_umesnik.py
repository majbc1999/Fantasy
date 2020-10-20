import bottle
import json


from main import Uporabnik, Tekma, Napoved, Tabela
from orodje_za_json import dodaj_uporabnika, preveri

# Tukaj se potem začne spet graditi spletna stran

@bottle.get("/")
def prijavna_stran():
    return bottle.template("prijavna_stran.tpl")

@bottle.get("/napaka/")
def vrni_napako():
    return bottle.template("napaka.tpl")

@bottle.get("/napaka2/")
def vrni_napako2():
    return bottle.template("napaka2.tpl")

@bottle.post("/registracija/<username>/<password>/<password2>/")
def registracija(username, password, password2):
    username = bottle.request.forms.getunicode("ime")
    password = bottle.request.forms.getunicode("password")
    password2 = bottle.request.forms.getunicode("password2")
    if password != password2:
        bottle.redirect("/napaka/")
    else: 
        if preveri(username)==False:
            bottle.redirect("/napaka2/")
        else:
            dodaj_uporabnika(username, password)
            bottle.redirect("/uspesnaregistracija")


@bottle.get("/uspesnaregistracija")
def vrni_uspeh():
    return bottle.template("uspeh.tpl")
        
# Program moramo na koncu še pognati

bottle.run(reloader=True, debug=True)