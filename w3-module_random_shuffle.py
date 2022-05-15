#https://www.w3schools.com/python/ref_random_shuffle.asp
#Random shuffle() Method shuffle()方法
#接受一個序列，並以隨機順序返回此序列。
#Shuffle a list (reorganize the order of the list items):
#隨機排列清單（重新組織清單項的順序）：
''''
import random
mylist = ["apple", "banana", "cherry"]
random.shuffle(mylist)
#print(mylist)
shuffle()
DeprecationWarning: The *random* parameter to shuffle() has been deprecated
該函數將要被棄用
'''
#Definition and Usage 定義和用法
#The shuffle() method takes a sequence, like a list, and reorganize the order of the items.
#該方法採用一個序列（如清單），並重新組織項目的順序。shuffle()
#Note: This method changes the original list, it does not return a new list.
#注意：此方法更改原始清單，它不會返回新清單。
#Syntax 語法
#random.shuffle(sequence, function)
#Parameter：Values 參數值
#Parameter：Description
#sequence：Required. A sequence.
#必填。序列。
#function：Optional. The name of a function that returns a number between 0.0 and 1.0.
#If not specified, the function random() will be used
#自選。返回介於 0.0 和 1.0 之間的數位的函數的名稱。
#如果未指定，將使用函數 random（）
#You can define your own function to weigh or specify the result.
#您可以定義自己的函數來稱重或指定結果。
#If the function returns the same number each time, the result will be in the same order each time:
#如果該函數每次返回相同的數位，則結果每次的順序相同：
import random
def myfunction():
  return 0.1
mylist = ["apple", "banana", "cherry"]
random.shuffle(mylist, myfunction)
print(mylist)

