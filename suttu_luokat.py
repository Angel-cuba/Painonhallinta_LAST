# Luokka ja olioharjoituksia

# Luokka lintujen tietojen tallennuksen

class Lintu:
    def __init__(self, nimi, tietellinen_nimi, laji, ravinto ):
        self.nimi = nimi
        self.tietellinen_nimi = tietellinen_nimi
        self.laji = laji
        self.ravinto = ravinto

    def aani(self, aani):
        print('Sano', aani)

lintu = Lintu('korppi', 'corvus corax', 'varislinnut', 'raadot')

print(lintu.nimi, 'tieteellisestä nimetään ', lintu.tietellinen_nimi)
lintu.aani('kraak, kraack')

class Kahlaaja(Lintu):
    """docstring for Kahlaaja."""
    def __init__(self, nimi, tietellinen_nimi,laji, ravinto):
        super().__init__(nimi, tietellinen_nimi, laji, ravinto)
        self.laji = laji

kahjaala = Kahlaaja('Kurki', 'Grus Grus', 'sammakot', 'karpaset')
print(kahjaala.nimi, 'sanoo', kahjaala.tietellinen_nimi, 'ja syö', kahjaala.ravinto)
