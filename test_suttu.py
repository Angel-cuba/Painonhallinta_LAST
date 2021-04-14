# Testaan sutty.py:n funktioiden toiminnot

# Modulien ja kirjastojen lataukset
import suttu

# Testataan syötettä
def test_kysy_henkilotiedot(monkeypatch):
    syote = 'mika vainio'

    # Korvataan Pythonin sisäinen input-funktio muuttujalla syöte
    monkeypatch.setattr('builtins.input', lambda _: syote)

    assert suttu.kysy_henkilotiedot() == 'Mika Vainio'

def test_toteamus(capsys):
    suttu.toteamus()
    naytto, virhe = capsys.readouterr()
    assert naytto == 'Kyllä se siitä, herra presidentti\n'
    assert virhe == ''
    