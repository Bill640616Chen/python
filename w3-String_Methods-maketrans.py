#https://www.w3schools.com/python/ref_string_maketrans.asp
#Python 字串 maketrans() Method
#Returns a translation table to be used in translations
#建立映射表，並在方法中將其替換為「P」字元的任何「S」字元：translate()
txt = "Hello Sam!"
mytable = txt.maketrans("S", "P") #把S取代為P
#maketrans會把字元映射為unicode碼,translate則把unicode轉為字元
print(txt.translate(mytable)) #Hello Pam!
#在w3-修改字申.py的第21行
a = "Hello, World!"
print(a.replace("H", "J"))#Jello, World!
#定義和使用
#該方法返回可與該方法一起替換指定字元的映射表。maketrans() translate()
#語法
#string.maketrans(x, y, z)
#參數值
#Parameter(參數)：Description(描述)
#x：Required(必填). If only one parameter is specified, this has to be
#  a dictionary describing how to perform the replace. If two or more 
# parameters are specified, this parameter has to be a string specifying
#  the characters you want to replace.
#如果只指定了一個參數，則必須是描述如何執行替換的字典。如果指定了兩個或多個參數，
# 則此參數必須是一個字串，指定要替換的字元。
#y：Optional(自選). A string with the same length as parameter x. 
# Each character in the first parameter will be replaced with the 
# corresponding character in this string.
#長度與參數 x 相同的字串。第一個參數中的每個字元將被此字串中的相應字元替換。
#z：Optional(自選). A string describing which characters to remove from
#  the original string.
#描述從原始字串中刪除哪些字元。
#使用映射表取代許多字元：
txt = "Hi Sam!"
x = "mSa" #(代表哪幾個字元要取代)
y = "eJo" #與x的字申值字元互換,但順序是原始字串的順序
mytable = txt.maketrans(x, y)
#maketrans把x,y的值製作成字典型的翻譯表unicode
print (mytable) #透過maketrans印出下面的字典
#m鍵的值是e,S鍵的值是J,a鍵的值是o,所以y變數的字元都完成替換
#Sam替換成Joe
#{109m: 101e, 83S: 74J, 97a: 111o},值替換為鍵
#x,y的字申值中字元的排序很重要!!!
print(txt.translate(mytable))
#Hi Joe! #translate給我的感覺是把字典變字串

txt = "Hi Sam!"
x = "mSi" #(鍵)
y = "eJo" #(值)
mytable = txt.maketrans(x, y)
print (mytable) 
#{109m: 101e, 83S: 74J, 105i: 111o}
print(txt.translate(mytable)) 
#Ho Jae! #translate給我的感覺是把字典變字串
#maketrans會把字元映射為unicode碼,translate則把unicode轉為字元

txt = "Good night Sam!"
x = "mSa"
y = "eJo"
z = "odnght" #刪除原始字串的相關字元
mytable = txt.maketrans(x, y, z)
print(txt.translate(mytable)) #translate給我的感覺是把字典變字串
#{109m: 101e, 83S: 74J, 97a: 111o, 111o: None, 100d: None, 110n: None, 103g: None, 104h: None, 
#116t: None}
#G i Joe!

#該方法本身返回一本字典，描述每個替換，在單代碼：maketrans()
txt = "Good night Sam!"
x = "mSa"
y = "eJo"
z = "odnght"
print(txt.maketrans(x, y, z))
#{109m: 101e, 83S: 74J, 97a: 111o, 111o: None, 100d: None, 110n: None, 103g: None, 104h: None, 
#116t: None}

myDict = {"name": "John", "country": "Norway"}
x = "#".join(myDict) #"#"為散列字元當作分離器
print(x) #name#country,只有鍵被#隔開
#iterable應該可以拆分任何一種形式的陣列,用符號或字元隔開裡面的字申
#注意：當使用字典作為可重做時，返回的值是密鑰，而不是值。(錯誤翻譯)
#Note: When using a dictionary as an iterable, the returned values are the keys, not the values.
#注意：當使用字典當作序列,返回的都是鍵,而不是值
print(x.split("#")) #待號就是密鑰
#['name', 'country']

#以下為測試輸出的值可以返回原字典格式
myDict = {"name": "John", "country": "Norway"}
x = "#".join(myDict)
print(x) 
##name#country
print(x.split("#"))
#['name', 'country']

