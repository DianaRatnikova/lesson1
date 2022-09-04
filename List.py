phones = ["iPhone 12", "Samsung Galaxy S21", "Xiaomi Mi11"]
print(phones)
["iPhone 12", "Samsung Galaxy S21", "Xiaomi Mi11"]
count = len(phones)
print(count)

phones = ["iPhone 12", "Samsung Galaxy S21", "Xiaomi Mi11"]
phones.append("iPhone 12")
count = len(phones)
print(count)

print(phones.count("iPhone 12"))
print(phones.count("iPhone 9"))

#Создайте список из чисел 3, 5, 7, 9 и 10.5
#Выведите содержимое списка на экран
#Добавьте в конец списка строку "Python"
#Выведите длину списка на экран

list1=[3,4,7,9,10.5]
print(list1)
list1.append("Python")
print(list1)
print(len(list1))

#Выведите на экран начальный элемент списка
#Выведите на экран последний элемент списка
#Напечатайте элементы списка со второго по четвертый включительно
#Удалите из списка строку "Python"

print(list1[0])
print(list1[-1])
print(list1[1:4])
list1.remove("Python")
print(list1)