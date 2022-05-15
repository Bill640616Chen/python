#https://www.w3schools.com/python/ref_func_map.asp
#Python map() Function Python map()函數
#Returns the specified iterator with the specified function applied to each item
#返回指定的反覆運算器，其中指定的函數應用於每個專案。
#Calculate the length of each word in the tuple:
#計算元組中每個單詞的長度：
def myfunc(n):
  return len(n)
x = map(myfunc, ('apple', 'banana', 'cherry'))
print(x)
#convert the map into a list, for readability:
print(list(x)) #[5, 6, 6]
#Definition and Usage 定義和用法
#The map() function executes a specified function for each item in an iterable. The item is sent to the function as a parameter.
#map（） 函數為 iterable 中的每個項目執行指定的函數。 專案作為參數發送到函數。
#Syntax 語法
#map(function, iterables)
#Parameter參數：Values值
#Parameter參數：Description描述
#function：Required. The function to execute for each item
#function：必需。 為每個項目執行的函數。
#iterable：Required. A sequence, collection or an iterator 
# object. 
#iterable：必需。 序列、集合或反覆運算器物件。
# You can send as many iterables as you like, 
# just make sure the function has one parameter for each 
# iterable.
#您可以發送任意數量的可反覆運算物件，只需確保該函數的每個可反覆
# 運算物件都有一個參數即可。
#Make new fruits by sending two iterable objects into the function:
print('-------------分隔線------------')
#通過將兩個可反覆運算物件發送到函數中來生成新的水果：
def myfunc(a, b):
  return a + b
x = map(myfunc, ('apple', 'banana', 'cherry'), ('orange', 'lemon', 'pineapple'))
print(x)
#convert the map into a list, for readability:
print(list(x))
#['appleorange', 'bananalemon', 'cherrypineapple']
