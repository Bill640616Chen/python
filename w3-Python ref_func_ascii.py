#https://www.w3schools.com/python/ref_func_ascii.asp
#Python ascii() Function Python ascii()函數
#Returns a readable version of an object. Replaces none-ascii characters with escape character
#返回物件的可讀版本。 用轉義字元替換 none-ascii 字元。
#Escape non-ascii characters:
#轉義非 ASCII 字元：
x = ascii("My name is Ståle")
print(x)
#Definition and Usage 定義和用法
#The ascii() function returns a readable version of any object (Strings, Tuples, Lists, etc).
#ascii（） 函數傳回任何物件（字串，元組，清單等）的可讀版本。
#The ascii() function will replace any non-ascii characters with escape characters:
#ascii（） 函數會將所有非 ascii 字元替換為轉義字元：
#å will be replaced with \xe5.
#å 將替換為 xe5。
#Syntax 語法
#ascii(object)
#Parameter參數：Values值
#Parameter參數：Description描述
#object	An object, like String, List, Tuple, Dictionary etc.
#object 物件，比如字串、清單、元組、字典等等。
