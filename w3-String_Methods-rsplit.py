#https://www.w3schools.com/python/ref_string_rsplit.asp
#Python 字串 rsplit() Method
#rsplit()是從字串後面開始往前找
#Split a string into a list, using comma, followed by a space (, ) as the separator:
#使用逗號將字串拆分成清單，然後將空間（，）作為分離器：
txt = "apple, banana, cherry"
x = txt.rsplit(", ")
print(x) #['apple', 'banana', 'cherry']
#定義和使用
#該方法從右側的字串(逗號也算,也當作分離器),開始將字串拆分為清單。rsplit()
#如果沒有指定「最大值」，此方法將返回與split相同的方法。split()
#Note: When maxsplit is specified, the list will contain
# the specified number of elements plus one.
#注意：當最大拆分被指定時，清單將包含指定多加一個元素的數字。
#Syntax語法
#string.rsplit(separator, maxsplit)
#(分離器,最大拆分)
#Parameter Values參數值
#Parameter(參數)：Description(描述)
#separator(分離器)：Optional(自選). 
#Specifies the separator to use when splitting the string. By default any whitespace is a separator
#當拆分字串時指定分離器去使用。預設分離器可以是任何的空白
#maxsplit(最大拆分)：Optional(自選). 
#Specifies how many splits to do. Default value is -1, which is "all occurrences"
#指定多少個拆分可以做。預設值是-1,意思是所有事件(最多的拆分)
#Split the string into a list with maximum 2 items:
#將字串拆分為一個清單裡最多二個項目
txt = "apple, banana, cherry"
# setting the maxsplit parameter to 1, will return a list with 2 elements!
#設定最大清單的參數為1,將會傳回帶有2個元素的清單
x = txt.rsplit(", ", 1)
print(x) #['apple, banana', 'cherry']
#以下測試,進行深度了解
txt = "apple, banana, cherry"
x = txt.rsplit(", ", -1) #-1的意思,找所有的","(要被拆除的字元)
print(x)
#['apple', 'banana', 'cherry']

txt = "apkeee, benena, cherry"
x = txt.rsplit("e", -1) #-1的意思,找所有的"e"(要被拆除的字元)
print(x)
#['apk', '', '', ', b', 'n', 'na, ch', 'rry']
#拆掉一個e,就必給旁邊的元素'',eee,拆第三個時,因為左邊也是要拆的,給一個空白
#所以總只給二個

txt = "apke, benena, cherry"
x = txt.rsplit("e", -1) #-1的意思,找所有的"e"(要被拆除的字元)
print(x)
#['apk', ', b', 'n', 'na, ch', 'rry']要被拆除的字元當作分離器

txt = "apkeee, benena, cherry"
x = txt.rsplit("e", 1) #1的意思,將會傳回帶有2個元素的清單
print(x) #1是決定要拆幾個e
#['apkeee, benena, ch', 'rry']

txt = "apkeee, benena, cherry"
x = txt.rsplit(" ", 1) #1的意思,將會傳回帶有2個元素的清單
print(x) #1是決定要拆幾個空白
#['apkeee, benena,', 'cherry']

txt = "apkeee, benena, cherry"
x = txt.rsplit("  ", 1) #1的意思,將會傳回帶有2個元素的清單
print(x) #字串裡沒有兩個連續空白可以拆,所以清單只有一個字串
#['apkeee, benena, cherry']

txt = "apkeee, benena, cherry"
x = txt.rsplit(" ", 10) 
#最大拆分,是看字串裡有幾個分離器就執行幾個(此例為空白),決定帶有幾個元素
print(x) 
#['apkeee,', 'benena,', 'cherry']