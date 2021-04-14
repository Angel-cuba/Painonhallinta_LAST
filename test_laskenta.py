# Modulin laskenta.py testit

# Modulien ja kirjastojen lataukset
import laskenta

# Ensimmäinen testi lasketaan painoindeksi ja verrataan tulosta ennalta laskettuun arvoon, huom sentit
def test_painoideksi():
    assert round(laskenta.bmi(74, 171), 2) == 25.31 # huom. pyöristys

# Aikuisen naisen rasvaprosentti, kun bmi on 25 ja ikä 40
def test_aikuisen_rasvaprosentti_nainen():
    assert round(laskenta.rasvaprosentti(25,40, 0), 1) == 33.8 # huom. pyöristys

# Aikuisen miehen rasvaprosentti, kun bmi on 25 ja ikä 40
def test_aikuisen_rasvaprosentti_mies():
    assert round(laskenta.rasvaprosentti(25,40, 1), 1) == 23.0 # huom. pyöristys
    
# Tytön rasvaprosentti, kun bmi on 25 ja ika 16
def test_lapsen_rasvaprosentti_tytto():
    assert round(laskenta.rasvaprosentti(25,16, 0), 1) == 27.9 # huom. pyöristys    

# Pojan rasvaprosentti, kun bmi on 25 ja ika 16
def test_lapsen_rasvaprosentti_poika():
    assert round(laskenta.rasvaprosentti(25,16, 1), 1) == 24.3 # huom. pyöristys