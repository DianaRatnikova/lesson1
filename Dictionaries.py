product = {
    "name": "iPhone 12",
    "stock": 24,
    "price": 65432.1
}
print(product)
print(len(product))


product["memory"] = 64
print(product)
{'name': 'iPhone 12', 'stock': 24, 'price': 65432.1, 'memory': 64}
product["name"] = "iPhone 12 Pro"
print(product)
{'name': 'iPhone 12 Pro', 'stock': 24, 'price': 65432.1, 'memory': 64}

print(product["price"])
print(product["stock"])
#"Безопасное" обращение по ключу
print(product.get("name"))
print(product.get("discount"))

#Значения по-умолчанию
#С помощью .get() можно задать значение, которое мы получим, если ключа в словаре нет.
print(product.get("discount", 0)) #0
print(product.get("country", "CN")) #'CN'

#Удаление элемента
#С помощью ключевого слова del можно удалить элемент по названию ключа. Если такого элемента нет - будет ошибка

del product["stock"]
print(product)
#{'name': 'iPhone 12', 'price': 65432.1}


#Задание
#Создайте словарь:
#{"city": "Москва", "temperature": "20"}
#Выведите на экран значение ключа city
#Уменьшите значение "temperature" на 5
#Выведите на экран весь словарь

mydict={"city": "Москва", "temperature": "20"}
print(mydict["city"])
mydict["temperature"]=int(mydict["temperature"])-5
print(mydict)

#Проверьте, есть ли в словаре ключ country
#Выведите значение по-умолчанию "Россия" для ключа country
#Добавьте в словарь элемент date со значением "27.05.2019"
#Выведите на экран длину словаря

print("About country:", mydict.get("country"))
mydict["country"]="Россия"
print(mydict)
mydict["date"]="27.05.2019"
print(mydict)
print(len(mydict))