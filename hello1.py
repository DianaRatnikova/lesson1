user_name=input('Как Вас зовут? ')
print("Привет, ", user_name)
user = 'Миша'
b = f'Привет {user}!'
print(b)

a = 'Привет'
b = 'мир'
c = 2
d = f'{a} {b}{c}!'
print(d)  # Привет мир2!
print(len(d))

a = 'Привет'.upper()
print(a) # ПРИВЕТ
b = 'Привет'.lower()
print(b)  # привет
c = 'python'.capitalize()
print(c)  # Python