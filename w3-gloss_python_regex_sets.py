#https://www.w3schools.com/python/gloss_python_regex_sets.asp
#Python RegEx Sets 正則表達式集
#A set is a set of characters inside a pair of square brackets with a special meaning: []
#集合是一對方括號內的一組字元，具有特殊含義： []
#Set	    Description	
#[arn]	    Returns a match where one of the specified 
#           characters (a, r, or n) are present	
import re
txt = "The rain in Spain"
#Check if the string has any a, r, or n characters:
x = re.findall("[arn]", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
print('-------------分隔線------------')
#[a-n]	    Returns a match for any lower case character, 
#           alphabetically between a and n	
import re
txt = "The rain in Spain"
#Check if the string has any characters between a and n:
x = re.findall("[a-n]", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
print('-------------分隔線------------')
#[^arn]	    Returns a match for any character EXCEPT a, r, 
#           and n	
import re
txt = "The rain in Spain"
#Check if the string has other characters than a, r, or n:
x = re.findall("[^arn]", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
print('-------------分隔線------------')
#[0123]	    Returns a match where any of the specified 
#           digits (0, 1, 2, or 3) are present	
import re
txt = "The rain in Spain"
#Check if the string has any 0, 1, 2, or 3 digits:
x = re.findall("[0123]", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
print('-------------分隔線------------')
#[0-9]	    Returns a match for any digit between 0 and 9	
import re
txt = "8 times before 11:45 AM"
#Check if the string has any digits:
x = re.findall("[0-9]", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
print('-------------分隔線------------')
#[0-5][0-9]	Returns a match for any two-digit numbers 
#           from 00 and 59	
import re
txt = "8 times before 11:45 AM"
#Check if the string has any two-digit numbers, from 00 to 59:
x = re.findall("[0-5][0-9]", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
print('-------------分隔線------------')
#[a-zA-Z]	Returns a match for any character alphabetically
#           between a and z, lower case OR upper case	
import re
txt = "8 times before 11:45 AM"
#Check if the string has any characters from a to z lower case, and A to Z upper case:
x = re.findall("[a-zA-Z]", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
print('-------------分隔線------------')
#[+]	    In sets, +, *, ., |, (), $,{} has no special 
#           meaning, so [+] means: return a match for any + 
#           character in the string
import re
txt = "8 times before 11:45 AM"
#Check if the string has any + characters:
x = re.findall("[+]", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
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
#RegEx Special Sequences 正則表達式特殊序列
#https://www.w3schools.com/python/gloss_python_regex_sequences.asp
#RegEx Match Object 正則表達式匹配物件
#https://www.w3schools.com/python/gloss_python_regex_match.asp