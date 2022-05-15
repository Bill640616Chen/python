#https://www.w3schools.com/python/python_lists_comprehension.asp
#Python List Comprehension 清單理解
#List Comprehension 清單理解
#List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
#當您想要根據現有清單的值創建新清單時，清單理解提供了更短的語法。
#Example:範例
#Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.
#根據水果清單，您需要一個新的清單，其中僅包含名稱中帶有字母"a"的水果。
#Without list comprehension you will have to write a for statement with a conditional test inside:
#沒有清單理解,您必須編寫一個帶有條件測試的陳述：
print("-----------------print沒在for迴圈裡")
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [] #newlist = 清單
for x in fruits:
  if "a" in x:
    newlist.append(x) #append,清單增加項目的方法
print(newlist)
#1.進入for迴圈
#2."apple", "banana", "cherry", "kiwi", "mango"依序代入x,
# 如果x裡有a,就執行newlist.append(x)
#3.最後一個代入後,離開for迴圈,執行print(newlist)
print("-----------------print在for迴圈裡")
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [] #newlist = 清單
for x in fruits:
  if "a" in x:
    newlist.append(x) #append,清單增加項目的方法
    print(newlist)
#1.進入for迴圈
#2.把fruits清單的值依序代入,第一個符合條件就新增一個值到newlist
#3.進入print直接輸出['apple']清單
#4.再次進入for迴圈
#5.把fruits清單的值依序代入,第一個符合條件就新增一個值到newlist
#6.第二個符合條件就新增一個值到newlist
#7.進入print直接輸出['apple', 'banana']清單
#8.再次進入for迴圈
#9.把fruits清單的值依序代入,第一,第二,第五個符合條件就新增一個值到newlist
#10.進入print直接輸出['apple', 'banana', 'mango']清單

print("-----------------更短的語法")
#With list comprehension you can do all that with only one line
# of code:
#有了清單理解，您只需一行代碼即可做到這一點：
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x] #陳述式放在迴圈後面
print(newlist) #['apple', 'banana', 'mango']

print("------------------(簡短語法)語法詳解")
#The Syntax語法
#newlist = [expression for item in iterable if condition == True]
#[expression for 項目 in 可迭代物件 如果 條件 == True ]
#The return value is a new list, leaving the old list unchanged.
#傳回值是一個新的清單，使舊清單保持不變。
#Condition
#The condition is like a filter that only accepts the items that 
# valuate to True.
#此條件就像一個篩檢程式，只接受評估為 True 的項目。
#Only accept items that are not "apple":
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if x != "apple"]
print(newlist) #['banana', 'cherry', 'kiwi', 'mango']
#The condition if x != "apple"  will return True for all elements 
# other than "apple", making the new list contain all fruits 
# except "apple".
#條件if x!= "apple" 將傳回真實的所有元素， 除了 "蘋果"， 使新清單包含所有水果， 除了 "蘋果" 。

print("---------此條件是可自選的，可以省略的(簡短語法)")
#The condition is optional and can be omitted:
#此條件是可自選的，可以省略的：
#With no if statement:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits]
print(newlist) #["apple", "banana", "cherry", "kiwi", "mango"]

print("-------------------Iterable可迭代(簡短語法)")
#Iterable可迭代
#The iterable can be any iterable object, like a list, tuple, set etc.
#可迭代可以是任何可迭代的物件,像list, tuple, set 等等
#You can use the range() function to create an iterable:
newlist = [x for x in range(10)]
print(newlist) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#Same example, but with a condition:相同的例子,但是有一個條件
newlist = [x for x in range(10) if x < 5]
print(newlist) #[0, 1, 2, 3, 4]

print("-------------------------Expression(簡短語法)")
#Expression 運算式
#The expression is the current item in the iteration, but it is also the outcome,
# which you can manipulate before it ends up like a list item in the new list:
#該表示形式是反覆運算中的目前項目，但它也是結果，
# 您可以在新清單中的清單項目結束之前操作它

#Set the values in the new list to upper case:
#設定值在新清單裡要大寫
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x.upper() for x in fruits]
print(newlist) #['APPLE', 'BANANA', 'CHERRY', 'KIWI', 'MANGO']

print("--------您可以將結果設定為任何您喜歡的--Expression(簡短語法)")
#You can set the outcome to whatever you like:
#您可以將結果設定為任何您喜歡的：
#Set all values in the new list to 'hello':
#設定所有值在新清單為hello
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = ['hello' for x in fruits]
print(newlist) #['hello', 'hello', 'hello', 'hello', 'hello']

print("-----該運算式還可以包含條件，但作為一種操縱結果的方法--Expression(簡短語法)")
#The expression can also contain conditions, not like a filter, but as a way to manipulate the outcome:
#該運算式還可以包含條件，不像篩檢程式，但作為一種操縱結果的方法：
#Return "orange" instead of "banana":傳回「橘子」而不是「香蕉」
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist) #['apple', 'orange', 'cherry', 'kiwi', 'mango']
#The expression in the example above says:
#運算式在此例這麼說:
#Return the item if it is not banana, if it is banana return orange.
#傳回的項目如果它不是香蕉,如果是它是香蕉則傳回橘子

print("----Looping Using List Comprehension(簡短語法)")
#Looping Using List Comprehension迴圈使用清單理解
#List Comprehension offers the shortest syntax for looping through lists:
#清單理解提供了循環瀏覽清單的最短語法：
#A short hand for loop that will print all items in a list:
#循環的簡短語句，將列印清單中的所有項目：
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]
#簡單語句需要有[]

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
#問題提問
newlist = [x for x in fruits if x != "apple"]
newlist = [x  if x != "apple" else "orange" for x in fruits]
newlist = [x if x != "banana" else "orange" for x in fruits]
#if或for之後的條件式跑完,才會給最前面的x賦值


