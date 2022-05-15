#https://www.w3schools.com/python/python_datatypes.asp
#內置數據類型
#在程式設計中，數據類型是一個重要的概念。
#變數可以存儲不同類型的數據，不同類型的變數可以做不同的事情。
#根據預設，Python 在這些類別中內置了以下數據類型：
#文字類型：	str
#數位類型：	int, float, complex(複數)
#序列類型：	list(列表), tuple(元組), range
#映射類型：	dict(字典)
#設定類型：	set(集合), frozenset
#布林類型：	bool
#二進位類型：bytes, bytearray, memoryview
#獲取數據類型
#您可以使用該功能取得任何物件的資料類型：type()
x = 5 #<class 'int'>
print(type(x))
#在 Python 中，當您向變數分配值時，數據類型被設置為：
x = "Hello World" #str
x = 20 #int
x = 20.5 #float
x = 1j #complex複數
c = -20.3j-5.3j#用-號寫也沒關係
print (c.real)#取實部
print (c.imag)#取虛部
#-0.0,有j的都是虛部啦
#-25.6
#實跟實,虛跟虛,各獨自加減乘除
x = ["apple", "banana", "cherry"] #list列表
x = ("apple", "banana", "cherry") #tuple元組
x = (1,) #tuple元組
x = range(6) #range範圍
print(x) #range(0, 6)
x = {"name" : "John", "age" : 36} #dict,有鍵:值,字典
x = {"apple", "banana", "cherry"} #set集合
x = ({"apple", "banana", "cherry"}) #frozenset凍集合
print(x) #{'cherry', 'banana', 'apple'}
#(class) frozenset(iterable: Iterable[str] = ...)凍結集（可重置：可重置[str]
x = True #bool布靈值
x = b"Hello" #bytes位元
print(x) #b'Hello'
x = bytearray(5) #bytearray位元陣列
print(x) #bytearray(b'\x00\x00\x00\x00\x00')
x = memoryview(bytes(5)) #記憶體檢視
print(x) #<memory at 0x000002010085C1C0>
#設置特定數據類型
#如果要指定資料類型，您可以使用以下建構器功能：
x = str("Hello World")	#str	
x = int(20)	#int	
x = float(20.5)	#float	
x = complex(1j)	#complex	
x = list(("apple", "banana", "cherry"))	#list	
#有指定類型時,用雙括唬號
x = tuple(("apple", "banana", "cherry"))	#tuple	
#有指定類型時,用雙括唬號
x = range(6)	#range	
print(x)	#range(0, 6)
x = dict(name="John", age=36)	#dict
#有指定類型時,鍵不需要雙或單引號,用鍵=值,不需用冒號
print(x)	#{'name': 'John', 'age': 36}
x = set(("apple", "banana", "cherry"))	#set
#有指定類型時,用雙括唬號	
x = frozenset(("apple", "banana", "cherry"))	#frozenset
#有指定類型時,用雙括唬號	
x = bool(5)	#bool
print(x)	#True
x = bytes(5)	#bytes	
print(x)    #b'\x00\x00\x00\x00\x00'
x = bytearray(5)	#bytearray	
print(x)    #bytearray(b'\x00\x00\x00\x00\x00')
x = memoryview(bytes(5))	#memoryview
print(x)    #<memory at 0x0000019A62D0C1C0>