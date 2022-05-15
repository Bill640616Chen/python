#https://www.w3schools.com/python/ref_func_bytes.asp
#Python bytes() Function Python bytes()函數
#Returns a bytes object 返回位元組物件。
#Return an array of 4 bytes:
#傳回 4 個字節的陣列：
x = bytes(0)
print(x)
#Definition and Usage 定義和用法
#The bytes() function returns a bytes object.
#bytes()函數傳回位元組物件。
#It can convert objects into bytes objects, or create empty bytes object of the specified size.
#它可以將物件轉換為位元組物件，或創建指定大小的空位元組物件。
#The difference between bytes() and bytearray() is that bytes() returns an object that cannot be modified, and bytearray() returns an object that can be modified.
#bytes()和 bytearray()之間的區別在於，bytes()傳回一個不能修改的物件，而 bytearray()傳回一個可以修改的物件。
#Syntax 語法
#bytes(x, encoding, error)
#Parameter參數：Values值
#Parameter參數：Description描述
#x：A source to use when creating the bytes object.
#x：創建 bytearray 物件時使用的資源
#If it is an integer, an empty bytes object of the specified size will be created.
#如果是整數，則會創建指定大小的空 bytearray 物件。
#x = bytearray(0),b''
#x不能為負數
#If it is a String, make sure you specify the encoding of the source.
#如果是字串，請確保規定了資源的編碼。
#encoding：The encoding of the string
#encoding：字串的編碼
#error：Specifies what to do if the encoding fails.
#error：規定若編碼失敗要做什麼。
#Related Pages 相關頁面
#The bytearray() Function
#bytearray()函數