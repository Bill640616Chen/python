#https://www.w3schools.com/python/ref_dictionary_keys.asp
#Python Dictionary keys() Method 字典keys()方法
#Return the keys:
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.keys()
print(x) #dict_keys(['brand', 'model', 'year'])
#dict_keys(字典的key)(['brand', 'model', 'year'])用list呈現
#Definition and Usage
#The keys() method returns a view object. The view object contains the keys of the dictionary, as a list.
#keys()方法傳回一個可視物件。這個物件包含字典裡的key,用list呈現
#The view object will reflect any changes done to the dictionary, see example below.
#可視物件將反映對字典所做的任何更改，請參閱下面的範例。
#Syntax
#dictionary.keys()
#Parameter：Values
#No：parameters
#When an item is added in the dictionary, the view object also gets updated:
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.keys() #取字典裡的鍵
print(x)
#print(car.keys()),輸出與print(x)相同
car["color"] = "white"
print(x)
#dict_keys(['brand', 'model', 'year', 'color'])

