# Kysymysmodulin testit

# Modulien ja kirjatojen lataukset
import kysymys

# TODO: tee testit ja kirjoita Wikiin ohjeet syötteen automatisoinnista

# Syöte ok
def test_kysymys_ok(monkeypatch):
    syote = '50'
    monkeypatch.setattr('builtins.input', lambda _: syote)
    assert kysymys.kysy_liukuluku('Painosi (kg)', 20, 350) == 50
    
# Syötteessä tietotyyppivirhe

# Alle alarajan

# Yli ylärajan