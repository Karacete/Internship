toplam_fiyat = 0
icecek_sayisi = 0
while True:
    icecek = input("İçecek seçiniz : \nlatte \namericano \nespresso \ndone\n")
    if icecek == "latte":
        toplam_fiyat += 3.5
        icecek_sayisi += 1
    elif icecek == "americano":
        toplam_fiyat += 3
        icecek_sayisi += 1
    elif icecek == "espresso":
        toplam_fiyat += 2.5
        icecek_sayisi += 1
    elif icecek == "done":
        print(f"Toplam içecek sayısı: {icecek_sayisi} \nToplam fiyat: {toplam_fiyat} TL")
        break
    else:
        print("Geçersiz içecek seçimi. Lütfen tekrar deneyin.")
        continue
