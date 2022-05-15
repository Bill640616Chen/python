#https://www.w3schools.com/python/python_regex.asp#search
#Python RegEx (Regular Expression)正則表示式
#search() Function search()函數
#The search() function searches the string for a match, 
# and returns a Match object if there is a match.
#搜索（） 功能搜索比對字串，並在比對時返回比對物件。
#If there is more than one match, only the first 
# occurrence of the match will be returned:
#如果有多項比對,只有傳回第一次的比對
#Search for the first white-space character in the string:
#搜尋字串的第一個空白
import re
txt = "The rain in Spain"
x = re.search("\s", txt)
#\s：Returns a match where the string contains a white space character
#傳回包含空白字元的字串比對
print("The first white-space character is located in position:", x.start())
#x.start()傳回第一個空白從哪個位置出現

print("------------------------如果比對沒找到,則傳回None值")
#If no matches are found, the value None is returned:
#如果比對沒找到,則傳回None值
#Make a search that returns no match:
#做一個無比對的搜尋
import re
txt = "The rain in Spain"
x = re.search("Portugal", txt)
print(x)