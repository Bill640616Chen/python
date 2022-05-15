#https://www.w3schools.com/python/ref_stat_mode.asp
#statistics.mode()：Calculates the mode (central tendency) of the given numeric or nominal data
#計算給定數位或名義資料的模式（中心趨勢）
#Calculate the mode (central tendency) of the given data:
#計算給定資料的模式（中心趨勢）：
# Import statistics Library
import statistics
# Calculate the mode
print(statistics.mode([1, 3, 3, 3, 5, 7, 7 ,9, 11]))
print(statistics.mode([1, 1, 3, -5, 7, -9, 11]))
print(statistics.mode(['red', 'green', 'blue', 'red']))
#Definition and Usage 定義和用法
#The statistics.mode() method calculates the mode (central tendency) of the given numeric or nominal data set.
#該方法計算給定數位或名義數據集的模式（中心趨勢）。statistics.mode()
#Syntax 語法
#statistics.mode(data)
#Parameter Values 參數值
#Parameter：Description
#data：Required. The data values to be used (can be any sequence, list or iterator)
#必填。要使用的資料值（可以是任何序列、清單或反覆運算器）
#Note: If data is empty, it returns a StatisticsError.
#注意：如果數據為空，則返回統計信息錯誤。
#Technical Details 技術細節
#Return Value:	A float or nominal value, representing the mode of the given data
#返回值：	A 或標稱值，表示給定數據的模式float
#Python Version:	3.4
#Change Log:	3.8: Now handles multimodal datasets (will return the first mode encountered)
#更新紀錄：	3.8：現在處理多模式資料集（將返回遇到的第一個模式）
