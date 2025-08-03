friends = {'John','Michael','Terry','Eric','Graham'}
my_friends = {'Reg','Loretta','Colin','John','Graham'}
cars =['900','420','V70','911','996','V90','911','911','S','328','900']
for friend in friends:
    if friend =="Eric":
        print("Eric is friend")
    if friend == "John":
        print("John is friend")
#iki kümenin birleşimi
print(friends.union(my_friends))
# ortak olanlar
print (friends.intersection(my_friends)) 
#friends kümesinde olup my_friends kümesinde olmayanlar
print (friends.difference(my_friends)) 
#sadece bir kümede olanlar
print(friends.union(my_friends))
#cars listesindeki elemanları yineleneleme olmadan küme haline getir
print(set(cars))