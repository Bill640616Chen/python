def square(x) :         # 计算平方数
     return x ** 2

y=map(square, [1,2,3,4,5])    # 计算列表各个元素的平方
print(y)
#<map object at 0x100d3d550>     # 返回迭代器
y=list(map(square, [1,2,3,4,5]))   # 使用 list() 转换为列表
#[1, 4, 9, 16, 25]
print(y)
print('--------------這裡沒用到def的函數--------------')
y=list(map(lambda x: x ** 2, [1, 2, 3, 4, 5]))   # 使用 lambda 匿名函数
#[1, 4, 9, 16, 25]
print(y)
'''
Python map（） 函數
Python 內置函數 Python 內置函數

描述
map（） 會根據提供的函數對指定序列做映射。

第一個參數 function 以參數序列中的每一個元素調用 function 函數，返回包含每次 function 函數返回值的新清單。

語法
map（） 函數語法：

map(function, iterable, ...)
參數
function -- 函數
iterable -- 一個或多個序列
返回值
Python 2.x 傳回清單。

Python 3.x 返回反覆運算器。
'''