csv = 'Eric,John,Michael,Terry,Graham:TerryG;Brian'
friends_list= []
csv = ','.join(csv.split(':'))
csv = ','.join(csv.split(';'))
for friend in csv.split(','):
    friends_list.append(friend)
print(friends_list)