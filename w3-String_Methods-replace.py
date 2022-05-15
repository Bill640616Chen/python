#https://www.w3schools.com/python/ref_string_replace.asp
#Python 字串 replace() Method
#替換「香蕉」一詞：
txt = "I like bananas"
x = txt.replace("bananas", "apples")
print(x)
#定義和使用
#該方法用另一個指定短語替換指定短語。replace()
#筆記：如果沒有指定其他短語，所有發生則將替換指定短語的。
#Sytax語法
#string.replace(oldvalue, newvalue, count)
#參數值
#Parameter：Description
#oldvalue(舊值)：Required(必填). The string to search for
#newvalue(新值)：Required(必填). The string to replace the old value with
#count(計算)：Optional(自選).
#A number specifying how many occurrences of the old value you want to replace. Default is all occurrences
#指定要替換舊值的發生次數的數位。預設是所有事件
#取代「one」字的所有發生：
txt = "one one was a race horse, two two was one too."
x = txt.replace("one", "three")
print(x)
#three three was a race horse, two two was three too.
#替換「one」字的第一次出現：
txt = "one one was a race horse, two two was one too."
x = txt.replace("one", "three", 2) #one取代兩次
print(x)
#three three was a race horse, two two was one too.