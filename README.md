CC Checker - Gelişmiş Kredi Kartı Doğrulama Scripti

Yazar: Mustafa550
Proje: checker
Sürüm: 1.0


---

Açıklama

Bu Python scripti, kullanıcıdan alınan kredi kartı bilgilerini gerçekçi ve basit yöntemlerle doğrular.
Kart numarasının geçerliliği, türü, son kullanma tarihi ve CVV uygunluğu kontrol edilir.
Termux ve Linux terminal ortamlarında çalışmak üzere uygundur.


---

Gereksinimler

Android için Termux uygulaması veya bilgisayarda Linux/MacOS terminali

Python 3 yüklü olmalı (Termux’ta kurulum talimatı aşağıda)



---

Kurulum & Çalıştırma Adımları

1. Termux için Python Kurulumu (Eğer Python yüklü değilse)

Termux’u aç ve şu komutları sırayla yaz:

pkg update && pkg upgrade -y
pkg install python -y

2. Git kur (eğer yoksa)

pkg install git -y

3. Repoyu klonla

git clone https://github.com/Mustafa550/checker.git

4. Proje dizinine gir

cd checker

5. Python scriptini çalıştır

python3 checker.py
