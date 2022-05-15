#https://www.w3schools.com/python/python_regex.asp#findall
#Python RegEx (Regular Expression)正則表示式
#findall() Function findall()函數
#The findall() function returns a list containing all matches.
#findall()函數傳回一個包含所有比對的清單
#Print a list of all matches:
#輸出所有比對的清單
import re
txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)

print("------------------------清單包含在順序裡找不到比對")
#The list contains the matches in the order they are found.
#清單包含在順序裡找不到比對
#If no matches are found, an empty list is returned:
#如果比對沒找到,一個空的清單會傳回
#Return an empty list if no match was found:
#如果比對找不到,傳回一個list型態的空清單
import re
txt = "The rain in Spain"
x = re.findall("Portugal", txt)
print(x) #[]