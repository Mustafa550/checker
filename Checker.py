# SPECTER-ALLIANCE     by_SpecterZone1

import os
import time
import re
from datetime import datetime

class R:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    CYAN = '\033[96m'
    RESET = '\033[0m'

def clear():
    os.system("clear" if os.name == "posix" else "cls")

def luhn_check(card_number):
    card_number = card_number.replace(" ", "")
    if not card_number.isdigit():
        return False
    total = 0
    reverse_digits = card_number[::-1]
    for i, digit in enumerate(reverse_digits):
        n = int(digit)
        if i % 2 == 1:
            n *= 2
            if n > 9:
                n -= 9
        total += n
    return total % 10 == 0

def detect_card_type(card_number):
    card_number = card_number.replace(" ", "")
    if re.match(r'^4\d{12}(\d{3})?$', card_number):
        return "Visa"
    elif re.match(r'^(5[1-5]\d{14}|2(2[2-9]\d{12}|[3-6]\d{13}|7[01]\d{12}|720\d{12}))$', card_number):
        return "MasterCard"
    elif re.match(r'^3[47]\d{13}$', card_number):
        return "American Express"
    elif re.match(r'^(6011\d{12}|65\d{14}|64[4-9]\d{13}|622(12[6-9]|1[3-9]\d|[2-8]\d{2}|9[01]\d|92[0-5])\d{10})$', card_number):
        return "Discover"
    else:
        return "Bilinmeyen"

def bin_to_bank(card_number):
    bin_bank = {
        "411111": "Chase Bank",
        "550000": "Bank of America",
        "340000": "American Express",
        "601100": "Discover"
    }
    bin6 = card_number.replace(" ", "")[:6]
    return bin_bank.get(bin6, "Bilinmeyen Banka")

def check_length_by_type(card_number, card_type):
    length = len(card_number.replace(" ", ""))
    if card_type == "Visa":
        return length in [13, 16, 19]
    elif card_type == "MasterCard":
        return length == 16
    elif card_type == "American Express":
        return length == 15
    elif card_type == "Discover":
        return length == 16
    else:
        return False

def tarih_check(month, year):
    try:
        if not (month.isdigit() and year.isdigit()):
            return False
        now = datetime.now()
        exp_date = datetime(int(year), int(month), 1)
        return exp_date >= datetime(now.year, now.month, 1)
    except:
        return False

def cvv_check(cvv, card_type):
    if not cvv.isdigit():
        return False
    if card_type == "American Express":
        return len(cvv) == 4
    else:
        return len(cvv) == 3

def kart_kontrol_et():
    clear()
    print(f"{R.CYAN}📋 Kredi Kartı Doğrulama{R.RESET}\n")
    cc = input("💳 Kart numarası (xxxx xxxx xxxx xxxx): ").strip()
    if not re.match(r'^[\d ]+$', cc):
        print(f"{R.RED}❌ Kart numarası sadece rakam ve boşluk içermeli!{R.RESET}")
        input("\nDevam etmek için Enter'a bas...")
        return

    card_type = detect_card_type(cc)
    bank_name = bin_to_bank(cc)

    ay = input("📅 Son kullanma ayı (MM): ").strip()
    yil = input("📅 Son kullanma yılı (YYYY): ").strip()
    cvv = input("🔐 CVV (3 veya 4 haneli): ").strip()

    print(f"\n{R.YELLOW}⏳ Kontrol ediliyor...{R.RESET}\n")
    time.sleep(1)

    valid = True

    if not luhn_check(cc):
        print(f"{R.RED}❌ Kart numarası geçersiz (Luhn hatası){R.RESET}")
        valid = False
    else:
        print(f"{R.GREEN}✅ Kart numarası geçerli (Luhn OK){R.RESET}")

    if not check_length_by_type(cc, card_type):
        print(f"{R.RED}❌ Kart numarası uzunluğu {card_type} için uygun değil{R.RESET}")
        valid = False
    else:
        print(f"{R.GREEN}✅ Kart numarası uzunluğu {card_type} için uygun{R.RESET}")

    if not tarih_check(ay, yil):
        print(f"{R.RED}❌ Son kullanma tarihi geçersiz veya geçmiş{R.RESET}")
        valid = False
    else:
        print(f"{R.GREEN}✅ Son kullanma tarihi geçerli{R.RESET}")

    if not cvv_check(cvv, card_type):
        print(f"{R.RED}❌ CVV geçersiz (Kart tipine göre uygun değil){R.RESET}")
        valid = False
    else:
        print(f"{R.GREEN}✅ CVV geçerli{R.RESET}")

    print(f"\nKart Türü: {card_type}")
    print(f"Banka: {bank_name}")

    if valid:
        print(f"\n{R.GREEN}🎉 Kart BİLGİLERİ GEÇERLİ{R.RESET}")
    else:
        print(f"\n{R.RED}⚠️ Kart bilgileri geçersiz{R.RESET}")

    input("\nDevam etmek için Enter'a bas...")

def menu():
    while True:
        clear()
        print(f"SPECTER-ALLIANCE     by_SpecterZone1\n")
        print(f"""
{R.CYAN}╔════════════════════════════╗
║      🧪 Gelişmiş CC CHECKER 🧪       ║
╠════════════════════════════╣
║ 1. Kart kontrolü yap       ║
║ 2. Çıkış                   ║
╚════════════════════════════╝{R.RESET}
""")
        secim = input("Seçiminiz: ").strip()
        if secim == "1":
            kart_kontrol_et()
        elif secim == "2":
            print("\nÇıkılıyor...\n")
            break
        else:
            print(f"{R.RED}Geçersiz seçim!{R.RESET}")
            time.sleep(1)

if __name__ == "__main__":
    menu()
