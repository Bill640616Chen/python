#https://www.w3schools.com/python/ref_func_zip.asp
#Python zip() Function Python zip()函數
#Returns an iterator, from two or more iterators
#從兩個或多個反覆運算器返回一個反覆運算器。
#Join two tuples together:
#把兩個元組連接起來：
a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica")
x = zip(a, b)
#use the tuple() function to display a readable version of the result:
#使用 Tuple （） 功能顯示結果的可讀版本：
print(tuple(x))
#Definition and Usage 定義和用法
#The zip() function returns a zip object, which is an iterator of tuples where the first item in each passed iterator is paired together, and then the second item in each passed iterator are paired together etc.
#zip（） 函數返回 zip 物件，它是元組的反覆運算器，其中每個傳遞的反覆運算器中的第一項配對在一起，然後每個傳遞的反覆運算器中的第二項配對在一起，依此類推。
#If the passed iterators have different lengths, the iterator with the least items decides the length of the new iterator.
#如果傳遞的反覆運算器具有不同的長度，則專案數最少的反覆運算器將決定新反覆運算器的長度。
#Syntax 語法
#zip(iterator1, iterator2, iterator3 ...)
#Parameter參數：Values值
#Parameter參數：Description描述
#iterator1, iterator2, iterator3 ...	Iterator objects that will be joined together
#iterator1, iterator2, iterator3 ...	被連接在一起的反覆運算器物件。
#If one tuple contains more items, these items are ignored:
#如果一個元組包含更多項，則將忽略這些項：
a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica", "Vicky")
x = zip(a, b)
#use the tuple() function to display a readable version of the result:
#使用 Tuple （） 功能顯示結果的可讀版本：
print(x) #<zip object at 0x000001B8940E4D40>
print(tuple(x))
