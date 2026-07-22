# Demo Package

Bu paket, NovaVision AI platformu konfigürasyon standartlarına uygun olarak oluşturulmuş bir "Demo" paketidir.

## Özellikler (Gereksinimler)

1. **İki Adet Executor İçerir**:
   - `ExecutorOne`: 1 adet girdi (Input) alır, 1 adet çıktı (Output) üretir.
   - `ExecutorTwo`: 2 adet girdi alır, 2 adet çıktı üretir.
2. **Bağımlı Açılır Menü (dependentDropdown)**:
   - Her iki Executor'ın yapılandırma modelinde `DemoDependentDropdown` adlı bir `dependentDropdownlist` alanı bulunur.
   - Bu menünün **OptionA (Method A)** ve **OptionB (Method B)** olmak üzere 2 farklı seçeneği vardır.
   - **OptionA** seçildiğinde, biri `Integer (number)`, diğeri `Boolean (checkbox)` olan iki farklı veri tipinde alan açılır.
   - **OptionB** seçildiğinde, biri `Float (number)`, diğeri `String (textInput)` olan iki farklı veri tipinde alan açılır.

## Görüntü İşleme Yetenekleri (OpenCV)

Bu paket yalnızca mimari kuralları sağlamakla kalmaz, aynı zamanda `cv2` (OpenCV) kütüphanesi ile gerçek görüntü işleme algoritmaları barındırır:
- **ExecutorOne**: Sisteme yüklenen resmi alır ve Siyah-Beyaz (Grayscale) formata çevirerek tek bir çıktı üretir.
- **ExecutorTwo**: Sisteme yüklenen iki farklı resmi alır. Birinci çıktı olarak bu iki resmi harmanlar (Alpha Blending). İkinci çıktı olarak ise iki resim arasındaki piksel farklarını (Absolute Difference) hesaplar.

## Dosya Yapısı

- `src/models/PackageModel.py`: Pydantic kullanılarak tanımlanmış olan yapılandırma şeması (Input/Output ve Dropdown listeleri).
- `src/executors/ExecutorOne.py`: 1 Girdi / 1 Çıktı çalışan, Siyah-Beyaz filtre uygulayan birinci işlemci.
- `src/executors/ExecutorTwo.py`: 2 Girdi / 2 Çıktı çalışan, resim harmanlama ve fark bulma işlemleri yapan ikinci işlemci.

*Bu depo eğitim amacıyla oluşturulmuştur.*
