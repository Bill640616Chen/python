#https://www.w3schools.com/python/python_string_formatting.asp
#String Formatting 字串格式化
#To make sure a string will display as expected, we can format the result with the format() method.
#為了確保字串按預期顯示，我們可以使用 format（） 方法對結果進行格式化。
#String format() 字串 format（）
#The format() method allows you to format selected parts of a string.
#format（） 方法允許您格式化字串的選定部分。
#Sometimes there are parts of a text that you do not control, maybe they come from a database, or user input?
#有時文本的一部分是你無法控制的，也許它們來自資料庫或使用者輸入？
#To control such values, add placeholders (curly brackets {}) in the text, and run the values through the format() method:
#要控制此類值，請在文本中添加佔位元（花括弧 {}），然後通過 format（） 方法運行值：
print("---------------------------------新增要顯示價格的佔位元")
#Add a placeholder where you want to display the price:
#新增要顯示價格的佔位元：
price = 49
txt = "The price is {} dollars"
print(txt.format(price))

print("---------------您可以在花括弧內新增參數以指定如何轉換值：")
#You can add parameters inside the curly brackets to specify how to convert the value:
#您可以在花括弧內新增參數以指定如何轉換值：
#Format the price to be displayed as a number with two decimals:
#將價格格式化為帶有兩位小數的數位：
price = 49
txt = "The price is {:.2f} dollars"
print(txt.format(price))
#Check out all formatting types in our String format() Reference.
#查看字串 format（） 參考手冊中的所有格式類型。
#Multiple Values 多個值
#If you want to use more values, just add more values to the format() method:
#如需使用更多值，只需向 format（） 方法添加更多值：
#print(txt.format(price, itemno, count))
print("------------------------------------並添加更多佔位元：")
#And add more placeholders:
#並添加更多佔位元：
quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))

print("------------------{0}{1}{2:.2f}----Index Numbers 索引號")
#Index Numbers 索引號
#You can use index numbers (a number inside the curly brackets {0}) to be sure the values are placed in the correct placeholders:
#您可以使用索引號（花括弧 {0} 內的數位）來確保將值放在正確的佔位元元中：
quantity = 3 #位置0
itemno = 567 #位置1
price = 49   #位置2
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))
print("--------------此外，如果要多次引用相同的值，請使用索引號：")
#Also, if you want to refer to the same value more than once, use the index number:
#此外，如果要多次引用相同的值，請使用索引號：
age = 36
name = "John"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))

print("---------------------------------Named Indexes 命名索引")
#Named Indexes 命名索引
#You can also use named indexes by entering a name inside the 
# curly brackets {carname}, but then you must use names when 
# you pass the parameter values txt.format(carname = "Ford"):
#您還可以通過在花括弧 {carname} 中輸入名稱來使用命名索引，
# 但是在傳遞參數值 txt.format（carname = "Ford"） 時，必須使用名稱：
myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))