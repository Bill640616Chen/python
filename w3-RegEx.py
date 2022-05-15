#https://www.w3schools.com/python/python_regex.asp
#Python RegEx (Regular Expression)正則表示式
#A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.
#RegEx 或正則表示式是形成搜索模式的字元序列。
#RegEx can be used to check if a string contains the specified search pattern.
#RegEx 可用於檢查字串是否包含指定的搜索模式。
#RegEx Module 正則表示式模組
#Python has a built-in package called re, which can be used to work with Regular Expressions.
#Python 提供名為 re 的內置包，可用於處理正則表示式。
#Import the re module:
#匯入 re 模組：
import re
print("--檢索字串以查看它是否以 「The」 開頭並以 「Spain」 結尾：")
#RegEx in Python
#When you have imported the re module, you can start using regular expressions:
#導入 re 模組後，就可以開始使用正規表示式了：
#Search the string to see if it starts with "The" and ends with "Spain":
#檢索字串以查看它是否以 「The」 開頭並以 「Spain」 結尾：
import re
#Check if the string starts with "The" and ends with "Spain":
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
#^：Starts with開始於
#.：Any character (except newline character)任何字元（換行符除外）
#*：Zero or more occurrences零次或多次出现
#$：Ends with結束於
if x:
  print("YES! We have a match!")
else:
  print("No match")

