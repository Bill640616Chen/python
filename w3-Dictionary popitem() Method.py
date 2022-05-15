#https://www.w3schools.com/python/ref_dictionary_popitem.asp
#Python Dictionary popitem() Method 字典popitem()方法
#Remove the last item from the dictionary:
#移除字典裡最後一個項目
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.popitem() #移除字典裡最後一個項目
print(car) #{'brand': 'Ford', 'model': 'Mustang'}
#Definition and Usage
#The popitem() method removes the item that was last 
# inserted into the dictionary. In versions before 3.7, 
# the popitem() method removes a random item.
#現在的版本popitem()是移除字典裡最後一個項目,在版本3.7是隨機移除
#The removed item is the return value of the popitem() method, as a tuple, see example below.
#被popitem()方法移除的項目會傳回值,以tuple顯示,看以下的範例
#Syntax
#dictionary.popitem() (不需要填參數)
#Parameter：Values
#No parameters
#The removed item is the return value of the pop() method:
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car.popitem()) #('year', 1964)
#把car.popitem()放入print裡,會以tuple傳回最後一個的鍵值
#這時候的car變成car = {"brand": "Ford","model": "Mustang"}
x = car.popitem()
print(x) #('model', 'Mustang')
#把car.popitem()方法賦予變數便會傳回值,以tuple顯示
#所以傳回x的值變為是('model', 'Mustang')
#popitem()是移除字典裡最後一個項目的方法
