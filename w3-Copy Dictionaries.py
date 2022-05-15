#https://www.w3schools.com/python/python_dictionaries_copy.asp
#Python Copy Dictionaries 複製字典
#Copy a Dictionary
#You cannot copy a dictionary simply by typing dict2 = 
# dict1, because: dict2 will only be a reference to dict1,
#  and changes made in dict1 will automatically also be made
#  in dict2.
#你不能僅僅通過鍵入第 dict2 = dict1 來複製字典，因為：dict2 
# 將僅引用 dict1，在 dict1 中做出的更改也會自動在 dict2 中進行。
#There are ways to make a copy, one way is to use the 
# built-in Dictionary method copy().
#有辦法複製，一種方法是使用內建字典方法copy()。
print("----------------------複製字典的方法copy() method")
#Make a copy of a dictionary with the copy() method:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)
print("----------------------複製字典的方法dict() method")
#Another way to make a copy is to use the built-in function dict().
#Make a copy of a dictionary with the dict() function:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict) #用dict化進行複製
print(mydict)
list1 = [22,1.3,"a","b"]
list2 = list(list1)
print(list1) #用list化也可以進行複製
print(list(list1))


