#https://www.w3schools.com/python/ref_string_split.asp
#Python 字串 split() Method
#將字串拆分成清單，其中每個單詞都是清單專案：
txt = "welcome to the jungle"
x = txt.split() #無字元(分離器)代表預設為空白
print(x) #['welcome', 'to', 'the', 'jungle']
#定義和使用
#The method splits a string into a list.split()
#這方法拆分字串為清單
#You can specify the separator, default separator is any whitespace.
#你可以指定分離器(要拆的完元),預設分離器是任何空白
#Note: When maxsplit is specified, the list will contain
# the specified number of elements plus one.
#注意：當最大拆分被指定時，清單將包含指定多加一個元素的數字。
#Syntax語法
#string.rsplit(separator, maxsplit)
#(分離器,最大拆分)
#Parameter Values參數值
#Parameter(參數)：Description(描述)
#separator(分離器)(要拆的字元)：Optional(自選). 
#Specifies the separator to use when splitting the string. By default any whitespace is a separator
#當拆分字串時指定分離器去使用。預設分離器可以是任何的空白
#maxsplit(最大拆分)：Optional(自選). 
#Specifies how many splits to do. Default value is -1, which is "all occurrences"
#指定多少個拆分可以做。預設值是-1,意思是所有事件(最多的拆分)
#使用逗號拆分字串，然後用空間作為分離器：
txt = "hello, my name is Peter, I am 26 years old"
x = txt.split(", ") #把", "字元都拆了
print(x) #['hello', 'my name is Peter', 'I am 26 years old']
#Use a hash(#) character as a separator:
#井字號 
#在電話按鍵上的井字號唸作 pound sign，而現在常在 Facebook 或 Instagram 
#等社群平台上看到的＃則稱作 hashtag 
txt = "apple#banana#cherry#orange"
x = txt.split("#") #把#拆了
print(x) #['apple', 'banana', 'cherry', 'orange']
#要跟上面同樣的輸出結果,有另個的方式
#Split the string into a list with max 2 items:
txt = "apple#banana#cherry#orange"
# setting the maxsplit parameter to 1, will return a list with 2 elements!
x = txt.split("#", 1) #只能拆一個
print(x) #['apple', 'banana#cherry#orange']

txt = "apple#banana#cherry#orange"
x = txt.split("#") #把#拆了
print(x) #['apple', 'banana', 'cherry', 'orange']
#要跟上面同樣的輸出結果,有另二個的方式
print ( txt.split("#",4))
print (txt.split("#",-1))


