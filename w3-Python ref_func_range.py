#https://www.w3schools.com/python/ref_func_range.asp
#Python range() Function Python range()函數
#Returns a sequence of numbers, starting from 0 and increments by 1 (by default)
#返回數位序列，從 0 開始且以 1 為增量（預設地）。
#Create a sequence of numbers from 0 to 6, and print each item in the sequence:
#建立 0 到 5 的數字序列，並列印序列中的每個專案：
x = range(6)
for n in x:
  print(n)
#Definition and Usage 定義和用法
#The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number.
#range（） 函數傳回數位序列，預設從 0 開始，預設以 1 遞增，並以指定的數字結束。
#Syntax 語法
#range(start, stop, step)
#Parameter參數：Values值
#Parameter參數：Description描述
#start：Optional. An integer number specifying at which position to start. Default is 0
#start：可選。 整數，指定從哪個位置開始。 預設為 0。
#stop：Required. An integer number specifying at which position to stop (not included).
#stop：可選。 整數，指定在哪個位置結束。
#step：Optional. An integer number specifying the incrementation. Default is 1
#step：可選的。 整數，指定增量。 預設為 1。
#Create a sequence of numbers from 3 to 5, and print each item in the sequence:
print('-------------分隔線------------')
#建立一個從 3 到 5 的數位序列，並列印該序列中的每個專案：
x = range(3, 6)
for n in x:
  print(n)
#Create a sequence of numbers from 3 to 19, but increment by 2 instead of 1:
print('-------------分隔線------------')
#創建一個從 3 到 19 的數位序列，但增加 2 而不是 1：
x = range(3, 20, 2)
for n in x:
  print(n)

