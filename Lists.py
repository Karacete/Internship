sales_w1 = [7,3,42,19,15,35,9]
sales_w2 = [12,4,26,10,7,28]
sales = []
new_sales = []
new_sale = input ("Yeni gun degerini ekleyiniz: ")
sales_w2.append(int(new_sale))
sales = sales_w1 + sales_w2
profit = 1.5
for sale in sales:
    sale*=profit
    new_sales.append(sale)

print("Toplam satis: "+str(sum(new_sales)))
print("En iyi gun: "+str(max(new_sales)))
print("En kotu gun: "+str(min(new_sales)))    
