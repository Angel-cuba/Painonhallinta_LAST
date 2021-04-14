# Tiedosto ideoiden testaamiseen

# Testataan merkkijonoa numeroarvo
numeroarvo = '123.45'
print('Tutkittava numeerinen merkkijono on:', numeroarvo)

# Etsitään desimaalipisteen paikka merkkijonosta (.)
pilkunpaikka = numeroarvo.find('.')
print('Pilkku löytyy indeksistä:',pilkunpaikka, 'ja se on', pilkunpaikka + 1, 'merkki vasemmalta')

# Pilkotaan merkkijono pisteen kohdalta
osat = numeroarvo.split('.')

# Selvitetään len-funktiolla montako osaa tuli: 1 pilkku -> 2 osaa. Jos enemmän osia -> virhe
print('Merkkijonon osat ovat' ,osat ,'ja niitä on', len(osat), 'kpl')

# Tietotyyppi on split-metodin ansiosta nyt merkkijonon sijaan lista,
# jossa ei ole isnumeric-metodia. Siksi muutetaan alkiot merkkijonoiksi
kokonaisosa = str(osat[0])
desimaaliosa = str(osat[1])

# Tarkistetaan ovatko merkkijonojen kirjaimet numeroita
print('Kokonaisosa numeerinen', kokonaisosa.isnumeric())
print('Desimaaliosa numeerinen', desimaaliosa.isnumeric())

def kysy_henkilotiedot():
    nimi = input('Nimi: ')
    henkilotiedot = nimi.title()
    return henkilotiedot

def toteamus():
    print('Kyllä se siitä, herra presidentti')

if __name__ == "__main__":

    henkilotiedot = kysy_henkilotiedot()
    print(henkilotiedot)

    toteamus()
