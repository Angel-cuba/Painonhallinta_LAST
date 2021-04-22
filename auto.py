
# Auto-luokka yliluokka erilaisille autotyypeille

# Ominaisuudet (Field, Property) merkki, malli, vuosimalli, kilometrit, käyttövoima, vaihteistotyyppi, väri ja 

class Auto():    
    # Olionmuodostin eli knstruktori
    def __init__(self, rek, merkki, malli, vm, km, kvoima, vaihteito, vari, paastot, s_tilavuus, hinta):
        """Auto-luokka mallinen auto-olioille yliluokka eri autotyyppeille

        Args:
            rek (string): Auton rekisterinumero esim. ABC-123
            merkki (string): Auton valmistaja
            malli (string): Tyyppimerkintä
            vm (integer): Vuosimalli
            km (integer): Ajetut kilometrit
            kvoima (string): Käyttövoima: diesel, bensiini, hybridi, sähkö, kaasu, vety
            vaihteito (string): Vaihteiston tyyppi: käsi, automaatti
            vari (string): Auton pääväri
            paasto (int): Hiilidioksidipäästö g/km
            s_tilavuus (float): Sylinteritilavuus
            hinta (float): Auton myytihinta Eur
        """     
        self.rek = rek
        self.merkki = merkki
        self.malli = malli
        self.vm = vm
        self.km = km
        self.kvoima = kvoima
        self.vaihteito = vaihteito
        self.vari = vari
        self.paasto = paastot
        self.s_tilavuus = s_tilavuus
        self.hinta = hinta

    # Metodi jäljella olevien kilometrien arviointiin
    def km_jaljella(self):
        kilometreja = (self.s_tilavuus * 100000) - self.km
        return kilometreja 

    # Metodi jäljella olien kilometrien kustannusten arviointiin
    def km_jaljella_hinta(self):
        km_hinta = self.hinta / (self.s_tilavuus * 100000 - self.km)  
        return km_hinta

    # Metodi, jolla voi laskea korjatun jäljella olevan kilometrimäärän
    def korjatut_kilometrit(self, kerroin):
        """[summary]

        Args:
            kerroin (float): Korjauskerroin hybrideillä 1.5, dieseleillä 2

        Returns:
            float: Arvio jäljella 
        """
        jaljella_km = (self.s_tilavuus* kerroin * 100000 -self.km) 
        return jaljella_km

    # Staattinen metodi jäjjellä olevien kilometrien laskemiseen
    @staticmethod
    def arvio_kilometrit(sylinteritilavuus, mittarilukema, korjauskerroin):
        """Laskee arvion jäjjellä olevista ajokilometeistä

        Args:
            sylinteritilavuus (float): Sylinteritilavuus litroina
            mittarilukema (integer): Matkamittarin lukema
            korjauskerroin (float): Korjauskerroin Diesel 2.0, Hybridi 1.35

        Returns:
            float: Arvio jäljella olevista ajokilometreista
        """
        jaljella_km = sylinteritilavuus * korjauskerroin * 100000 - mittarilukema
        return jaljella_km


class Henkiloauto(Auto):
        # Henkiloauto
        def __init__(self, rek, merkki, malli, vm, km, kvoima, vaihteito, vari, paastot, s_tilavuus, hinta, istuimet, ovet, korimalli, tavaratila, lisavarausteet):
            super().__init__(rek, merkki, malli, vm, km, kvoima, vaihteito, vari, paastot, s_tilavuus, hinta)
            """ Henkiloauto-objektien konstruktori

            Args:
            istuimet (integer): Penkkien määrän
            ovet (integer): Ovien määrä
            korimalli (string): Mallit: porrasperä, viitoperä, farmari, tila-auto
            tavaratila (string): Tavaratilan 
            """

            self.istuimet = istuimet
            self.ovet = ovet
            self.korimalli = korimalli
            self.tavaratila = tavaratila        
            self.lisavarausteet = lisavarausteet

if __name__ == '__main__':
    henkiloauto1 = Henkiloauto('ABC-12', 'Ferrary', 'Land', 2020, 354322, 'diesel', 'automaatti', 'punainen', 270, 2.8, 4000, 7, 5, 'tila-auto', 300, ['vakionopeuden säädin', 'peruutuskamera'])
    print('Rekisterinumero: ', henkiloauto1.rek, 'istumapaikkoja', henkiloauto1.istuimet)

# Lasketaan jäljelläolevien kilometrien hinta

print('Jäljellä olevien kilometrien hinta on', henkiloauto1.km_jaljella())

print('Jäljellä olevien kilometrien hinta on', henkiloauto1.km_jaljella_hinta())

print('Korjatut kilometrit on:', henkiloauto1.korjatut_kilometrit(2))

kilometreja_jaljella = Auto.arvio_kilometrit(2.8, 364800, 2)
print('Laskettu staattisella metodilla:', kilometreja_jaljella)