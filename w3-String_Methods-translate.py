#https://www.w3schools.com/python/ref_string_translate.asp
#Python 字串 translate() Method
#Replace any "S" characters with a "P" character:
#用P取代S
#use a dictionary with ascii codes to replace 83 (S) with 80 (P):
#使用字典格式放進ascii代碼去完成P取代S
mydict = {83:  80}
txt = "Hello Sam!"
print(txt.translate(mydict)) #Hello Pam!
#定義和使用
#The method returns a string where some specified characters are replaced with the character described in a dictionary, or in a mapping table.translate()
#該方法返回一個字串，其中某些指定字元被替換為字典中或映射表中描述的字元。
#Use the method to create a mapping table. maketrans()
#使用該方法創建映射表maketrans()
#If a character is not specified in the dictionary/table, the character will not be replaced.
#如果字典/表格中未指定字元，則不會替換字元。
#If you use a dictionary, you must use ascii codes instead of characters.
#如果您使用字典，則必須使用 ascii 代碼而不是字元。
#Syntax語法
#string.translate(table)
#Parameter Values參數值
#Parameter(參數)：Description(描述)
#table(表)：Required(必填). Either a dictionary, or a mapping table describing how to perform the replace
#要麼字典或映射表還是要描述如何替換
#Use a mapping table to replace "S" with "P":
txt = "Hello Sam!"
mytable = txt.maketrans("S", "P")
print(txt.translate(mytable)) #Hello Pam!

#Use a mapping table to replace many characters:
txt = "Hi Sam!"
x = "mSa"
y = "eJo"
mytable = txt.maketrans(x, y) 
print(mytable)
#{109: 101, 83: 74, 97: 111},把xy兩個變數的字串,透過ascii轉換成字典
print(txt.translate(mytable)) #Hi Joe!

#The third parameter in the mapping table describes characters that you want to remove from the string:
txt = "Good night Sam!"
x = "mSa"
y = "eJo"
z = "odnght" ##刪除原始字串的相關字元
mytable = txt.maketrans(x, y, z)
print(txt.translate(mytable)) #G i Joe!

#The same example as above, but using a dictionary instead of a mapping table:
txt = "Good night Sam!"
mydict = {109: 101, 83: 74, 97: 111, 111: None, 100: None, 110: None, 103: None, 104: None, 116: None}
print(txt.translate(mydict))
#G i Joe!
