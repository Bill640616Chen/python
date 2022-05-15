#https://www.w3schools.com/python/ref_dictionary_popitem.asp
#Python Dictionary setdefault() Method 字典setdefault()方法
#Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
#傳回指定鍵的值。如果鍵不存在，插入一個鍵，給它一個指定值
#Get the value of the "model" item:
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.setdefault("model", "Bronco")
print(x)
#Definition and Usage
#The setdefault() method returns the value of the item with the specified key.
#setdefault()傳回指定key的值
#If the key does not exist, insert the key, with the specified value, see example below
#如果該key不存在，插入一個有指定值的key
#Syntax
#dictionary.setdefault(keyname, value)
#Parameter Values
#Parameter：Description
#keyname：Required. The keyname of the item you want to return the value from
#value：Optional.
#If the key exist, this parameter has no effect.
#如果該key存在,參數是沒效果
#If the key does not exist, this value becomes the key's value
#如果該key不存在，該值就會成為key的值
#Default value None 預設值為None
#dictionary.setdefault(keyname)沒把值給鍵,輸出為None
#dictionary.setdefault(key,value)傳回值(None也可)
#,也等於為字典新增鍵值
#Get the value of the "color" item, if the "color" item does not exist, insert "color" with the value "white":
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.setdefault("color", "white")
print(x) #white
print(car.setdefault(11, 22)) #22
print(car.setdefault("year",1965)) #1964
print(car.setdefault("year")) #1964
print(car.setdefault(55)) #None
print(car)
#{'brand': 'Ford', 'model': 'Mustang', 'year': 1964,
# 'color': 'white', 11: 22, 55: None}
print("---------------------------------方法不給變數測試")
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.setdefault("color", "white")
print(car)
#新增新的鍵值到字典中