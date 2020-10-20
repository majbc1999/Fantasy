import json

def dodaj_uporabnika(username, password):
    data = {
        'username': username,
        'password': password}
    with open('data.txt', 'a') as outfile:
        json.dump(data, outfile)
        outfile.write('\n')

def preveri(username):
    with open('data.txt') as datoteka:
        for vrstica in datoteka:
            json_file = vrstica.rstrip()
            data = json.loads(json_file)
            if data["username"]==username:
                return False
        return True