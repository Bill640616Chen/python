#https://www.w3schools.com/python/python_regex.asp
#Python RegEx (Regular Expression)正則表示式
#Metacharacters字元符
#Metacharacters are characters with a special meaning:
#字元符是具有特殊含義的字元：
print("-----------------------[]：A set of characters 一组字符")
#[]：A set of characters 一组字符
import re
txt = "The rain in Spain"
#Find all lower case characters alphabetically between "a" and "m":
x = re.findall("[a-m]", txt)
print(x) #['h', 'e', 'a', 'i', 'i', 'a', 'i']

print("----------------------\：示意特殊序列（也可用於轉義特殊字元）")
#Signals a special sequence (can also be used to escape special characters)
#示意特殊序列（也可用於轉義特殊字元）
import re
txt = "That will be 59 dollars"
#Find all digit characters:
x = re.findall("\d", txt)
#\d：傳回字串包含數位的符合項（數位 0-9）	
print(x) #['5', '9']

print("----------------------.：任何字元（換行符除外）")
#.：Any character (except newline character)
#任何字元（換行符除外）
import re
txt = "hello_world"
#Search for a sequence that starts with "he", followed by two (any) characters, and an "o":
x = re.findall("he...o", txt)
print(x) #[]一個點代表一個字元
x = re.findall("he..._", txt)
print(x) #['hello_']空白字元也可以匹配

print("---------------------------^：Starts with 起始於")
#^：Starts with 起始於
import re
txt = "hello world"
#Check if the string starts with 'hello':
x = re.findall("^hello ", txt)
if x:
  print("Yes, the string starts with 'hello'")
else:
  print("No match")

print("---------------------------$：Ends with 結束於")
#$：Ends with 結束於
import re
txt = "hello world "
#Check if the string ends with 'world':
x = re.findall("world$", txt)
if x:
  print("Yes, the string ends with 'world'")
else:
  print("No match")

print("-------------*：Zero or more occurrences 零次或多次出現")
#*：Zero or more occurrences 零次或多次出現
import re
txt = "The rain in Spain falls mainly in the plain!"
#Check if the string contains "ai" followed by 0 or more "x" characters:
x = re.findall("aix*", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

print("-------------+：One or more occurrences 一次或多次出現")
#+：One or more occurrences 一次或多次出現
import re
txt = "The rain in Spain falls mainly in the plain!"
#Check if the string contains "ai" followed by 1 or more "x" characters:
x = re.findall("aix+", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

print("------{}：Exactly the specified number of occurrences確切地指定的出現次數")
#{}：Exactly the specified number of occurrences
#確切地指定的出現次數
import re
txt = "The rain in Spain falls mainly in the plain!"
#Check if the string contains "a" followed by exactly two "l" characters:
x = re.findall("al{2}", txt)
#al{2},l出現２次
print(x) #['all']
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

print("---------------------------------|：Either or 兩者任一")
#|：Either or 兩者任一
import re
txt = "The rain in Spain falls mainly in the plain!"
#Check if the string contains either "falls" or "stays":
x = re.findall("falls|stays", txt)
#x = re.compile
#compile 函數用於編譯正則表達式，生成一個正則表示式（ Pattern ）物件
#，供 match（） 和 search（） 這兩個函數使用。
print(x) #['falls']
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

print("--------------------()：Capture and group 捕獲和分組")
#()：Capture and group 捕獲和分組
