
# Auto-luokka yliluokka erilaisille autotyypeille

# Ominaisuudet (Field, Property) merkki, malli, vuosimalli, kilometrit, käyttövoima, vaihteistotyyppi, väri ja 

class Auto():    
    # Olionmuodostin eli knstruktori
    def __init__(self, rek, merkki, malli, vm, km, kvoima, vaihteito, vari, paastot):
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

class Henkiloauto(Auto):
        # Henkiloauto
        def __init__(self, rek, merkki, malli, vm, km, kvoima, vaihteito, vari, paastot, istuimet, ovet, korimalli, tavaratila, lisavarausteet):
            super().__init__(rek, merkki, malli, vm, km, kvoima, vaihteito, vari, paastot)
            """ Henkiloauto-objektien konstruktori

            Args:
            istuimet (integer): Penkkien määrän
            ovet (integer): Ovien määrä
            korimalli (string): Mallit: porrasperä, viitoperä, farmari, tiula-auto
            tavaratila (string): Tavaratilan 
            """

            self.istuimet = istuimet
            self.ovet = ovet
            self.korimalli = korimalli
            self.tavaratila = tavaratila        
            self.lisavarausteet = lisavarausteet

if __name__ == '__main__':
    henkiloauto1 = Henkiloauto('ABC-12', 'Ferrary', 'Land', 2020, 354322, 'diesel', 'automaatti', 'punainen', 270, 10, 7, 'tila-auto', 300, ['vakionopeuden säädin', 'peruutuskamera'])
    print('Rekisterinumero: ', henkiloauto1.rek, 'istumapaikkoja', henkiloauto1.istuimet)