# Tietokantamoduli

# Modulien ja kirjastojen lataukset
import sqlite3
from sqlite3.dbapi2 import SQLITE_INSERT

# Luodaan uusi tietokanta projektin hakemistoon
tietokannan_nimi = 'painonhallinta.db'

def luo_tietokanta(tiedosto):
    """Luo tietokannan huom. tiedoston tyyppi po. .db
    Args:
        tiedosto (string): SQL Lite tietokantatiedoston nimi
    """
    yhteys = sqlite3.connect(tiedosto)
    yhteys.close()

def luo_taulut(tiedosto):
    """Luo SQL Lite tietokantaan tarvittavat taulut
    """
    # Muodostetaan yhteys tietokantaan, luodaan kanta tarvittaessa
    yhteys = sqlite3.connect(tiedosto)

    # Luodaan Henkilö-taulu
    yhteys.execute('''CREATE TABLE henkilo
        (henkilo_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        etunimi TEXT NOT NULL,
        sukunimi TEXT NOT NULL,
        sukupuoli INTEGER NOT NULL,
        spaiva DATE NOT NULL);''')

    # Luodaan Mittaukset-taulu, mittaus_id on laskuri
    yhteys.execute('''CREATE TABLE mittaus 
        (mittaus_id INTEGER  PRIMARY KEY AUTOINCREMENT NOT NULL,
        henkilo_id INTEGER NOT NULL,
        pituus REAL NOT NULL,
        paino REAL NOT NULL,
        FOREIGN KEY (henkilo_id)
            REFERENCES henkilo (henkilo_id)
            ON DELETE CASCADE);''')
            
    
    # Suljetaan tietokantayhteys taulujen luonnin jälkeen
    yhteys.close()

# Luodaan testidataa
def lisaa_henkilo(tiedosto, etunimi, sukunimi, sukupuoli, spaiva):
    """Lisätään argumenttina annetun tietokannan henkilo-tauluun uusi tietue
    Args:
        tiedosto (string): tietokantatiedoston nimi
        etunimi (string): Henkilön etunimi
        sukunimi (string): Henkilön sukunimi
        sukupuoli (int): Sukupuolikoodi 1: mies 0: nainen
        spaiva (string): ISO-standardin mukainen päiväys YYYY-MM-DD
    """
    # Rakennetaan SQL-lause argumenttien arvoista
    sql_lause = "INSERT INTO henkilo (etunimi, sukunimi, sukupuoli, spaiva) VALUES (" + "'" + etunimi + "', " + "'" + sukunimi + "', " + str(sukupuoli) + ", " + "'" + spaiva + "');"

    # Luodaan yhteys tietokantaan
    yhteys = sqlite3.connect(tiedosto)

    # Suoritetaan tietueen lisäys SQL-lauseena
    yhteys.execute(sql_lause)

    # Vahvistetaan tapahtuma (transaktio)
    yhteys.commit()

    # Suljetaan yheys
    yhteys.close()

# Funktio, jolla saadaan puolilainausmerkit merkkijonon ympärille
def sql_string(kentta):
    kentta = "'" + kentta +"'"
    return kentta

# Rutiini mittaustietojen syöttämiseksi mittaukset tauluun, huom. mittaus_id laskuri
def lisaa_mittaus(tiedosto, henkilo_id, pituus, paino):
    """Lisää henkilön mittaustiedot mittaus-tauluuun
    Args:
        henkilo_id (integer): henkiön id
        pituus (float): henkilön pituus sentteinä
        paino (float): henkilön paino kiloina
    """
    sql_lause = "INSERT INTO mittaus (henkilo_id, pituus, paino) VALUES (" + str(henkilo_id) + "," + str(pituus) + "," + str(paino) + ");"

     # Luodaan yhteys tietokantaan
    yhteys = sqlite3.connect(tiedosto)

    # Suoritetaan tietueen lisäys SQL-lauseena
    yhteys.execute(sql_lause)

    # Vahvistetaan tapahtuma (transaktio)
    yhteys.commit()

    # Suljetaan yheys
    yhteys.close()

# TODO: luo rutiini tietojen lukemiseksi molemmista tauluita
def lue_kaikki(tiedosto, taulu):
    """[summary]
    Args:
        tiedosto (string): tietokantatiedoston nimi
        taulu (string): taulun nimi
    Returns:
        list: tulosjoukon tietueet
    """
    lista = []
    sql_lause = "SELECT * FROM " + taulu + ";"

     # Luodaan yhteys tietokantaan
    yhteys = sqlite3.connect(tiedosto)

    # Suoritetaan tietueen lisäys SQL-lauseena
    tulosjoukko = yhteys.execute(sql_lause)
    for rivi in tulosjoukko:
        lista.append(rivi)
    
    # Suljetaan yheys
    yhteys.close()

    return lista   

# Paikallinen testaus
if __name__ == "__main__":
    # luo_tietokanta(tietokannan_nimi)
    # luo_taulut(tietokannan_nimi)

    '''
    etunimi = 'Mikko'
    sukunimi = 'Viljanen'
    sukupuoli = 1
    spaiva = '1968-12-03'
    sql_lause = "INSERT INTO henkilo (etunimi, sukunimi, sukupuoli, spaiva) VALUES (" + "'" + etunimi + "', " + "'" + sukunimi + "', " + str(sukupuoli) + ", " + "'" + spaiva + "');"
    print(sql_lause) '''

    # lisaa_henkilo(tietokannan_nimi, 'Mikko', 'Viljanen', 1, '1968-12-03')
    # lisaa_henkilo(tietokannan_nimi, 'Mika', 'Vainio', 1, '1962-06-26')

    '''
    henkilo_id = 1
    pituus = 171
    paino = 74
    sql_lause = "INSERT INTO mittaus (henkilo_id, pituus, paino) VALUES (" + str(henkilo_id) + "," + str(pituus) + "," + str(paino) + ");"
    print(sql_lause) '''

    # lisaa_mittaus(tietokannan_nimi, 2, 171, 74)

    tulosjoukko = lue_kaikki(tietokannan_nimi, 'henkilo')
    print(tulosjoukko)
    # Näkymän testaus: näkymä tehty GUI:ssa, muista tallentaa ja sulkea ennen testaamista!
    tulosjoukko2 = lue_kaikki(tietokannan_nimi, 'henkilon_mittaukset')
    print(tulosjoukko2)