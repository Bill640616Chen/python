#https://www.w3schools.com/python/python_regex.asp
#Python RegEx (Regular Expression)正則表示式
#Special Sequences 特殊序列
#A special sequence is a \ followed by one of the characters in the list below, and has a special meaning:
#特殊序列指的是\後跟下表中的某個字元，擁有特殊含義：
print("---------------\A：如果指定的字元位於字串的開頭，則返回匹配項")
#\A：Returns a match if the specified characters are at the beginning of the string
#如果指定的字元位於字串的開頭，則返回匹配項
import re
txt = "The rain in Spain"
#Check if the string starts with "The":
x = re.findall("\AThe", txt)
print(x)
if x:
  print("Yes, there is a match!")
else:
  print("No match")

print("------------開頭-\b：返回指定字元位於單詞的開頭或末尾的匹配項")
#\b：Returns a match where the specified characters are at the
#  beginning or at the end of a word
#返回指定字元位於單詞的開頭或末尾的匹配項
#(the "r" in the beginning is making sure that the string is 
# being treated as a "raw string")
#（開頭的"r"是確保字串被視為"原始字串"）
import re
txt = "The rain in Spain"
#Check if "ain" is present at the beginning of a WORD:
x = re.findall(r"\bain", txt) #檢查ain是否為字首
print(x)
if x :
  print("Yes, there is at least one match!")
else:
  print("No match")

print("------------末尾-\b：返回指定字元位於單詞的開頭或末尾的匹配項")
#\b：Returns a match where the specified characters are at the
#  beginning or at the end of a word
#返回指定字元位於單詞的開頭或末尾的匹配項
#(the "r" in the beginning is making sure that the string is 
# being treated as a "raw string")
#（開頭的"r"是確保字串被視為"原始字串"）
import re
txt = "The rain in Spain"
#Check if "ain" is present at the end of a WORD:
x = re.findall(r"ain\b", txt) #檢查ain是否為字尾
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

print("--------------開頭-\B：傳回指定字元存在的匹配項，但不在單詞的開頭（或結尾處）")
#\B：Returns a match where the specified characters are present, 
# but NOT at the beginning (or at the end) of a word
#(the "r" in the beginning is making sure that the string is 
# being treated as a "raw string")
#傳回指定字元存在的匹配項，但不在單詞的開頭（或結尾處）
#（開頭的"r"是確保字串被視為"原始字串"）
import re
txt = "The rain in Spain"
#Check if "ain" is present, but NOT at the beginning of a word:
x = re.findall(r"\Bain", txt)
print(x)
if x:
  print("Yes, there is at least one match!") #
else:
  print("No match")

print("---------------末尾-\B：傳回指定字元存在的匹配項，但不在單詞的開頭（或結尾處）")
#\B：Returns a match where the specified characters are present, 
# but NOT at the beginning (or at the end) of a word
#(the "r" in the beginning is making sure that the string is 
# being treated as a "raw string")
#傳回指定字元存在的匹配項，但不在單詞的開頭（或結尾處）
#（開頭的"r"是確保字串被視為"原始字串"）
import re
txt = "The rain in Spain"
#Check if "ain" is present, but NOT at the end of a word:
x = re.findall(r"ain\B", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match") #[]No match

print("-------------\d：傳回字串包含數位的符合項（數位 0-9）")
#\d：Returns a match where the string contains digits 
# (numbers from 0-9)
#傳回字串包含數位的符合項（數位 0-9）
import re
txt = "The rain in2Spain"
#Check if the string contains any digits (numbers from 0-9):
x = re.findall("\d", txt)
print(x)
if x:
  print("Yes, there is at least one match!") #['2]
else:
  print("No match")

print("-------------\D：返回字串不包含數位的匹配項")
#\D：Returns a match where the string DOES NOT contain digits
#返回字串不包含數位的匹配項
import re
txt = "The rain in2Spain"
#Return a match at every no-digit character:
x = re.findall("\D", txt)
print(x)
if x:
  print("Yes, there is at least one match!") #
else:
  print("No match")

print("----------------------\s：返回字串包含空白字元的匹配項")
#\s：Returns a match where the string contains a white space character
#返回字串包含空白字元的匹配項
import re
txt = "The rain in Spain"
#Return a match at every white-space character:
x = re.findall("\s", txt)
print(x)
if x:
  print("Yes, there is at least one match!") #
else:
  print("No match")

print("--------------------------\S：返回字串不包含空白字元的匹配項")
#\S：Returns a match where the string DOES NOT contain a white space character
#返回字串不包含空白字元的匹配項
import re
txt = "The rain in Spain"
#Return a match at every NON white-space character:
x = re.findall("\S", txt)
print(x)
if x:
  print("Yes, there is at least one match!") #
else:
  print("No match")

print("---------------\w：返回一個匹配項，其中字串包含任何單詞字元")
#\w：Returns a match where the string contains any word 
# characters (characters from a to Z, digits from 0-9, 
# and the underscore _ character)
#返回一個匹配項，其中字串包含任何單詞字元
#（從 a 到 Z 的字元，從 0 到 9 的數位和下劃線 _ 字元）
import re
str = "The rain in Spain"
#Return a match at every word character (characters from a to Z, digits from 0-9, and the underscore _ character):
x = re.findall("\w", str)
print(x)
if (x):
  print("Yes, there is at least one match!") #
else:
  print("No match")

print("------------\W：返回一个匹配项，其中字符串不包含任何单词字符")
#\W：Returns a match where the string DOES NOT contain any word characters
#返回一个匹配项，其中字符串不包含任何单词字符
import re
txt = "The rain in Spain"
#Return a match at every NON word character (characters NOT between a and Z. Like "!", "?" white-space etc.):
x = re.findall("\W", txt)
print(x)
if x:
  print("Yes, there is at least one match!") #
else:
  print("No match")

print("------------\Z：如果指定的字元位於字串的末尾，則返回匹配項")
#\Z：Returns a match if the specified characters are at the end of the string
#如果指定的字元位於字串的末尾，則返回匹配項
import re
txt = "The rain in Spain"
#Check if the string ends with "Spain":
x = re.findall("Spain\Z", txt)
print(x)
if x:
  print("Yes, there is a match!") #
else:
  print("No match")
