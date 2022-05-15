#https://www.w3schools.com/python/ref_file_readlines.asp
#Python File readlines() Method Python readlines
#Returns a list of lines from the file
#返回檔案中的行清單。
#Return all lines in the file, as a list where each line is an item in the list object:
#作為清單返回檔中的所有行，其中每一行都是清單物件中的一項：
f = open("demofile.txt", "r")
print(f.readlines())
#Definition and Usage 定義和用法
#The readlines() method returns a list containing each line in the file as a list item.
#readlines（） 方法返回一個清單，其中包含檔中的每一行作為清單項。
#Use the hint parameter to limit the number of lines returned. If the total number of bytes returned exceeds the specified number, no more lines are returned.
#請使用hint參數來限制返回的行數。 如果返回的位元組總數超過了指定的數目，則不會再返回任何行。
#Syntax 語法
#file.readlines(hint)
#Parameter參數：Values值
#Parameter參數：Description描述
#hint：Optional. If the number of bytes returned exceed the hint number, no more lines will be returned. Default value is  -1, which means all lines will be returned.
#hint：可選。 如果返回的位元組數超過hint數，將不再返回任何行。 默認值為 -1，這意味著將返回所有行。
#Do not return the next line if the total number of returned bytes are more than 33:
#如果返回的位元組總數大於 33，則不返回下一行：
f = open("demofile.txt", "r")
print(f.readlines(33))


