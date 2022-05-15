#https://www.w3schools.com/python/ref_func_reversed.asp
#Python reversed() Function Python reversed()函數
#Returns a reversed iterator
#返回反轉的反覆運算器。
#Reverse the sequence of a list, and print each item:
#反轉清單的順序，並列印每個專案：
alph = ["a", "b", "c", "d"]
ralph = reversed(alph)
for x in ralph:
  print(x)
#Definition and Usage 定義和用法
#The reversed() function returns a reversed iterator object.
#reversed（） 函數返回反向的反覆運算器物件。
#Syntax 語法
#reversed(sequence)
#Parameter參數：Values值
#Parameter參數：Description描述
#sequence：Required. Any iterable object
#sequence：必需。 可反覆運算物件。
#Related Pages 相關頁面
#The iter() function returns an iterator object.
#iter（） 函數（返回反覆運算器物件）
#The list.reverse() method reverses a List.
#list.reverse（） 方法（反轉清單）
