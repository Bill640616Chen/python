#https://www.w3schools.com/python/ref_dictionary_get.asp
#Python Dictionary get() Method 字典get()方法
#Get the value of the "model" item:
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.get("model")
print(x) #Mustang

#Definition and Usage
#The get() method returns the value of the item with the specified key.
#get()方法傳回一個項目指定鍵的值
#Syntax
#dictionary.get(keyname, value)
#Parameter Values
#Parameter：Description
#keyname：Required. The keyname of the item you want to
# return the value from
#你想要傳回值從項目的keyname,不管這個項目有沒有在字典裡
#value：Optional. A value to return if the specified key
# does not exist.Default value None
#就算字典裡沒指定的鍵,但是在get(x.y)裡是y有值的,則傳回y值
#如果get(x),只有keyname,沒有y值則傳回預設值None
#如果get(y),只有一個參數都是當作keyname,也是傳回None
#get()裡一定要必填參數
#Try to return the value of an item that do not exist:
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.get("price", 15000)
print(x) #15000