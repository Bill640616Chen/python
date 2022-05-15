#https://www.w3schools.com/python/gloss_python_regex_metacharacters.asp
#Python RegEx Meta Characters
#Metacharacters 元字元
#Metacharacters are characters with a special meaning:
#元字元是具有特殊含義的字元：
#Character	Description	                Example	
#[]	        A set of characters	        "[a-m]"	
import re
txt = "The rain in Spain"
#Find all lower case characters alphabetically between "a" and "m":
x = re.findall("[a-m]", txt)
print(x)
print('-------------分隔線------------')
#\	        Signals a special sequence
#           (can also be used to escape 
#           special characters)	        "\d"	
import re
txt = "That will be 59 dollars"
#Find all digit characters:
x = re.findall("\d", txt)
print(x)
print('-------------分隔線------------')
#.	        Any character (except 
#           newline character)	        "he..o"	
import re
txt = "hello planet"
#Search for a sequence that starts with "he", followed by two (any) characters, and an "o":
x = re.findall("he..o", txt) #一定要2個點,1個點會變成空集合
print(x)
print('-------------分隔線------------')
#^	        Starts with	                "^hello"	
import re
txt = "hello planet"
#Check if the string starts with 'hello':
x = re.findall("^hello", txt)
if x:
  print("Yes, the string starts with 'hello'")
else:
  print("No match")
print('-------------分隔線------------')
#$	        Ends with	                "planet$"	
import re
txt = "hello planet"
#Check if the string ends with 'planet':
x = re.findall("planet$", txt)
if x:
  print("Yes, the string ends with 'planet'")
else:
  print("No match")
print('-------------分隔線------------')
#*	        Zero or more occurrences	"he.*o"	
import re
txt = "hello planet"
#Search for a sequence that starts with "he", followed by 0 or more  (any) characters, and an "o":
x = re.findall("he.*o", txt)
print(x)
print('-------------分隔線------------')
#+	        One or more occurrences	    "he.+o"	
import re
txt = "hello planet"
#Search for a sequence that starts with "he", followed by 1 or more  (any) characters, and an "o":
x = re.findall("he.+o", txt)
print(x)
print('-------------分隔線------------')
#?	        Zero or one occurrence	    "he.?o"	
import re
txt = "hello planet"
#Search for a sequence that starts with "he", followed by 0 or 1  (any) character, and an "o":
x = re.findall("he.?o", txt) #?往前0或1個字元
print(x)
#This time we got no match, because there were not zero, not one, but two characters between "he" and the "o"
print('-------------分隔線------------')
#{}	        Exactly the specified 
#           number of occurrences	    "he.{2}o"	
import re
txt = "hello planet"
#Search for a sequence that starts with "he", followed excactly 2 (any) characters, and an "o":
x = re.findall("he.{2}o", txt)
print(x)
print('-------------分隔線------------')
#|	        Either or	                "falls|stays"	
import re
txt = "The rain in Spain falls mainly in the plain!"
#Check if the string contains either "falls" or "stays":
x = re.findall("falls|stays", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
#()	        Capture and group	 
#Related Pages 相關頁面
#Python RegEx Tutorial Python 正則表達式教程
#https://www.w3schools.com/python/python_regex.asp
#RegEx 正則表達式
#https://www.w3schools.com/python/gloss_python_regex.asp
#RegEx Functions 正則表達式函數
#https://www.w3schools.com/python/gloss_python_regex_functions.asp
#RegEx Special Sequences 正則表達式特殊序列
#https://www.w3schools.com/python/gloss_python_regex_sequences.asp
#RegEx Sets 正則表達式集
#https://www.w3schools.com/python/gloss_python_regex_sets.asp
#RegEx Match Object 正則表達式匹配物件
#https://www.w3schools.com/python/gloss_python_regex_match.asp