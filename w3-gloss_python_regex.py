#https://www.w3schools.com/python/gloss_python_regex.asp
#Python RegEx 正則表達式
#RegEx Module 正則表達式模組
#Python has a built-in package called , which can be used to work with Regular Expressions.re
#Python有一個名為 的內置包，可用於處理正則表示式。re
#Import the module:re
#匯入模組：re
import re
#RegEx in Python Python 中的正則表達式
#When you have imported the module, you can start using regular expressions:re
#匯入模組後，可以開始使用正規表示式：re
#Search the string to see if it starts with "The" and ends with "Spain":
#搜尋字串以查看它是否以「The」開頭並以「Spain」結尾：
import re
#Check if the string starts with "The" and ends with "Spain":
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
if x:
  print("YES! We have a match!")
else:
  print("No match")
#Related Pages 相關頁面
#Python RegEx Tutorial Python 正則表達式教程
#https://www.w3schools.com/python/python_regex.asp
#RegEx Functions 正則表達式函數
#https://www.w3schools.com/python/gloss_python_regex_functions.asp
#Metacharacters in RegEx 正則表達式中的元字元
#https://www.w3schools.com/python/gloss_python_regex_metacharacters.asp
#RegEx Special Sequences 正則表達式特殊序列
#https://www.w3schools.com/python/gloss_python_regex_sequences.asp
#RegEx Sets 正則表達式集
#https://www.w3schools.com/python/gloss_python_regex_sets.asp
#RegEx Match Object 正則表達式匹配物件
#https://www.w3schools.com/python/gloss_python_regex_match.asp