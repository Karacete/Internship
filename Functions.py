def greeting(name, age=28,color='red'):
    #Greets user with 'name' from 'input box' and 'age', if available, default age is used
    print('Hello '  +  name + ', you will be ' + str(age+1) + 
          ' years old next birthday and we hear you like the color ' + color + '!')
    print(f'Hello {name}, you will be {age+1} years old next birthday and we hear you like the color {color}!')

name = input('Enter your name: ')
age = input('Enter your age: ')
color = input('Enter your favorite color: ')
greeting(name.title(), int(age), color.lower())