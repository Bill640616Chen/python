#https://www.w3schools.com/python/python_tuples_loop.asp
#Python Loop Tuples Tuple迴圈
#Loop Through a Tuple 迴圈通過tuple
#You can loop through the tuple items by using a for loop.
print("-----------------------靠著使用for迴圈，loop tuple")
#你可以用loop通過tuple項目，靠著使用for迴圈
#Iterate through the items and print the values:
#通過項目和列印值來可迭代(可重覆運算)
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)
#apple
#banana
#cherry
#Learn more about for loops in our Python For Loops Chapter.

print("-------------Loop Through the Index Numbers迴圈瀏覽索引編號")
#Loop Through the Index Numbers迴圈瀏覽索引編號
#You can also loop through the tuple items by referring to their index number.
#您也可以通過引用它們的索引號來循環瀏覽這些項目。
#Use the range() and len() functions to create a suitable iterable.
#使用範圍 （） 和 len （） 功能創建合適的可迭代。
#Print all items by referring to their index number:
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)): 
#len計算tuple裡有幾個項目,得出range(3)
  print(thistuple[i])
#apple
#banana
#cherry

print("--------------------------Using a While Loop 使用while迴圈")
#Using a While Loop 使用while迴圈
#You can loop through the list items by using a while loop.
#你可以使用while迴圈來迴圈清單的項目
#Use the len() function to determine the length of the tuple, 
# then start at 0 and loop your way through the tuple items 
# by refering to their indexes.
#使用 len（） 功能確定 Tuple 的長度，然後從 0 開始，通過參考其索引來
# 循環瀏覽tuple項貝。
#Remember to increase the index by 1 after each iteration.
#請記住，每次反覆運算後將索引增加 1。
#Print all items, using a while loop to go through all the index numbers:
thistuple = ("apple", "banana", "cherry")
i = 0 #i是索引值變數
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1 #每次反覆運算後將索引增加 1
#apple
#banana
#cherry