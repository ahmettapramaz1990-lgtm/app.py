# Kontroller

Bir değişikliğin çalıştığını söylemeden önce ilgili kontrolleri çalıştır ve sonucu raporla.

- Testler: `pytest`
- Lint: `ruff check .`

Not: Depoda henüz Python kodu ve test yok. Bu komutlar, kod ve testler eklenip `pytest` ile `ruff` kurulduğunda anlamlı sonuç verir. O zamana kadar bir komut çalışmazsa veya hiç test bulamazsa bunu "doğrulanmadı" olarak raporla, başarılı sayma.
