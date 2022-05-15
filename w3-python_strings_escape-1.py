
txt = "Hello\nWorld!" #\n換行了
print(txt) 
#Hello
#World!
txt3 = "Hello\nWorld!" #\r運輸返回,第一句消除了
print(txt3) 
#Hello
#World!
txt3 = "Hello\rWorld!" #\r運輸返回,第一句消除了
print(txt3) #World!