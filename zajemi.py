import re
import requests


with open('laliga.html') as f:
    vsebina = f.read()


# Najprej moramo za vsak matchday posebej
vzorec_za_matchday = (
    r'<div class="large-6 columns">.+<div class="box">\n'
    r'.+?<div class="table-header">'
    r'(?P<naslov>.*?)'
    r'</div>'
    r'\w*?\W+?'
    r'<td class="text-right no-border-rechts hauptlink"><span class="tabellenplatz">'
    r'(?P<mestodomače>.*?)'
    r'</span>&nbsp;&nbsp;<a class="vereinprofil_tooltip tooltipstered" id="\d\d\d" href=".+?">'
    r'(?P<domačaekipa>.*?)'
    r'</a></td>'
    )

vzorec_ekipe = (
    r'<a class="vereinprofil_tooltip tooltipstered" '
    r'id="\d*?" '
    r'href=".*?">'
    r'(?P<naslov>.*?)'
    r'</a>'
    )

#def nalozi_stran(url):
#    print(f'Nalagam {url}...')
#    headers = {'Accept-Language': 'de-at;it-it;en-us'}
#    odziv = requests.get(url, headers=headers)
#    return odziv.text
#
#
#vsebina = nalozi_stran('https://www.transfermarkt.com/laliga/gesamtspielplan/wettbewerb/ES1/saison_id/2020')



for zadetek in re.finditer(vzorec_za_matchday,vsebina):
    naslov = zadetek['naslov']
    dekipa = zadetek['domačaekipa']
    print(naslov)
    print(dekipa)


for zadetek in re.finditer(vzorec_ekipe,vsebina):
    dekipa = zadetek['naslov']
    print(dekipa)