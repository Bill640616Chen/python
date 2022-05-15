#https://www.w3schools.com/python/ref_dictionary_values.asp
#Python Dictionary values() Method 字典values()方法
#Returns a list of all the values in the dictionary
#以清單的方式傳回字典裡的所有值
#Return the values:
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.values()
print(x)
#dict_values(['Ford', 'Mustang', 1964])

#Definition and Usage
#The values() method returns a view object. The view object contains the values of the dictionary, as a list.
#values()傳回一個可視物件。這個可視物件以list的形式含字典所有的值
#The view object will reflect any changes done to the dictionary, see example below.
#這個可視物品將反映任何字典內容的改變,請下面的範例
#Syntax
#dictionary.values()
#Parameter：Values
#No parameters
#When a values is changed in the dictionary, the view object also gets updated:
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.values()
car["year"] = 2018 #改值
car["color"] = "white" 
#就算字典裡沒有該鍵,因有賦值,還是會進入list裡
print(x)
#dict_values(['Ford', 'Mustang', 2018, 'white'])
#還要測試字典裡的字典