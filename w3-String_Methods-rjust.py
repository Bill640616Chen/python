#https://www.w3schools.com/python/ref_string_rjust.asp
#Python 字串 rjust() Method
#Returns a right justified version of the string
#返回正確的字串正確版本
#返回一個 20 字長， 正確的版本的單詞 「香蕉」：
txt = "banana"
x = txt.rjust(20)
print(x, "is my favorite fruit.")
#注意：結果，香蕉這個詞的左邊實際上有14個空白處。
#              banana is my favorite fruit.
#定義和使用
#該方法將正確對齊字串，使用指定字元（空間預設）作為填充字元。rjust()
#Sytax語法
#string.rjust(length, character)
#參數值
#Parameter(參數)：Description(描述)
#length(長度)：Required(必填). The length of the returned string
#character(字元)：Optional(自選). 
# A character to fill the missing space (to the left of the string). Default is " " (space).
#1個字元去填滿空格(在參數的左邊),預設值為空白格
#使用字母「O」作為填充字元：
txt = "banana"
x = txt.rjust(20, "O")
print(x)
#OOOOOOOOOOOOOObanana