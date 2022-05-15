#https://www.w3schools.com/python/ref_func_enumerate.asp
#Python enumerate Function Python enumerate函數
#Takes a collection (e.g. a tuple) and returns it as an enumerate object
#獲取集合（例如元組）並將其作為枚舉物件返回。
#Convert a tuple into an enumerate object:
#將元組轉換為可枚舉物件：
x = ('apple', 'banana', 'cherry')
y = enumerate(x)
print(list(y))
#Definition and Usage 定義和用法
#The enumerate() function takes a collection (e.g. a tuple) and returns it as an enumerate object.
#enumerate（）函數接受一個集合（例如元組），並將其作為枚舉物件返回。
#The enumerate() function adds a counter as the key of the enumerate object.
#enumerate（）函數添加一個計數器作為枚舉對象的鍵。
#Syntax 語法
#enumerate(iterable, start)
#Parameter參數：Values值
#Parameter參數：Description描述
#iterable：An iterable object
#iterable：可反覆運算物件
#start：A Number. Defining the start number of the enumerate object. Default 0
#start：數位。 定義枚舉物件的起始編號。 預設值為 0。
