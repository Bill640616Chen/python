#https://www.w3schools.com/python/ref_dictionary_update.asp
#Python Dictionary update() Method 字典update()方法
#Updates the dictionary with the specified key-value pairs
#用一對指定的key-value更新字典
#Insert an item to the dictionary:
#setdefault()也可以新增有值無值的鍵值
#dictionary.setdefault(keyname, value)
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.update({"color": "White"})
print(car)
#{'brand': 'Ford', 'model': 'Mustang', 'year': 1964,
# 'color': 'White'}
#Definition and Usage
#The update() method inserts the specified items to the dictionary.
#update()插入指定項目到字典裡,無傳回值
#The specified items can be a dictionary, or an iterable object with key value pairs.
#這指定項目可以是字典或是可迭代物件一定要有一對key-value
#Syntax
#dictionary.update(iterable) (可迭代性)
#Parameter Values
#Parameter：Description
#iterable：A dictionary or an iterable object with key 
# value pairs, that will be inserted to the dictionary
#可迭代性：字典或可迭代物件,都要有一對key-value的型態,都可以
# 被插入到字典裡
print("-------------測試給無傳回值的方法一個變數,還是輸出None")
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.update({"color": "White"})
print(x) #None
print(car)
#{'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 
# 'color': 'White'}
#就算x是None,x右邊的方法還是影響到car的內容,就是in place
#in place是就地取值