#https://www.w3schools.com/python/ref_string_casefold.asp
#Python 字串 casefold() Method
#Make the string lower case:使字申全小寫
txt = "Hello, And Welcome To My World!"
x = txt.casefold()
print(x) #hello, and welcome to my world!
#定義和使用
#The method returns a string where all the characters are lower case.casefold()
#這方法返回字串上的所有位元都是小寫
#This method is similar to the method, but the method is stronger,
# more aggressive, meaning that it will convert more characters 
# into lower case, and will find more matches when comparing two s
# trings and both are converted using the method. lower()casefold()
#此方法與方法類似，但該方法更強、更具攻擊性，這意味著它將將更多字元轉換為小字，
# 並在比較兩個字串時找到更多的匹配項，並且兩者都使用該方法進行轉換。
# lower()casefold()
#語法
#string.casefold()
#參數值
#無參數