#https://www.w3schools.com/python/python_strings_modify.asp
#Python -修改字串
#Python 有一套內置的方法，您可以在字串上使用。
#上箱Upper Case
#方法在上一種情況下傳回字串：upper()是每一個位元改為大寫
a = "Hello, World!"
print(a.upper())#upper是每一個位元改為大寫
#HELLO, WORLD!
#小寫
#方法在較低情況下傳回字串：lower()小寫
a = "Hello, World!"
print(a.lower())
#hello, world!
#刪除空白
#空白是實際文本之前和/或之後的空間，您經常要刪除此空間。
#該方法從開頭或結尾刪除任何空白：strip()
a = " Hello, World! "#本文前後都有空白
print(a.strip()) # returns "Hello, World!"
#替換字串
#該方法用另一個字串取代字串：replace()
a = "Hello, World!"
print(a.replace("H", "J"))#Jello, World!
#拆分字串
#方法返回指定分離器(要被拆掉的字元)之間的文本成為清單專案時的清單。split()
#如果找到分離器的實例，則方法將字串拆分為子弦：split()
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']把字串變為清單
print(a.split("o")) # returns ['Hell', ', W', 'rld!']o被拆掉