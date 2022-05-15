#https://www.w3schools.com/python/ref_list_append.asp
#Python List List append() Methods 清單新增方法

print("------------------測試Add 2 list to a list:")
a = ["apple", "banana", "cherry"]
b = ["Ford", "BMW", "Volvo"]
c = ["Ford", "BMW"]
b.append(c) #先把c放進b
a.append(b) #再把新b放進a
print(a)
#['apple', 'banana', 'cherry', ['Ford', 'BMW', 'Volvo', ['Ford', 'BMW']]]     
print("-----測試輸出為None時,用in-place把值輸出 測試 a.append(b.append(c))")
a = ["apple", "banana", "cherry"]
b = ["Ford", "BMW", "Volvo"]
c = ["Ford", "BMW"]
a.append(b.append(c)) #b.append(c)為None
print(a)
#['apple', 'banana', 'cherry', None]
print(a+b+c)
#print(a)====a變成['apple', 'banana', 'cherry', None]
#b.append(c)====b變成['Ford', 'BMW', 'Volvo',['Ford', 'BMW']]
#c還是'Ford', 'BMW'
#['apple', 'banana', 'cherry', None, 'Ford', 'BMW', 'Volvo',
# ['Ford', 'BMW'], 'Ford', 'BMW']
print("---------測試輸出為None時,用in-place把值輸出 print(a.append(b))")
a = ["apple", "banana", "cherry"]
b = ["Ford", "BMW", "Volvo"]
print(a.append(b)) #None
print(a+b)
#a.append(b)====a變成['apple', 'banana', 'cherry', ['Ford', 'BMW', 'Volvo']
#b還是"Ford", "BMW", "Volvo"
#['apple', 'banana', 'cherry', ['Ford', 'BMW', 'Volvo'],
#  'Ford', 'BMW', 'Volvo']