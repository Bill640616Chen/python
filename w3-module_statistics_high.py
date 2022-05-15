#https://www.w3schools.com/python/ref_stat_median_high.asp
#statistics.median_high()：Calculates the high median of the given data
#計算給定數據的最高中位數
#Calculate the high median (middle value) of the given data:
#計算給定數據的高中位數（中間值）：
# Import statistics Library
import statistics
# Calculate the high middle values
print(statistics.median_high([1, 3, 5, 7, 9, 11, 13]))
print(statistics.median_high([1, 3, 5, 7, 9, 11]))
print(statistics.median_high([-11, 5.5, -3.4, 7.1, -9, 22]))
#Definition and Usage 定義和用法
#The statistics.median_high() method calculates the high median of the given data set. This method also sorts the data in ascending order before calculating the high median.
#該方法計算給定數據集的高中位數。此方法還在計算高中位數之前按升序對數據進行排序。statistics.median_high()
#Note: If the number of data values is odd, it returns the exact middle value. If the number of data values is even, it returns the larger of the two middle values.
#注意：如果數據值的數量為奇數，則返回確切的中間值。如果數據值的數量為偶數，則返回兩個中間值中較大的一個。
#Syntax 語法
#statistics.median_high(data)
#Parameter Values 參數值
#Parameter：Description
#data：Required. The data values to be used (can be any sequence, list or iterator)
#必填。要使用的資料值（可以是任何序列、清單或反覆運算器）
#Note: If data is empty, it returns a StatisticsError.
#注意：如果數據為空，則返回統計信息錯誤。
#Technical Details 技術細節
#Return Value:	A float value, representing the high median (middle value) of the given data
#返回值：	一個值，表示給定數據的高中位數（中間值）float
#Python Version:	3.4


