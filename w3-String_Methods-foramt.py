#https://www.w3schools.com/python/ref_string_format.asp
#Python 字串 format() Method
#將價格插入佔位元元內，價格應為固定點、二位小數格式：
txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))
#For only 49.00 dollars! float代表小數點,2是兩位數
#定義和使用
#該方法格式化指定值，並將其插入字串的佔位元中。format()
#佔位元使用捲曲括弧進行定義： [] 。閱讀更多有關下方佔位元部分的佔位元。
#該方法返回格式化的字串。format()
#語法
#string.format(value1, value2...)
#參數值
#Parameter(參數)：Description(描述)
#value1, value2...：Required(必填). One or more values that should be formatted and inserted in the string.
#The values are either a list of values separated by commas, a key=value list, or a combination of both.
#The values can be of any data type.
#必填。應格式化並插入字串中的一個或多個值。
#這些值要麼是逗號分隔的值清單，要麼是按逗號劃分的key=value(字典)，要麼是兩者兼而有之的值清單。
#這些值可以是任何數據類型。
#佔位元
#佔位元可以使用命名的索引、編號索引，甚至空的佔位元進行識別。{price}{0}{}
#使用不同的佔位元值：
txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
txt2 = "My name is {0}, I'm {1}".format("John",36)
txt3 = "My name is {}, I'm {}".format("John",36)
print (txt1) #My name is John, I'm 36
print (txt2) #My name is John, I'm 36
print (txt3) #My name is John, I'm 36
myorder = "I want {} pieces of item {} for {} dollars.".format(3,567,49.95)
print(myorder) #對照w3-格式字申.py#I want 3 pieces of item 567 for 49.95 dollars.

