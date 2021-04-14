# Tiedostojen luomisen ja käyttämisen kokeiluja

# Kirjastojen ja modulien lataukset
import os
import csv

# Luodaan tiedosto projektin juurihakemistoon
""" tiedosto = open('data.txt', 'x')
tiedosto.close() """

# Lisätään edelliseen tiedostoon uusi rivi
tiedosto = open('data.txt', 'a')
tiedosto.write('# Tässä tiedostossa on painoindeksitietoja\n')
tiedosto.close()

# Luetaan tiedosto
tiedosto = open('data.txt', 'r')
print(tiedosto.read())
tiedosto.close()

# Kirjoitetaan tiedostoon lisää rivejä käyttäen with open() -rakennetta
with open('data.txt', 'a') as tallentaja:
    tallentaja.writelines('Etunimi;Sukunimi;Pituus;Paino\n')
    tallentaja.writelines('Mika;Vainio;171;72\n')
    tallentaja.writelines('Mikko;Viljanen;176;82\n')

# Luetaan tiedot with open()-rakenteen avulla
with open('data.txt', 'r') as lukija:
    print(lukija.read())

