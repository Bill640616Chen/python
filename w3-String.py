#https://www.w3schools.com/python/python_strings.asp
#Python字串
#字串
#巨蛇中的字串被單個引號或雙引號包圍。
#"你好"和'你好'是一樣的。
#您可以顯示具有該功能的字串字面：print()
print("Hello")
print('Hello')
#將字串分配給可變項
#將字串分配給變數是用可變數完成的，然後用等號和字串完成：
a = "Hello"
print(a)
#多行字串
#您可以使用三個報價將多行字串分配給變數：(換行用)
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
#或三個單一報價：(換行用)
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)
#注意：結果，線路中斷處的插入位置與代碼相同。
#字串是陣列
#像許多其他流行的程式設計語言一樣，Python 中的字串是代表單碼字元的位元陣列。
#但是，Python 沒有字元數據類型，單個字元只是長度為 1 的字串。
#方形支架可用於訪問字串的元素。
#在位置 1 處取得字元（請記住第一個字元具有位置 0）：
a = "Hello, World!"#位元陣列
print(a[1])#e
#循環通過字串
#由於字串是陣列，因此我們可以用迴圈迴圈字元中的字元。for
for x in "banana":
  print(x)#從b開始往下
#字串長度
#要獲得字串的長度，請使用該功能。len()
a = "Hello, World!"
print(len(a))#13,包括標點符號跟空格
#檢查字串
#要檢查某個短語或字元是否存在於字串中，我們可以使用關鍵字。in
#檢查以下文本中是否存在「免費」：
txt = "The best things in life are free!"
print("free" in txt)
#True,因為in是檢查就變True or False
#在聲明中使用它：if
#只有在存在"免費"時才列印：
txt = "The best things in life are free!"
if "free" in txt:#當True時,才有列印
  print("Yes, 'free' is present.")
#檢查是否
#要檢查某個短語或字元是否不在字串中，我們可以使用關鍵字。not in
txt = "The best things in life are free!"
print("expensive" not in txt)#因為not in是檢查就變True or False
#在聲明中使用它：if
#僅在不存在「昂貴」時列印：
txt = "The best things in life are free!"
if "expensive" not in txt:#當True時,才有列印
  print("No, 'expensive' is NOT present.")