#https://www.w3schools.com/python/gloss_python_multi_line_comments.asp
#Python multi_line_comments 多行注解
#Python does not really have a syntax for multi line comments.
#Python 實際上沒有多行評論的語法。
#To add a multiline comment you could insert a # for each line:
#要添加多行註釋，您可以為每行插入一個：#
#This is a comment
#written in
#more than just one line
print("Hello, World!")
#Or, not quite as intended, you can use a multiline string.
#或者，不能完全按預期使用多行字串。
#Since Python will ignore string literals that are not assigned to a variable, you can add a multiline string (triple quotes) in your code, and place your comment inside it:
#由於 Python 將忽略未分配給變數的字串字面，因此您可以在代碼中添加多行字串（三重報價），並將您的注釋放入其中：
"""
This is a comment
written in
more than just one line
"""
print("Hello, World!")
#As long as the string is not assigned to a variable, Python will read the code, but then ignore it, and you have made a multiline comment.
#只要字串未分配到變數，Python 將讀取代碼，但隨後忽略它，並且您已進行了多行評論。
#Related Pages 相關頁面
#Python Comments Tutorial Python 評論教程
#https://www.w3schools.com/python/python_comments.asp
#Single Line Comments 單行註釋
#https://www.w3schools.com/python/gloss_python_comments.asp
