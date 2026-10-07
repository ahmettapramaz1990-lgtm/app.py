from app import selamla


def test_normal_isim():
    assert selamla("Ayşe") == "Merhaba, Ayşe!"


def test_bos_string():
    assert selamla("") == "Merhaba, dünya!"


def test_yalnizca_bosluk():
    assert selamla("   ") == "Merhaba, dünya!"
    assert selamla("\t\n") == "Merhaba, dünya!"
