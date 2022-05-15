#https://www.w3schools.com/python/gloss_python_regex_sequences.asp
#Python RegEx Special Sequences 正則式特殊序列
#Special Sequences 特殊序列
#A special sequence is a followed by one of the characters in the list below, and has a special meaning:\
#特殊序列是後跟以下清單中的字元之一，具有特殊含義：\
#Character	Description	                        Example	
#\A	        Returns a match if the specified
#           characters are at the beginning 
#           of the string	                    "\AThe"	
import re
txt = "The rain in Spain"
#Check if the string starts with "The":
x = re.findall("\AThe", txt)
print(x)
if x:
  print("Yes, there is a match!")
else:
  print("No match")
print('-------------分隔線------------')
#r"\bain"
#\b	        Returns a match where the specified
#           characters are at the beginning or 
#           at the end of a word	            
#                                               	
import re
txt = "The rain in Spain"
#Check if "ain" is present at the beginning of a WORD:
#r"" 的作用是去除轉義字元.對應re,有沒有r,結果是一樣的
#除非b有另外的意思,所以需要去除轉義
x = re.findall(r"\bain", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

print('-------------分隔線------------')
#r"ain\b"
import re
txt = "The rain in Spain"
#Check if "ain" is present at the end of a WORD:
#r"" 的作用是去除轉義字元.對應re,有沒有r,結果是一樣的
#除非b有另外的意思,所以需要去除轉義
x = re.findall(r"ain\b", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
print('-------------分隔線-----585-------')
#r"\Bain"
#\B	        Returns a match where the specified 
#           characters are present, but NOT at 
#           the beginning (or at the end) of a 
#           word	                            
import re
txt = "The rain in Spain"
#Check if "ain" is present, but NOT at the beginning of a word:
#r"" 的作用是去除轉義字元.對應re,有沒有r,結果是一樣的
#除非b有另外的意思,所以需要去除轉義
x = re.findall(r"\Bain", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

print('-------------分隔線------------')
#r"ain\B"
import re
txt = "The rain in Spain"
#Check if "ain" is present, but NOT at the end of a word:
#r"" 的作用是去除轉義字元.對應re,有沒有r,結果是一樣的
#除非b有另外的意思,所以需要去除轉義
x = re.findall(r"ain\B", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
print('-------------分隔線------------')
#\d	        Returns a match where the string
#           contains digits (numbers from 0-9)	"\d"	
import re
txt = "The rain in Spain"
#Check if the string contains any digits (numbers from 0-9):
x = re.findall("\d", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
print('-------------分隔線------------')
#\D	        Returns a match where the string 
#           DOES NOT contain digits	            "\D"	
import re
txt = "The rain in Spain"
#Return a match at every no-digit character:
x = re.findall("\D", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
print('-------------分隔線------------')
#\s	        Returns a match where the string 
#           contains a white space character	"\s"	
import re
txt = "The rain in Spain"
#Return a match at every white-space character:
x = re.findall("\s", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
print('-------------分隔線------------')
#\S	        Returns a match where the string 
#           DOES NOT contain a white space 
#           character	                        "\S"	
import re
txt = "The rain in Spain"
#Return a match at every NON white-space character:
x = re.findall("\S", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
print('-------------分隔線------------')
#\w	        Returns a match where the string 
#           contains any word characters 
#           (characters from a to Z, digits 
#           from 0-9, and the underscore _ 
#           character)	                        "\w"	
import re
txt = "The rain in Spain"
#Return a match at every word character (characters from a to Z, digits from 0-9, and the underscore _ character):
x = re.findall("\w", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
print('-------------分隔線------------')
#\W	        Returns a match where the string
#           DOES NOT contain any word 
#           characters                      	"\W"	
import re
txt = "The rain in Spain"
#Return a match at every NON word character (characters NOT between a and Z. Like "!", "?" white-space etc.):
x = re.findall("\W", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
print('-------------分隔線------------')
#\Z	        Returns a match if the specified
#           characters are at the end of the 
#           string	                            "Spain\Z"
import re
txt = "The rain in Spain"
#Check if the string ends with "Spain":
x = re.findall("n\Z", txt)
print(x)
if x:
  print("Yes, there is a match!")
else:
  print("No match")
#Related Pages 相關頁面
#Python RegEx Tutorial Python 正則表達式教程
#https://www.w3schools.com/python/python_regex.asp
#RegEx 正則表達式
#https://www.w3schools.com/python/gloss_python_regex.asp
#RegEx Functions 正則表達式函數
#https://www.w3schools.com/python/gloss_python_regex_functions.asp
#Metacharacters in RegEx 正則表達式中的元字元
#https://www.w3schools.com/python/gloss_python_regex_metacharacters.asp
#RegEx Sets 正則表達式集
#https://www.w3schools.com/python/gloss_python_regex_sets.asp
#RegEx Match Object 正則表達式匹配物件
#https://www.w3schools.com/python/gloss_python_regex_match.asp