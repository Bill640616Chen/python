#https://www.w3schools.com/python/gloss_python_indentation.asp
#Python Indentation 縮排
#Indentation refers to the spaces at the beginning of a code line.
#縮排是指代碼行開頭的空間。
#Where in other programming languages the indentation in code is for readability only, the indentation in Python is very important.
#在其他程式設計語言中，代碼中的縮排僅用於可讀性，Python 中的縮排非常重要。
#Python uses indentation to indicate a block of code.
#Python 使用縮排表示代碼塊。
if 5 > 2:
  print("Five is greater than two!")
#Python will give you an error if you skip the indentation:
#如果您跳過縮排，Python 會給你一個錯誤：
#Syntax Error: 語法錯誤：
'''if 5 > 2:
print("Five is greater than two!")
'''
#The number of spaces is up to you as a programmer, but it has to be at least one.
#作為程式師，空間的數量由您決定，但必須至少一個。
if 5 > 2:
 print("Five is greater than two!") 
if 5 > 2:
        print("Five is greater than two!") 
#You have to use the same number of spaces in the same block of code, otherwise Python will give you an error:
#您必須在同一代碼塊中使用相同數量的空間，否則 Python 會給您一個錯誤：
#Syntax Error: 語法錯誤：
'''
if 5 > 2:
 print("Five is greater than two!")
        print("Five is greater than two!")
'''
#Related Pages 相關頁面
#Python Syntax Tutorial Python 語法教程
#https://www.w3schools.com/python/python_syntax.asp
#Indentations in if statements 如果陳述中的縮排
#https://www.w3schools.com/python/gloss_python_if_indentation.asp
