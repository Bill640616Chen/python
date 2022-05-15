#https://www.w3schools.com/python/python_strings_escape.asp
#Python -逃生字元
#逃生字元
#要在字串中插入非法字元，請使用逃生字元。
#逃生字元是反向拉什，然後是要插入的字元。\
#非法字元的一個例子是被雙報價包圍的字串中的雙重報價：""
#如果您在被雙報價包圍的字串中使用雙報價，則會出現錯誤：
txt = "We are the so-called 'Vikings' from the north."
#若把 'Vikings' 改為"Vikings"則出現SyntaxError: invalid syntax錯誤
print(txt)
#We are the so-called 'Vikings' from the north.
#要解決這個問題，請使用逃生字元：\"
txt = "We are the so-called \"Vikings\" from the north."
print(txt) #這個\逃生字元2個都在"前
#We are the so-called "Vikings" from the north.
#逃生字元
#Python 中使用的其他逃生字元：
txt = 'It\'s alright.' #\'
print(txt) #It's alright.
txt = "This will insert one \\ (backslash)."  #\\
print(txt) #This will insert one \ (backslash).
txt = "This will insert one  (backslash)."
print(txt) #This will insert one  (backslash).
txt = "Hello\nWorld!" #\n換行了
print(txt) 
#Hello
#World!
txt3 = "Hello\rWorld!" #\r運輸返回,第一句消除了
print(txt3) #World!
txt = "Hello\tWorld!" #\t tab鍵的空格功能
print(txt) #Hello   World!
txt = "Hello \bWorld!" #\b backspace的功能
print(txt) #HellWorld!
txt = "Hello \fWorld!" #無輸出
txt = "\110\145\154\154\157" #\ooo,三個數字經過octal value轉換後...(八角值)
print(txt) #Hello,每一組數字代表一個英文字
#A backslash followed by three integers will result in a octal value
##A反向冲击，然後是三個整數將導致八度值
txt = "\x48\x65\x6c\x6c\x6f" #\xhh,三個位元經過hex value轉換後...(六角值)
print(txt) #Hello,每一組位元代表一個英文字
#A backslash followed by an 'x' and a hex number represents a hex value
#A反向睫毛，然後是「x」和六十六十個數位表示六角形值
