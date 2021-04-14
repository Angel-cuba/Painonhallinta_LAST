# RUTIINEJA TIETOJEN KYSYMISEKSI KÄYTTÄJÄLTÄ

# Kirjastojen ja modulien lataukset
import sanity2

# Funktioden määrittelyt
def kysy_liukuluku(kysymys, alaraja, ylaraja):
    """Kysyy käyttäjä liukuluvun tai kokonaisluvun ja tarkistaa syötteen oikean tietotyypin ja suuruuden

    Args:
        kysymys (str): Käyttäjälle esitettävä kysymys
        alaraja (float): pienin sallittu arvo
        ylaraja (float): suurin sallittu arvo

    Returns:
        float: käyttäjän syöttämä arvo liukulukuna
    """
    # Kysytään käyttäjältä tietoa, kunnes saadaan järkevä arvo
    luku = 0
    tapahtui_virhe = True

    while tapahtui_virhe == True:

        # Esitetään parametrina annettu kysymys ja tallennetaan vastaus (merkkijono) muuttujaan
        vastaus_str = input(kysymys + ' ')

        # Tarkistetaan syötteen järkevyys, virhetiedot ja arvo tallennetaan listamuuttujaan tulokset
        tulokset = sanity2.liukuluvuksi(vastaus_str)

        # Katsotaan onko virhekoodi 0, ja tallennetaan arvo muuttujaan vastaus
        if tulokset[0] == 0:
            vastaus = tulokset[2]

            # Tehdään raja-arvotarkistus, virhetiedot muuttujaan tarkistusviesti
            tarkistusviesti = sanity2.rajatarkistus(vastaus, alaraja, ylaraja)
            
            # Katsotaan onko arvo sallittujen rajojen sisällä tutkimalla virhekoodia
            if tarkistusviesti[0] == 0:
                tapahtui_virhe = False
                luku = vastaus

            else:
                # Jos raja-arvotarkistuksen virhekoodi ei ole 0, tulostetaan virheilmoitus
                print(tarkistusviesti[1])

        # Jos liukulukutarkistuksen virhekoodi ei ole 0, tulostetaan virheilmoitus    
        else:
            print(tulokset[1])

    return luku


# Koodauksen aikaiset tilapaistestit
if __name__ == '__main__':
    vastaus = kysy_liukuluku('Anna luku', 100, 200)
    print(vastaus)
        
