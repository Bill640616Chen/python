#https://www.w3schools.com/python/ref_func_print.asp
#Python print() Function Python print()函數
#Prints to the standard output device
#列印標準輸出設備。
#Print a message onto the screen:
#將訊息列印到螢幕上：
print("Hello World")
#Definition and Usage 定義和用法
#The print() function prints the specified message to the screen, or other standard output device.
#print（） 函數將指定的消息列印到螢幕或其他標準輸出設備上。
#The message can be a string, or any other object, the object will be converted into a string before written to the screen.
#該消息可以是字串，也可以是任何其他物件，該對象在寫到螢幕之前會被轉換為字串。
#Syntax 語法
#print(object(s), sep=separator, end=end, file=file, flush=flush)
#Parameter參數：Values值
#Parameter參數：Description描述
#object(s)：Any object, and as many as you like. Will be converted to string before printed
#object(s)：任何物件，以及任意數量。 列印前將轉換為字串。
#sep='separator'	Optional. Specify how to separate the objects, if there is more than one. Default is ' '
#sep='separator' 可選。 指定如何分隔物件，如果存在多個物件。 預設值為 ' '。
#end='end'	Optional. Specify what to print at the end. Default is '\n' (line feed)
#end='end' 可選。 可選的。 指定要在末尾列印的內容。 預設值為 『n』（換行符）。
#file：Optional. An object with a write method. Default is sys.stdout
#file：可選。 有寫入方法的物件。 默認為 sys.stdout。
#flush：Optional. A Boolean, specifying if the output is flushed (True) or buffered (False). Default is False
#flush：可選的。 布爾值，指定輸出是刷新（True）還是緩衝（False）。 默認為 False。
#Print more than one object:
#列印多個物件：
print("Hello", "how are you?")
#Print a tuple:
#列印元組：
x = ("apple", "banana", "cherry")
print(x)
#Print two messages, and specify the separator:
#列印兩條消息，並規定分隔符：
print("Hello", "how are you?", sep="---")

