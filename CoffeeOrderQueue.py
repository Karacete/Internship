toplam_fiyat = 0
icecek_sayisi = 0
while True:
    icecek = input("İçecek seçiniz : \nlatte \namericano \nespresso \nexit\n").title()
    if icecek == "Latte":
        toplam_fiyat += 3.5
        icecek_sayisi += 1
    elif icecek == "Americano":
        toplam_fiyat += 3
        icecek_sayisi += 1
    elif icecek == "Espresso":
        toplam_fiyat += 2.5
        icecek_sayisi += 1
    elif icecek == "Exit":
        print(f"Toplam içecek sayısı: {icecek_sayisi} \nToplam fiyat: {toplam_fiyat} TL")
        break
    else:
        print("Geçersiz içecek seçimi. Lütfen tekrar deneyin.")
        continue
