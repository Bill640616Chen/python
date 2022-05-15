#https://www.w3schools.com/python/ref_keyword_elif.asp
#Python Keyword elif 關鍵字 elif
#Used in conditional statements, same as else if
#在條件語句中使用，等同於else if。
#Print "YES" if the variable i is a positive number, print "WHATEVER" if i is 0, otherwise print "NO":
#如果變數 i 是正數，則列印 「YES」，如果 i 是 0 則列印 「WHATEVER」，否則列印 「NO」：
for i in range(-5, 5):
  if i > 0:
    print("YES")
  elif i == 0:
    print("WHATEVER")
  else:
    print("NO")
#Definition and Usage 定義和用法
#The elif keyword is used in conditional statements (if statements), and is short for else if.
#elif 關鍵字用在條件語句（if 語句）中，它是 else if 的簡寫。
#Related Pages 相關頁面
#The if keyword.
#The else keyword.
#Read more about conditional statements in our Python Conditions Tutorial.
#請在我們的 Python 條件 中學習更多條件語句的知識。