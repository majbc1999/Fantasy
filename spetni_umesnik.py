import bottle

from main import Uporabnik, Tekma, Napoved, Tabela

# Tukaj se potem začne spet graditi spletna stran

@bottle.get("/")
def prijavna_stran():
    return bottle.template("prijavna_stran.tpl")



# Program moramo na koncu še pognati

bottle.run(reloader=True, debug=True)