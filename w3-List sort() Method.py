#https://www.w3schools.com/python/ref_list_sort.asp
#Python List sort() Method 對清單進行排序方法
#對清單進行排序
print("-------------------sort elenmant順序測試")
#Sort the list alphabetically:
#按照字母排序
cars = ['Ford', 'BMW', 'Volvo']
cars.sort()
print(cars) #['BMW', 'Ford', 'Volvo']
print("-------------------sort Ab大小寫的順序測試")
cars = ['a', 'A', 'b','C']
cars.sort()
print(cars) #['A', 'C', 'a', 'b']先排大寫再排小寫
print("-------------------sort 負數與整數的順序測試")
cars = ['-3', '-5', '-1','-6','0']
cars.sort()
print(cars) #['-1', '-3', '-5', '-6', '0']在負數裡0放最後
print("-------------------sort 負數與整數的順序測試")
cars = ['2', '1', '0','5']
cars1 = ['-3','-1','-6','0']
cars.sort()
print(cars) #['0', '1', '2', '5'] 
print(cars.sort()) #None測試,皆為就地變值in-place
print(cars1.sort()) #None測試,皆為就地變值in-place
print(cars+cars1) #['0', '1', '2', '5', '-1', '-3', '-6', '0']
#Definition and Usage
#The sort() method sorts the list ascending by default.
#預設的sort()方法,按照上升的方式排序清單
#例：[6,3,5]-->[3,5,6],abc亦同,先排大寫再排小寫
print("------------reverse您還可以做一個函數來決定排序標準")
#You can also make a function to decide the sorting criteria(s).
#您還可以做一個函數來決定排序標準。
#Syntax
#list.sort(reverse=True|False, key=myFunc)
#sort的參數專用關鍵字key,不能更改,keyword argument for sort()
#當語法參數為自選時,代表參數非必填
#Parameter Values
#Parameter(參數)：Description(描述)
#reverse(反轉)：Optional(自選). 
#reverse=True will sort the list descending. Default is reverse=False
#key(key功能)：Optional(自選).
#A function to specify the sorting criteria(s)
#Sort the list descending:降幂排列
cars = ['Ford', 'BMW', 'Volvo']
cars.sort(reverse=True)
print(cars)
print("------------key=myFunc您還可以自訂函數來決定排序標準(此例為len)")
# A function that returns the length of the value:
#按照字串的長度排序的功能
def myFunc(e):
  return len(e)
#上面定義了一個功能函數,用來測量字串的長度
cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']
cars.sort(key=myFunc)
#key(key: (_p0: str) -> SupportsLessThan)=myFunc(傳回清單裡字串長度)
#每測量完一個字串就把值丟給key,然後key就執行SupportsLessThan(從最小值開始)
#所以字串最短的就傳回給cars
print(cars) #['VW', 'BMW', 'Ford', 'Mitsubishi']

print("------------key=myFunc您還可以自訂函數來決定排序標準(此例為傳回值)")
#Sort a list of dictionaries based on the "year" value of the dictionaries:
# A function that returns the 'year' value:
def myFunc(e):
  return e['year']
cars = [
  {'car': 'Ford', 'year': 2005},
  {'car': 'Mitsubishi', 'year': 2000},
  {'car': 'BMW', 'year': 2019},
  {'car': 'VW', 'year': 2011}
]
cars.sort(key=myFunc)
#key(key: (_p0: str) -> SupportsLessThan)=myFunc(傳回清單指定鍵的值)
#每傳完一個鍵就把值丟給key,然後key就執行SupportsLessThan(從最小值開始)
#所以最小值產生的鍵值的就傳回給cars
print(cars)

print("------------list.sort(reverse=True|False, key=myFunc)")
#Sort the list by the length of the values and reversed:

# A function that returns the length of the value:
def myFunc(e):
  return len(e)
cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']
cars.sort(reverse=True, key=myFunc)
#key=myFunc(測量字串的長度)本來按照長度排['VW', 'BMW', 'Ford', 'Mitsubishi']
#然後再執行reverse=True,把key=myFunc輸出的清單,反序排列
#['Mitsubishi', 'Ford', 'BMW', 'VW']
print(cars)
