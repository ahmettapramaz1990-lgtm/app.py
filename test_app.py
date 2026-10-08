import pytest

from app import selamla, yas_grubu


def test_normal_isim():
    assert selamla("Ayşe") == "Merhaba, Ayşe!"


def test_bos_string():
    assert selamla("") == "Merhaba, dünya!"


def test_yalnizca_bosluk():
    assert selamla("   ") == "Merhaba, dünya!"
    assert selamla("\t\n") == "Merhaba, dünya!"


def test_yas_grubu_cocuk():
    assert yas_grubu(0) == "çocuk"
    assert yas_grubu(12) == "çocuk"


def test_yas_grubu_genc():
    assert yas_grubu(13) == "genç"
    assert yas_grubu(17) == "genç"


def test_yas_grubu_yetiskin():
    assert yas_grubu(18) == "yetişkin"


def test_yas_grubu_negatif():
    with pytest.raises(ValueError):
        yas_grubu(-1)
