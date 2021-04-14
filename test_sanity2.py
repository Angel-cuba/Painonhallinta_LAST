# SANITY2-MODULIN TESTIT

# Modulin lataus
import sanity2

# RAJA-ARVOTARKASTUSTEN TESTIT

# Arvo rajojen sisällä, virhekoodi 0, virhesanoma: Arvo OK
def test_rajatarkistus_oikein():
    assert sanity2.rajatarkistus(100, 20, 300) == [0, 'Arvo OK'] 

# Arvo alle alarajan, virhekoodi 1, virhesanoma: Arvo on alle alarajan (20)
def test_rajatarkastus_alle():
    assert sanity2.rajatarkistus(10, 20, 300) == [1,'Arvo on alle alarajan (20)']
    
# Arvo yli ylärajan, virhekoodi 2, virhesanoma: Arvo on yli ylärajanrajan (300)
def test_rajatarkastus_yli():
    assert sanity2.rajatarkistus(350, 20, 300) == [2,'Arvo on yli ylärajan (300)']

# LIUKULUKUMUUNNOSTESTIT

# Syötteenä kokonaisluku, virhekoodi 0, virheilmoitus: Syöte OK, arvo liukulukuna
def test_liukuluku_kokoaisluku():
    assert sanity2.liukuluvuksi('15') == [0, 'Syöte OK', 15.0]

# Syötteenä liukuluku, jossa desimaalipiste
def test_liukuluku_liukuluku_piste():
    assert sanity2.liukuluvuksi('15.0') == [0, 'Syöte OK', 15.0]

# Syötteenä liukuluku, jossa desimaalipilkku: automaattinen korjaus
def test_liukuluku_liukuluku_pilkku():
    assert sanity2.liukuluvuksi('15,0') == [0, 'Syöte OK', 15.0]

# Syötteenä liukuluku, jossa useampi desimaalipiste: virhe
def test_liukuluku_monta_pistetta():
    assert sanity2.liukuluvuksi('15.0.7') == [1, 'Syöte sisältää useita erottimia. Vain yksi arvo on sallittu', 0]

# Syötteenä liukuluku, jossa usempi desimaalipilkku: virhe
def test_liukuluku_monta_pilkkua():
    assert sanity2.liukuluvuksi('15,0,7') == [1, 'Syöte sisältää useita erottimia. Vain yksi arvo on sallittu', 0]

# Syötteessä mukana kirjaimia lopussa: virhe
def test_liukuluku_kirjaimia_lopussa():
    assert sanity2.liukuluvuksi('15.0 kg') == [4, 'Desimaalierottimen jälkeen ylimääräisiä merkkejä: vain numerot ja desimaalipiste on sallittu', 0]

# Syötteessä mukana kirjaimia alussa: virhe
def test_liukuluku_kirjaimia_alussa():
    assert sanity2.liukuluvuksi('paino 15.0') == [3, 'Ennen desimaalierotinta ylimääräisiä merkkejä: vain numerot ja desimaalipiste on sallittu', 0]

# Syöte pelkkää tekstiä, ei numeroita: Virhe
def test_liukuluku_tekstia():
    assert sanity2.liukuluvuksi('sata') == [2, 'Syötteessä ylimäärisiä merkkejä: vain numerot ja desimaalipiste tai pilkku on sallittu', 0]


