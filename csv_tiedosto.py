# Modulin avulla luodaan, luetaan ja kirjoitetaan CSV-tiedostoja

# Kirjastojen ja modulien lataukset
import csv

# Luodaan oma CSV-määritys (murre, dialect) suomalaiselle Excelille
csv.register_dialect('fi_excel', delimiter = ';', quotechar = '"')

# Käytetään omaa CSV-määritystä 
def luo_otsikot_fi(tiedosto):
    with open(tiedosto, 'w', newline = '') as fi_tiedosto:
        csv_otsikoija = csv.writer(fi_tiedosto, dialect = 'fi_excel')
        csv_otsikoija.writerow(['Etunimi', 'Sukunimi', 'Palkka'])

# Luodaan otsikot CSV-tiedostoon
def luo_otsikot(tiedosto):
    """Luodaan CSV-tiedostoon tarvittavat sarakeotsikot

    Args:
        tiedosto (string): muokattavan tiedoston nimi
    """
# Määritellään csv-tiedosto, erotin, tekstitunniste ja rivinvaihtomääritys    
    with open(tiedosto, 'w', newline = '') as datatiedosto: # newline = '' estää tyhjien rivien syntymisen
        csv_kirjoittaja = csv.writer(datatiedosto, delimiter = ';', quotechar = '"', )
        csv_kirjoittaja.writerow(['Etunimi', 'Sukunimi', 'Pituus', 'Paino', 'Ikä', 'Sukupuoli', 'Tavoitepaino'])

# Lisätään rivejä CSV-tiedostoon
def lisaa_tiedot(tiedosto, etunimi, sukunimi, pituus, paino, ika, sukupuoli, tavoitepaino):
    """Lisää CSV-tiedostoon uuden datarivin

    Args:
        tiedosto (string): CSV-tiedoston nimi
        etunimi (string): Etunimi
        sukunimi (string): Sukunimi
        pituus (string): Pituus (cm)
        paino (string): Paino (kg)
        ika (string): Ikä
        sukupuoli (string): Mies 1, nainen 0
        tavoitepaino (string): Tavoitteena oleva paino (kg)
    """
    with open(tiedosto, 'a', newline = '') as datatiedosto: # Huom. tyhjien rivien esto newline = ''
        csv_kirjoittaja = csv.writer(datatiedosto, delimiter = ';', quotechar = '"')
        csv_kirjoittaja.writerow([etunimi, sukunimi, pituus, paino, ika, sukupuoli, tavoitepaino])
    
# Luetaan tiedot luetteloon ja palautetaan luettelo
def lue_rivit(tiedosto):
    """Palauttaa CSV-tiedoston sisällön listana

    Args:
        tiedosto (string): Palautettavan CSV-tiedoston nimi

    Returns:
        list: lista otsikoista ja arvoista
    """
    lista = [] # Tarvitaan tulosten saamiseksi ulos with-rakenteesta
    with open(tiedosto, 'r') as datatiedosto:
        csv_lukija = csv.reader(datatiedosto, delimiter = ';', quotechar = '"')
        for rivi in csv_lukija:
            lista.append(rivi) # Lisätään rivi listaan
    return lista

# Luetaan CSV-tiedosto avain-arvo-pareiksi listaan
def lue_sanakirjaan(tiedosto):
    sanakirja = [] # Lista riveistä avain-arvo-pareina
    with open(tiedosto, 'r') as datatiedosto:
        csv_lukija = csv.DictReader(datatiedosto, delimiter = ';', quotechar = '"')
        for rivi in csv_lukija:
            sanakirja.append(rivi)
    return sanakirja


if __name__ == "__main__":
    # Luodaan otsikot (kommentoi ensimmäisen käytön jälkeen)
    luo_otsikot('bmidata.csv')

    # Lisätään testimielessä rivejä
    lisaa_tiedot('bmidata.csv', 'Mika', 'Vainio', '171', '72', '59','1', '70')
    lisaa_tiedot('bmidata.csv', 'Mikko', 'Viljanen', '176', '80', '50','1', '75')

    # Luetaan tiedot
    with open('bmidata.csv', 'r') as testiluku:
        print(testiluku.read())

     # Luetaan tiedot listaan ja käydään se riveittäin läpi
    print(lue_rivit('bmidata.csv'))

    # Luetaan tiedot sanakirjaan ja käydään se riveittäin läpi
    print(lue_sanakirjaan('bmidata.csv'))
    
    # Suomalaisten asetusten testaus
    luo_otsikot_fi('suomalainen.csv')

    with open('suomalainen.csv', 'r') as testiluku:
        print(testiluku.read())   
    