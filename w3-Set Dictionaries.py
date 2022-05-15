#https://www.w3schools.com/python/python_dictionaries.asp
#Python Dictionaries 字典
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
#Dictionary
#Dictionaries are used to store data values in key:value pairs.
#字典都用來了把值資料在key:value(一對)
#A dictionary is a collection which is ordered*, changeable and does not allow duplicates.
#字典是一種收集,是有序的,可改變的,但不允許重複的key:value
#As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
#在版本3.7,字典是有序的,在版本3.6,字典是無序的
#Dictionaries are written with curly brackets, and have keys and values:
#字典的書寫方式是{},而且有key:value
#Create and print a dictionary:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
#{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
#Dictionary Items
#Dictionary items are ordered, changeable, and does not allow duplicates.
#字典是有序的,可改變的,但不允許重複的key:value
#Dictionary items are presented in key:value pairs, and can be referred to by using the key name.
#字典的項目都都存在於key:value一對,並可以靠著使用key name被引用
#Print the "brand" value of the dictionary:
#key:value(鍵:值)
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"]) #Ford

#Ordered or Unordered? 有序或無序
#As of Python version 3.7, dictionaries are ordered.
#  In Python 3.6 and earlier, dictionaries are unordered.
#版本3.7,字典是有序的,在版序3.6,字典是無序的
#When we say that dictionaries are ordered, it means that 
# the items have a defined order, and that order
# will not change.
#當我們說字典是有序的,這個意思是項目有定義的順序,
# 而且這個順序將不會被改變
#Unordered means that the items does not have a defined 
# order, you cannot refer to an item by using an index.
#無序的意思是項目沒有一個定義的順序,你不能引用靠使用索引的項目

#Changeable 可改變的
#Dictionaries are changeable, meaning that we can change,
# add or remove items after the dictionary has been created.
#字典都是可以改變的,意思是在字典被創建後我們可以改變,增加或移除項目

#Duplicates Not Allowed 重複是不被允許的
#Dictionaries cannot have two items with the same key:
#字典不能有兩個相同key的項目

#Duplicate values will overwrite existing values:
#重複的value將會覆寫已經存在的value
#覆寫規則：相同鍵時,最後一個值才會輸出
thisdict = {
  "brand": "Ford",
  "brand": "BMW",
  "brand": "Toyota",
  "model": "Mustang",
  "year": 2020,
  "year": 2001,
  "model": "ang",
}
print(thisdict)
#{'brand': 'Ford', 'model': 'Mustang', 'year': 2020}