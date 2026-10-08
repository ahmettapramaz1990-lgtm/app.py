def selamla(isim: str) -> str:
    if not isim.strip():
        return "Merhaba, dünya!"
    return f"Merhaba, {isim}!"


def yas_grubu(yas: int) -> str:
    if yas < 0:
        raise ValueError("Yaş negatif olamaz.")
    if yas <= 12:
        return "çocuk"
    if yas <= 17:
        return "genç"
    return "yetişkin"
