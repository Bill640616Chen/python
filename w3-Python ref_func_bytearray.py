#https://www.w3schools.com/python/ref_func_bytearray.asp
#Python bytearray() Function Python bytearray()函數
#Returns an array of bytes
#返回位元組陣列。
#Return an array of 4 bytes:
#傳回 4 個字節的陣列：
x = bytearray(0)
print(x)
#Definition and Usage 定義和用法
#The bytearray() function returns a bytearray object.
#bytearray（） 函數返回 bytearray 物件。
#It can convert objects into bytearray objects, or create empty bytearray object of the specified size.
#它可以將物件轉換為 bytearray 物件，或者創建指定大小的空位元組陣組物件。
#Syntax 語法
#bytearray(x, encoding, error)
#Parameter參數：Values值
#Parameter參數：Description描述
#x：A source to use when creating the bytearray object.
#x：創建 bytearray 物件時使用的資源
#If it is an integer, an empty bytearray object of the specified size will be created.
#如果是整數，則會創建指定大小的空 bytearray 物件。
#x = bytearray(0),bytearray(b'')
#x不能為負數
#If it is a String, make sure you specify the encoding of the source.
#如果是字串，請確保規定了資源的編碼。
#encoding：The encoding of the string
#encoding：encoding 字串的編碼
#error：Specifies what to do if the encoding fails.
#error：規定若編碼失敗要做什麼。
#Related Pages 相關頁面
#The bytes() Function
#bytes（） 函數