# ARPIGO
Bu bir RPG oyundur.

## Oyun Sistemi

### Mekanlar

#### Kamp
- Can tamamen dolar
- Envantere bakma
- Eşya Deposu
- Eşya değişimi sadece kampta olur

#### Gezgin Gepetto
- Eşya Alım Satım yeri

# Chapter 1 
#### Kayıp Ormanlar
- Yaratık: Manter
- Bölüm Sonu Canavarı: Poison Ivy
#### Gölge Dağı
- Yaratık: Onixous 
- Bölüm Sonu Canavarı: Shadow Griffin
#### Terkedilmiş Şehir
- Yaratık: Vortex 
- Bölüm Sonu Canavarı: Vel'koz
#### Orion Krallığı
- Yaratık: Yaugai Chief
- Bölüm Sonu Canavarı: Kral Erlang  

### Karakterler

#### Kılıç Ustası 
- Sağlık:80 Zırh:30 Kritik Oranı: 1.7 Saldırı Gücü: 60
- Çifte Vuruş 
#### Okçu 
- Sağlık:70 Zırh:25 Kritik Oranı: 1.6 Saldırı Gücü: 50
- Kritik Vuruş 
#### Büyücü 
- Sağlık:50 Zırh:15 Kritik Oranı: 1 Saldırı Gücü: 100
- Yüksek Hasar
#### Şifacı 
- Sağlık:60 Zırh:40 Kritik Oranı: 1 Saldırı Gücü: 70
- İyileştirici 
#### Suikastçi 
- Sağlık:75 Zırh:30 Kritik Oranı: 2 Saldırı Gücü: 60
- Savuşturma 
#### Tank
- Sağlık:100 Zırh:50 Kritik Oranı: 1.5 Saldırı Gücü: 70
- Savunması Yüksek
#### Warlock
- Sağlık:50 Zırh:25 Kritik Oranı: 1 Saldırı Gücü: 80
- Defansı Yok Sayar

### Yaratıklar
- Manter 
- Sağlık:100 Zırh:40 Kritik Oranı: 1.2 Saldırı Gücü:60
- Poison Ivy
- Sağlık:250 Zırh:60 Kritik Oranı: 1 Saldırı Gücü:100 
- Onixous
- Sağlık:150 Zırh:50 Kritik Oranı: 1.3 Saldırı Gücü:70
- Shadow Griffin
- Sağlık:340 Zırh:80 Kritik Oranı: 1.5 Saldırı Gücü:75
- Vortex
- Sağlık:200 Zırh:40 Kritik Oranı: 1 Saldırı Gücü:80
- Velkoz
- Sağlık:300 Zırh:40 Kritik Oranı:1 Saldırı Gücü:140
- Yaugai Chief
- Sağlık:380 Zırh:60 Kritik Oranı:2 Saldırı Gücü:50
- Kral Erlang
- Sağlık:550 Zırh:60 Kritik Oranı:2 Saldırı Gücü:100

### Eşyalar

#### Silahlar
- Çifte Kılıç
- Yay
- Asa
- Kılıç
- Büyülü Değnek
- Hançer
- Kalkan

#### Kıyafet
- Ağır Zırh | Tank & Kılıç Ustası
- Hafif Zırh | Okçu & Suikastçi 
- Kaftan | Büyücü | Şifacı | Zehirci

### Metotlar

#### show_info()
- Karakterin bilgilerini ekrana yansıtır
#### damage()
- Hedefe verilen hasarı hesaplar
#### fight()
- Karakter ile düşman arasındaki dövüşü yapar
### create_char()
- Karakter oluşturur

# Notlar
- Weapon sınıfı içerisinde attack_speed attr yaz