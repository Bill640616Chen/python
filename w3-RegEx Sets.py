#https://www.w3schools.com/python/python_regex.asp
#Python RegEx (Regular Expression)正則表示式
#Sets 集合
#A set is a set of characters inside a pair of square brackets [] with a special meaning:
#集合（Set）是一對方括弧 [] 內的一組字元，具有特殊含義：
print("---------------[arn]：如果指定的字元位於字串的開頭，則返回匹配項")
#[arn]：Returns a match where one of the specified characters (a, r, or n) are present
#返回一個匹配項，其中存在指定字元（a，r 或 n）之一
import re
txt = "The rain in Spain"
#Check if the string has any a, r, or n characters:
x = re.findall("[arn]", txt)
print(x)
if x:
  print("Yes, there is at least one match!") #
else:
  print("No match")

print("------------[a-n]：返回指定字元位於單詞的開頭或末尾的匹配項")
#[a-n]：Returns a match for any lower case character, alphabetically between a and n
#返回字母順序 a 和 n 之間的任意小寫字元匹配項
#import re
txt = "The rain in Spain"
#Check if the string has any characters between a and n:
x = re.findall("[a-n]", txt)
print(x)
if x:
  print("Yes, there is at least one match!") #
else:
  print("No match")

print("------------[^arn]：返回除 a、r 和 n 之外的任意字元的匹配項")
#[^arn]：Returns a match for any character EXCEPT a, r, and n
#返回除 a、r 和 n 之外的任意字元的匹配項
import re
txt = "The rain in Spain"
#Check if the string has other characters than a, r, or n:
x = re.findall("[^arn]", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

print("--------------[0123]：傳回指定字元存在的匹配項，但不在單詞的開頭（或結尾處）")
#[0123]：Returns a match where any of the specified digits (0, 1, 2, or 3) are present
#返回存在任何指定數位（0、1、2 或 3）的匹配項
import re
txt = "The rain in Spain"
#Check if the string has any 0, 1, 2, or 3 digits:
x = re.findall("[0123]", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match") #[]

print("---------------[0-9]：傳回指定字元存在的匹配項，但不在單詞的開頭（或結尾處）")
#[0-9]：Returns a match for any digit between 0 and 9
#返回 0 與 9 之間任意數位的匹配
import re
txt = "8 times before 11:45 AM"
#Check if the string has any digits:
x = re.findall("[0-9]", txt)
print(x)
if x:
  print("Yes, there is at least one match!") #
else:
  print("No match")
print("-----------測試[0-9]：傳回指定字元存在的匹配項，但不在單詞的開頭（或結尾處）")
import re
txt = "8 times before 11:45 AM"
#Check if the string has any digits:
print(re.findall("[0-9]", txt))

print("-----------[0-5][0-9]：返回介於 00 到 59 之間的任何數位的匹配項")
#[0-5][0-9]：Returns a match for any two-digit numbers from 00 and 59
#返回介於 00 到 59 之間的任何數位的匹配項
import re
txt = "8 times before 11:45 AM"
#Check if the string has any two-digit numbers, from 00 to 59:
x = re.findall("[0-5][0-9]", txt)
print(x)
if x:
  print("Yes, there is at least one match!") #
else:
  print("No match")

print("-----------[0-5][0-9][0-9]：測試可以幾位數")
import re
txt = "123,566,687,325,903,125"
#Check if the string has any two-digit numbers, from 000 to 599:
x = re.findall("[0-5][0-9][0-9]", txt) #[不能0-0]會變空集合
print(x) #['123', '566', '325', '125']

print("-------------[a-zA-Z]：返回字母順序 a 和 z 之間的任何字元的匹配，小寫或大寫")
#[a-zA-Z]：Returns a match for any character alphabetically between a and z, lower case OR upper case
#返回字母順序 a 和 z 之間的任何字元的匹配，小寫或大寫
import re
txt = "8 times before 11:45 AM"
#Check if the string has any characters from a to z lower case, and A to Z upper case:
x = re.findall("[a-zA-Z]", txt) #[A-Z][a-z]也可
print(x)
if x:
  print("Yes, there is at least one match!") #
else:
  print("No match")

print("------------[+]：在集合中，+、*、. 、|、（）、$、{} 沒有特殊含義，因此 [+] 表示：返回字串中任何 + 字元的匹配項")
#[+]：In sets, +, *, ., |, (), $,{} has no special meaning, 
# so [+] means: return a match for any + character in the string
#在集合中，+、*、. 、|、（）、$、{} 沒有特殊含義，
# 因此 [+] 表示：返回字串中任何 + 字元的匹配項
import re
txt = "8 times before 11:45 AM"
#Check if the string has any + characters:
x = re.findall("[+]", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match") #
import re
txt = "8 times before 11:45 AM"
#Check if the string has any + characters:
x = re.findall("[be+]", txt)
print(x) #['e', 'b', 'e', 'e']