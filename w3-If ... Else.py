#https://www.w3schools.com/python/python_conditions.asp
#Python If ... Else python的狀況
#Python Conditions and If statements
#Python supports the usual logical conditions from mathematics:
#Python 支援數學中通常的邏輯條件：
#Equals: a == b
#Not Equals: a != b
#Less than: a < b
#Less than or equal to: a <= b
#Greater than: a > b
#Greater than or equal to: a >= b
#These conditions can be used in several ways, most commonly in "if statements" and loops.
#這些條件可以通過多種方式使用，最常見的是「if陳述式」和迴圈。
#An "if statement" is written by using the if keyword.
#if 陳述式是使用 if 關鍵字寫的
print("------------------------------------if statement")
#If statement:
a = 33
b = 200
if b > a:
  print("b is greater than a")
  #b is greater than a
#In this example we use two variables, a and b, which are 
# used as part of the if statement to test whether b is 
# greater than a. As a is 33, and b is 200, we know that
# 200 is greater than 33, and so we print to screen that
#  "b is greater than a".
#在此示例中，我們使用兩個變數，a 和 b，這些變數用作如果語句的
# 一部分，以測試 b 是否大於 a。作為a是33，b是200，我們知道200
# 大於33，所以我們列印螢幕，"b is greater than a"。

#Indentation 縮排
#Python relies on indentation (whitespace at the beginning 
# of a line) to define scope in the code. Other programming
# languages often use curly brackets for this purpose.
#Python 依靠縮排（行開頭的空白）來定義代碼中的範圍。其他程式設計
# 語言通常為此目的使用捲曲括弧{}。
#If statement, without indentation (will raise an error):
print("-----------------if statemen沒有縮排的話,將會提升錯誤")
#If 條件式,沒有縮排的話,將會提升錯誤
a = 33
b = 200
if b < a:
#print("b is greater than a") # you will get an error
  print("b is greater than a")
#因為b < a是False,所以沒執行print

print("-------------------------------------------if elif")
#Elif elif表示再次判斷的意思，是else if的簡寫
#The elif keyword is pythons way of saying "if the previous
# conditions were not true, then try this condition".
#elif 關鍵字是python的方式說「如果先前的條件不是真的，
# 那麼嘗試這個條件」 。
a = 33
b = 33
if b > a: #這個陳述不是True,所以執行下一個
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
#a and b are equal
#In this example a is equal to b, so the first condition
# is not true, but the elif condition is true, so we print
# to screen that "a and b are equal".

print("--------------------------------------if elif else")
#Else
#The else keyword catches anything which isn't caught by the preceding conditions.
#else關鍵字捕獲任何沒有被上述條件捕獲的東西。
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
#a is greater than b
#In this example a is greater than b, so the first condition
# is not true, also the elif condition is not true, so we 
# go to the else condition and print to screen that "a is 
# greater than b".
print("-----------------------------------------if Else")
#You can also have an else without the elif:
#你也可以有else,沒有elif
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
#b is not greater than a

print("------------------------------------Short Hand If")
#Short Hand If 短敍述句If
#If you have only one statement to execute, you can put it
# on the same line as the if statement.
#如果您只有一個語句要執行，則可以將其與if語句放在同一行上。
#One line if statement:
a = 200
b = 33
if a > b: print("a is greater than b")
#a is greater than b

print("----------------------------Short Hand If ... Else")
#Short Hand If ... Else 短敍述句If ... Else
#If you have only one statement to execute, one for if, and 
# one for else, you can put it all on the same line:
#如果你只有一個語句要執行,一個為了if和一個為了else,你可以把它們
# 全部放在同一行
a = 2
b = 330
print("A") if a > b else print("B") #B
#如果a>b就執行print("A"),若不符合則print("B")
#This technique is known as Ternary Operators, 
# or Conditional Expressions.
#此技術稱為三元操作員或條件表達。
#You can also have multiple else statements on the same line:
print("---------------------您也可以在同一行上有多個else語句")
#您也可以在同一行上有多個else語句：
#One line if else statement, with 3 conditions:
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")
#＝,第一個判斷式print("A") if a > b else print("=") 
# a>b是假的,所以執行第二個判斷式
#第二次判斷式print("=") if a == b else print("B")
# a==b 是真的,所以執行print("=")
print("A") if a > b else print("=") if a < b else print("B")
#Ｂ,第一個判斷式print("A") if a > b else print("=")
# a>b是假的,所以執行第二個判斷式
#第二次判斷式print("=") if a < b else print("B")
# a<b也是假的,就執行print("B")

print("----------and關鍵字是一個邏輯操作員，用於組合條件語句：")
#And
#The and keyword is a logical operator, and is used to combine conditional statements:
#and關鍵字是一個邏輯操作員，用於組合條件語句：
#Test if a is greater than b, AND if c is greater than a:
a = 200
b = 33
c = 500
if a > b and c > a :
  print("Both conditions are True")
#and可以好幾個
#if a > b and c > a and a > c:判斷False,不會執行print
#if a > b and c > a and a <= c:判斷True,才會執行print
#and是所有條件都要是True,才會執行print

print("-----------or關鍵字是一個邏輯操作員，用於組合條件語句：")
#Or
#The or keyword is a logical operator, and is used to combine conditional statements:
#or關鍵字是一個邏輯操作員，用於組合條件語句：
#Test if a is greater than b, OR if a is greater than c:
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")
#or也很可以很多個,至少有一個True,就會執行print
#如果or全部都是False,不會執行print

print("-------------------------------Nested If if裡面的if")
#Nested If if裡面的if
#You can have if statements inside if statements, 
# this is called nested if statements.
x = 41
if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")
#先執行外面的if,再執行裡面的if
#如果外面的if是False,就不會執行裡面的if 
#如果裡面的if是False,就會輸出else
x = 41
if x > 10:
  print("Above ten,")
  if x < 20:
    print("and also above 20!")
  elif x < 30:
    print("above 30!")  
  else:
    print("but not above 20.")
#先執行外面的if,判斷為True,則執行print("Above ten,")
#接著執行裡面的if x<20 :判斷為False
#接著到elif判斷也是False
#最後到else,因為上面兩個都為False
# ,所以會執行print("but not above 20.")

print("-------------------------------The pass Statement")
#The pass Statement
#if statements cannot be empty, but if you for some reason
# have an if statement with no content, put in the pass 
# statement to avoid getting an error.
#if 陳述式不能是空的,但是如果你為了某些理由需要一個沒有內容的
# if陳述式,把它放在pass陳述式可以避免錯誤
a = 33
b = 200
if b > a:
  pass
# having an empty if statement like this, 
# would raise an error without the pass statement
#a = 33
#b = 200
#if b > a:
#IndentationError: expected an indented block
#縮放錯誤：預期縮編塊
