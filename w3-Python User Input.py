#https://www.w3schools.com/python/python_user_input.asp
#User Input 使用者輸入。
#Python allows for user input.
#Python允許使用者輸入
#That means we are able to ask the user for input.
#這意味著我們能夠要求用戶輸入。
#The method is a bit different in Python 3.6 than Python 2.7.
#Python 3.6 中的方法與 Python 2.7 略有不同。
#Python 3.6 uses the input() method.
#Python 3.6 使用 input（） 方法。
#Python 2.7 uses the raw_input() method.
#Python 2.7 使用 raw_input（） 方法。
#The following example asks for the username, and when you entered the username, it gets printed on the screen:
#下面的例子會詢問使用者的姓名，當您輸入名字時，名字將列印到螢幕上：
#Python 3.6
username = input("Enter username:")
print("Username is: " + username)
#Python 2.7
username = raw_input("Enter username:")
print("Username is: " + username)
#Python stops executing when it comes to the input() function, 
# and continues when the user has given some input.
#Python 停止執行輸入 （） 功能，並在使用者提供一些輸入時繼續執行。