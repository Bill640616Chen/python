#https://www.w3schools.com/python/python_dictionaries_loop.asp
#Python Loop Dictionaries 迴圈字典
#Loop Through a Dictionary 迴圈字典
#You can loop through a dictionary by using a for loop.
#可以使用for迴圈來迴圈字典
#When looping through a dictionary, the return value are the keys of the dictionary, but there are methods to return the values as well.
#當迴圈字典時,傳回值都是字典的鍵而已,但也有方法返回值。
print("---print(x) #傳回鍵,print(thisdict[x]) #[]傳回值的方法")
#Print all key names in the dictionary, one by one:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(x) #傳回鍵
#Print all values in the dictionary, one by one:
for x in thisdict:
  print(thisdict[x]) #[]傳回值的方法
print("------------------可以使用values()方法傳回字典裡的值")
#You can also use the values() method to return values of a dictionary:
#可以使用values()方法傳回字典裡的值
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict.values():
  print(x)
print("---------------------可以使用keys()方法傳回字典裡的鍵")
#You can use the keys() method to return the keys of a dictionary:
#可以使用keys()方法傳回字典裡的鍵
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict.keys():
  print(x)
print("---------------------可以使用item()方法,同時迴圈鍵值")
#Loop through both keys and values, by using the items() method:
#可以使用item()方法,同時迴圈鍵值
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x, y in thisdict.items():
  print(x, y)

