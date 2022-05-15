#https://www.w3schools.com/python/python_strings_slicing.asp
#Python -切片字串Slicing Strings
#切片
#您可以使用切片語法返回一系列字元。
#指定開始索引和結束索引（由結腸分離）以返回字串的一部分。
#將字元從位置 2 取得到位置 5（不包括）：
b = "Hello, World!"
print(b[2:5]) #[左:右],llo
#注意：第一個字元有索引 0。由0開始是左到右的順序,標點待號&空格都算
#從一開始就切片
#通過排除起始索引，範圍將從第一個字元開始：
#從頭到尾獲取字元到位置 5（不包括）：
b = "Hello, World!"
print(b[:5])#從0開始只到位置4,Hello
#切片到最後
#將最終指數排除在外，範圍將結束：
#從位置 2 獲取字元，一直到最後：
b = "Hello, World!"
print(b[2:])#llo, World!
#負索引,由-1開始由右至左的順序
#使用負索引從字串末尾開始切片：
#抓取字元：
#從： "o" 在 "世界！（位置 -5）
#到， 但不包括： "d" 在 "世界！（位置 -2）：
b = "Hello, World!"
print(b[-5:-2]) #[左:右],orl
