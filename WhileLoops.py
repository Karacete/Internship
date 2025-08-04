sayi = 63
hak = 7
kullanilan_hak = 0
while kullanilan_hak != hak:
    tahmin = int(input('Lütfen 0-100 tahmininizi giriniz: '))
    kullanilan_hak += 1
    if tahmin < sayi:
        print(f'Tahmininiz çok düşük ve {hak - kullanilan_hak} hakkınız kaldı')
    elif tahmin > sayi:
        print(f'Tahmininiz çok yüksek ve {hak - kullanilan_hak} hakkınız kaldı')
    else:
        print('Tebrikler, doğru tahmin ettiniz!')
        break