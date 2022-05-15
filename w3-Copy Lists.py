#https://www.w3schools.com/python/python_lists_copy.asp
#Python Copy Lists 複製清單
#Copy a List  複製一個清單
#You cannot copy a list simply by typing list2 = list1, 
# because: list2 will only be a reference to list1, and 
# changes made in list1 will automatically also be made in list2.
#您不能簡單地通過鍵入清單 2 = 清單 1 來複製清單，因為：清單 2 
# 將僅引用清單 1，清單 1 中的更改也會自動在清單 2 中進行。
#There are ways to make a copy, one way is to use the 
# built-in List method copy().
#有複製的方法，一種方法是使用內建清單copy（）方法。
print("----------Make a copy of a list with the copy() method")
#Make a copy of a list with the copy() method:
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist) #['apple', 'banana', 'cherry']
print(thislist.copy()) #['apple', 'banana', 'cherry']

print("-------------另外一種方法做個copy是使用內建的方法list()")
#Another way to make a copy is to use the built-in method list().
#另外一種方法做個copy是使用內建的方法list()
#Make a copy of a list with the list() method:
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist) 
#把物件thislist清單化
print(mylist)           #['apple', 'banana', 'cherry']
print(list(thislist))   #['apple', 'banana', 'cherry']
