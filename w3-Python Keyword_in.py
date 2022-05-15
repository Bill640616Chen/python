#https://www.w3schools.com/python/ref_keyword_in.asp
#Python Keyword in 關鍵字 in
#To check if a value is present in a list, tuple, etc.
#檢查清單、元組等集合中是否存在某個值。
#Check if "banana" is present in the list:
#檢查清單中是否存在 「banana」
fruits = ["apple", "banana", "cherry"]
if "banana" in fruits:
  print("yes")
#Definition and Usage 定義和用法
#The in keyword has two purposes:
#in 關鍵字有兩種作用：
#The in keyword is used to check if a value is present in a sequence (list, range, string etc.).
#in 關鍵字用於檢查序列（清單、範圍、字串等）中是否存在值。
#The in keyword is also used to iterate through a sequence in a for loop:
#in 關鍵字還用於在 for 迴圈中反覆運算序列：
#Loop through a list and print the items:
print('-------------分隔線------------')
#遍歷清單並列印專案：
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)