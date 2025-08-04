mode = input("+,-,*,/ modlarindan birini seciniz:")
sayi1 = int(input("Birinci sayiyi giriniz: "))
sayi2 = int(input("Ikinci sayiyi giriniz: "))

if(mode == "+"):
    print("Sonuc: " + str(sayi1 + sayi2))
elif(mode == "-"):
    print("Sonuc: " + str(sayi1 - sayi2))
elif(mode == "*"):
    print("Sonuc: " + str(sayi1 * sayi2))
elif(mode == "/"):
    if(sayi2 != 0):
        print("Sonuc: " + str(sayi1 / sayi2))
    else:
        print("Bir sayi sifira bolunemez!")
else:
    print("Gecersiz islem secimi!")