toplam_sure = float(input("Toplam yaris suresini yaziniz (saniye): "))
pit_stop = int(input("Kaç pit stop yapilmistir? "))
pit_stop_sure = float(input ("Ortalama pit stop suresi kaç saniyedir? "))
toplam_pit_stop = pit_stop * pit_stop_sure
yuzde = (toplam_pit_stop/toplam_sure) * 100
print ("Toplam pit stop suresi :" + str(pit_stop_sure))
print ("Pitlerde gecen surenin yuzdesi: " + str(round(yuzde,2)))
if(yuzde>5.0):
    print("Yeni bir pit ekibine ihtiyaciniz var.")