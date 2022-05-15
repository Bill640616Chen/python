#https://www.w3schools.com/python/ref_func_memoryview.asp
#Python memoryview() Function Python memoryview()函數
#Returns a memory view object
#返回記憶體檢視（memory view）物件。
#Create and print a memoryview object:
#建立並列印 memoryview 物件：
x = memoryview(b"Hello")
#一定要有b,b=byte
print(x)
#return the Unicode of the first character
# 返回首個字元的 Unicode
print(x[0])
#return the Unicode of the second character
# 返回第二個字元的 Unicode
print(x[1])
#Definition and Usage 定義和用法
#The memoryview() function returns a memory view object from a specified object.
#memoryview（） 函數從指定物件返回記憶體視圖物件。
#Syntax 語法
#memoryview(obj)
#Parameter參數：Values值
#Parameter參數：Description描述
#obj：A Bytes object or a Bytearray object.
#obj：位元組物件或位元組數位物件。

