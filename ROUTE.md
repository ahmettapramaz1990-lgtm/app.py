# Model seçimi

- **Sonnet 5.5:** Kapsamı belli, iyi tanımlanmış uygulama işleri.
- **Opus 5.5:** Çözülmemiş zor tasarım veya onarım işleri.
- Başlangıç rotası Sonnet 5.5'tir. Rota yalnızca bir kontrol (CHECKS.md) gerekçe sunduğunda değişir; işin "büyük görünmesi" gerekçe değildir.

## Alt ajan dağılımı

Ajan dosyalarındaki `model:` alanıyla uyumlu tutulur.

| Ajan | Model | Neden |
|---|---|---|
| `planner` | haiku | Salt okuyan, hafif planlama |
| `researcher` | haiku | Salt okuyan bilgi toplama |
| `builder` | sonnet | Kod yazar; kalite önemli |
| `reviewer` | sonnet | Kanıta dayalı karar verir |

Bir kontrol başarısız olursa yukarıdaki kural geçerlidir: model yalnızca o kanıtla yükseltilir, ajan dosyaları önce değiştirilmez.
