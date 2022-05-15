#https://www.w3schools.com/python/ref_dictionary_pop.asp
#Python Dictionary pop() Method 字典pop()方法
#Remove "model" from the dictionary:
print("-----------------------car.pop(keyname)移除字典裡的鍵值")
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.pop("model") #pop()裡一定要有鍵,不能無參數
print(car)
print("-------print(car.pop(keyname))移除字典裡的鍵後,剩鍵的值")
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car.pop("brand")) #Ford
#沒有賦予變數的屬性,大部分直接放入print裡輸出是None
#因為字典有key與value的關係,所以方法放入print會輸出值
print(car)
#{'model': 'Mustang', 'year': 1964},該鍵值也被移除了

#Definition and Usage
#The pop() method removes the specified item from the dictionary.
#The value of the removed item is the return value of the pop() method, see example below.

print("-----------dictionary.pop(keyname, defaultvalue)實作")
#Syntax
#dictionary.pop(keyname, defaultvalue)
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.pop("111",222)
print(car.pop("111",222)) #222
print(x) #輸出跟上面一樣
#執行這個方法,不存在的key,一樣傳回它的值
#如果不存在的key沒有值,就會顯示error
#Parameter Values
#Parameter：Description
#keyname：Required. The keyname of the item you want to remove
#defaultvalue：Optional. A value to return if the specified key do not exist.
#If this parameter is not specified, and the no item with the specified key is found, an error is raised
