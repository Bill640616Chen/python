#https://www.w3schools.com/python/python_strings_format.asp
#Python -格式字串
#字串格式
#正如我們在 Python 變數章節中學到的，我們不能將字串和數字組合在一起：
#TypeError: unsupported operand type(s) for +: 'int' and 'str'
#不受支援的操作類型
#age = 36
#txt = "My name is John, I am " + age
#print(txt)#can only concatenate str (not "int") to str
#唯一串聯的str （不是 "int"） 到 str

#但是，我們可以使用這種方法將字串和數字結合起來！format()
#該方法採用通過的參數，對它們進行格式化，並將它們放置在佔位元所在的字串中：
# format(){}
#使用該方法會插入字串：format()
age1 = 36
txt1 = "My name is John, and I am{}" #{}age1的值自動放入
#因為 txt1.format(age1) 這個功能, age1 取代了 txt1裡的 {}.
print(txt1.format(age1)) #My name is John, and I am36
txt1 = "{}, is the cutest man in the world"
age1 = "Tommy Lu "
print(txt1.format(age1))
#Tommy Lu , is the cutest man in the world

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

#I want 3 pieces of item 567 for 49.95 dollars.
#您可以使用索引號確保參數被放置在正確的佔位元中：{0}
quantity = 3  #位置0
itemno = 567  #位置1
price = 49.95 #位置2
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
#{}裡面的數字代表索引的位置
print(myorder.format(quantity, itemno, price))
#I want to pay 49.95 dollars for 3 pieces of item 567.