#https://www.w3schools.com/python/ref_string_join.asp
#Python 字串 join() Method
#Join all items in a tuple into a string, using a hash character as separator:
#將所有項目加入至元組陣列中的字申,使用一個散列字元當作分離器
from typing import get_args


myTuple = ("John", "Peter", "Vicky")
x = "#".join(myTuple) #"#"為散列字元當作分離器
print(x) #John#Peter#Vicky
#定義和使用
#該方法將所有專案以可轉為一體，並將它們連接成一個字串。join()
#字串必須指定為分離器。
#語法
#https://www.runoob.com/python/att-string-join.html
#此網站的解釋易懂
#string.join(sequence) #sequence要连接的元素序列
#參數值
#Parameter(參數)：Description(描述)
#sequence(要连接的元素序列)：Required(必填). 
# Any iterable object where all the returned values are strings
#所有返回值為字串的任何可重做物件
#將字典中的所有專案放入字串中，使用「TEST」一詞作為分離器：
myDict = {"name": "John", "country": "Norway"}
mySeparator = "TEST"
x = mySeparator.join(myDict)
print(x) #nameTESTcountry,只有鍵被TEST隔開
myDict = {"name": "John", "country": "Norway"}
x = "#".join(myDict) #"#"為散列字元當作分離器
print(x) #name#country,只有鍵被#隔開
#iterable應該可以拆分任何一種形式的陣列,用符號或字元隔開裡面的字申
#注意：當使用字典作為可重做時，返回的值是"鍵"，而不是值。(錯誤翻譯)
#Note: When using a dictionary as an iterable, the returned values are the keys, not the values.
#注意：當使用字典當作序列,返回的都是鍵,而不是值

print(x.split("#")) #代號就是密鑰
#['name', 'country']
#split("#")把#切掉用list重組
x=dict({'name':"John",'country':"Norway"})
print(x)
print(len(x))
