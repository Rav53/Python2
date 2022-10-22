
# winners = {'Имя':'Коля','Возраст': 18}


# del winners ['Возраст']
# print(winners)
age = input('Введите возраст:')
winners = {'Имя':'Коля'}
winners ['Возраст'] = age

print(winners)
    
    

exit()
x = 2
y = 3

def init(a,b):
    global x
    global y
    x = a
    y = b

def sum():
    return x + y