# Testataan suttuluokkia

# Kirjastojen ja modulien lataukset
import suttu_luokat

def test_lintu():
    uusi_lintu = suttu_luokat.Lintu('Huuhkaja', 'Bubo Bubo', 'Laji-llalal', 'pikkujyrsijät')
    assert uusi_lintu.nimi == 'Huuhkaja'
    assert uusi_lintu.tietellinen_nimi == 'Bubo Bubo'
    assert uusi_lintu.laji == 'Laji-llalal'
    assert uusi_lintu.ravinto == 'pikkujyrsijät'