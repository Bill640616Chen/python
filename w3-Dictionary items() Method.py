#https://www.w3schools.com/python/ref_dictionary_items.asp
#Python Dictionary items() Method 字典items()方法
#Return the dictionary's key-value pairs:
#傳回字典裡一對一對key-value(key-value是就一個item)
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.items()
print(x) 
#dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])
#Definition and Usage
#The items() method returns a view object. The view object 
# contains the key-value pairs of the dictionary, as tuples
# in a list.
#items()方法傳回一個可視物件。這個可視物件包含字典裡的一對一對
#的key-value,作為list中的tuple
#The view object will reflect any changes done to the 
# dictionary, see example below.
#可視物件將反映對字典所做的任何更改，請參閱下面的範例。
#Syntax
#dictionary.items()
#Parameter Values
#No parameters

#When an item in the dictionary changes value, 
# the view object also gets updated:
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
#x.pop("brand") 
x = car.items()
car["year"] = 2018
car[111] = 22 
#我先執行34行,再執行35行,卻不行,因為35行的x資料型態已經改變
#'dict_items' object has no attribute 'pop'
#這個件物沒有pop屬性,所以無法執行
print(x) #修改,新增都可以
#這個可視物件用list中的tuple顯示字典裡的
#一對一對的key-value