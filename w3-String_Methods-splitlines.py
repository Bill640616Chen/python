#https://www.w3schools.com/python/ref_string_splitlines.asp
#Python 字串 splitlines() Method
#Splits the string at line breaks and returns a list
#在線路中斷時拆分字串並傳回清單
#Split a string into a list where each line is a list item:
#將字串拆分成清單，其中每行為清單項目
txt = "Thank you for the music\nWelcome to the jungle"
print (txt)
x = txt.splitlines() #無字元為預設空白及True,但\n為換行符號
print(x) #['Thank you for the music', 'Welcome to the jungle']
#定義和使用
#The method splits a string into a list. The splitting is done at 
# line breaks.splitlines()
#這方法拆分字申為清單,拆分在線路中斷
#語法
#string.splitlines(keeplinebreaks)(保持線路中斷)
txt = "Thank you for the music\nWelcome to the jungle"
x = txt.splitlines(True) #保持線路中斷,意思是換行符號還在
print(x) #['Thank you for the music\n', 'Welcome to the jungle']

txt = "Thank you for the music\tWelcome to the jungle"
x = txt.splitlines() 
print(x) #['Thank you for the music\tWelcome to the jungle']
#因為\t只是tab空白鍵,並不會斷行,所以\t符號還在,整個字申並不會被拆分

txt = "Thank you for the music\nWelcome to the jungle"
x = txt.splitlines(False) #True則留\n,Fasle是不留\n
print(x) #['Thank you for the music', 'Welcome to the jungle']