#https://www.w3schools.com/python/gloss_python_if_nested.asp
#Nested If
#You can have if statements inside if statements, this is called nested if statements.
#您可以在語句中提供語句，這稱為嵌套語句。ififif
x = 41
if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")
print('-------------分隔線------------')
#下面的短語句,就沒有nested if了
y=41
print("Above ten,") if y > 10 else print("and also above 20!") if y > 20 else print("but not above 20.")
#Related Pages 相關頁面
#Python If...Else Tutorial
#https://www.w3schools.com/python/python_conditions.asp
#If Statement
#https://www.w3schools.com/python/gloss_python_if_statement.asp
#If Indentation
#https://www.w3schools.com/python/gloss_python_if_indentation.asp
#Elif
#https://www.w3schools.com/python/gloss_python_elif.asp
#Else
#https://www.w3schools.com/python/gloss_python_else.asp
#Shorthand If
#https://www.w3schools.com/python/gloss_python_if_shorthand.asp
#Shorthand If Else
#https://www.w3schools.com/python/gloss_python_if_else_shorthand.asp
#If AND
#https://www.w3schools.com/python/gloss_python_if_and.asp
#If OR
#https://www.w3schools.com/python/gloss_python_if_or.asp
#The pass keyword in If
#https://www.w3schools.com/python/gloss_python_if_pass.asp