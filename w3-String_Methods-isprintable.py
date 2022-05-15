#https://www.w3schools.com/python/ref_string_isprintable.asp
#Python 字串 isprintable() Method
#檢查文字中的所有字元是否可列印：
txt = "Hello! Are you #1?"
x = txt.isprintable()
print(x) #True
#定義和使用
#如果所有字元都是可列印的，否則錯誤，則方法返回 True。isprintable()
#無可列印字元的示例可以是運輸返回和線路饋送。
#語法
#string.isprintable()
#檢查文字中的所有字元是否可列印：
txt = "Hello!\nAre you #1?" #\n是換行的意思()
x = txt.isprintable()
print(x) #False