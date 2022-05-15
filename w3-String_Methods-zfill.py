#https://www.w3schools.com/python/ref_string_zfill.asp
#Python 字串 zfill() Method
#Fills the string with a specified number of 0 values at the beginning
#在開始時用指定數量的 0 值填充字串
#Fill the string with zeros until it is 10 characters long:
txt = "50"
x = txt.zfill(10)
print(x) #0000000050,含值,用0填滿到10字元的長度
#定義和使用
#The method adds zeros (0) at the beginning of the string, until it reaches the specified length.zfill()
#該方法在字串的開頭添加零 （0），直到達到指定長度。
#If the value of the len parameter is less than the length of the string, no filling is done.
#如果 len 參數值小於字串長度，則不進行填充。
#Syntax語法
#string.zfill(len)
#Parameter Values參數值
#Parameter(參數)：Description(描述)
#len(長度)：Required(必填). A number specifying the desired length of the string
#指定字串所需長度
#Fill the strings with zeros until they are 10 characters long:
a = "hello"
b = "welcome to the jungle"
c = "10.000"
print(a.zfill(10)) #00000hello
print(b.zfill(10)) #welcome to the jungle
print(c.zfill(10)) #000010.000 小數點也算字元

a = "hello?>1<"
print(a.zfill(10)) #0hello?>1< 符號數字也算