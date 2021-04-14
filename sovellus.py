# Tämä on painonhallintasovelluksen pääohjelma

# Kirjastojen ja modulien käyttöönotot
import laskenta
import kysymys
import luokat

# Varsinaisen pääohjelman alku

# Työsilmukka, ikuinen silmukka, jossa on poistumistoiminto (ehto True on aina voimassa)
uusi = 'K'
lista = []
while True:

    # Tehdään kysymykset modulin kysymys.py funktiota käyttämällä
    etunimi = input('Etunimi: ')
    sukunimi = input('Sukunimi: ')
    paino = kysymys.kysy_liukuluku('Paino (kg)', 30, 350)
    pituus = kysymys.kysy_liukuluku('Pituus (cm)', 100, 300)
    ika = kysymys.kysy_liukuluku('Ikä (v)', 3, 125)
    sukupuoli = kysymys.kysy_liukuluku('Sukupuoli nainen: 0, mies: 1', 0, 1)
    

    # Tehtävä 2
    if ika >= 18:
        tavoitepaino = kysymys.kysy_liukuluku('Tavoitepaino (kg)', 30, 350)
        aikuinen = luokat.Aikuinen(etunimi, sukunimi, pituus, paino, ika, sukupuoli, tavoitepaino)
        lista.append(aikuinen)
    else:
        lapsi = luokat.Lapsi(etunimi, sukunimi, pituus, paino, ika, sukupuoli)
        lista.append(lapsi)
   
    # Poistuminen ikuisesta silmukasta
    uusi = input('Lasketaanko uuden henkilön rasvaprosentti? (K/e)')
    if uusi.upper() == 'E':
        break

# Ikuisen silmukan jälkeen tulostetaan tietoja

# Otetaan listan ensimmäinen olio pois ja tulostetaan sen tietoja       
eka = lista.pop(0)
print(eka.etunimi, eka.sukunimi, eka.rasvaprosentti())

# Otetaan listan viimeinen olio pois ja tulostetaan sen tietoja
viimeinen = lista.pop()
print(viimeinen.etunimi, viimeinen.sukunimi, viimeinen.rasvaprosentti())