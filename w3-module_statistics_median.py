#https://www.w3schools.com/python/ref_stat_median.asp
#statistics.median()：Calculates the median (middle value) of the given data
#計算給定資料的中位數（中間值）
#Calculate the median (middle value) of the given data:
#計算給定資料的中位數（中間值）：
# Import statistics Library
import statistics
# Calculate middle values
print(statistics.median([1, 3, 5, 7, 9, 11, 13]))
print(statistics.median([1, 3, 5, 7, 9, 11]))
print(statistics.median([-11, 5.5, -3.4, 7.1, -9, 22]))
#會先把數值做排序才會算中位數
#Definition and Usage 定義和用法
#The statistics.median() method calculates the median (middle value) of the given data set. This method also sorts the data in ascending order before calculating the median.
#該方法計算給定數據集的中位數（中間值）。此方法還在計算中位數之前按升序對數據進行排序。statistics.median()
#Tip: The mathematical formula for Median is: Median = {(n + 1) / 2}th value, where n is the number of values in a set of data. In order to calculate the median, the data must first be sorted in ascending order. The median is the number in the middle.
#提示：中位數的數學公式為：中位數 = {（n + 1） / 2}th 值，其中 n 是一組數據中的值數。為了計算中位數，必須首先按升序對數據進行排序。中位數是中間的數位。
#Note: If the number of data values is odd, it returns the exact middle value. If the number of data values is even, it returns the average of the two middle values.
#注意：如果數據值的數量為奇數，則返回確切的中間值。如果數據值的數量為偶數，則返回兩個中間值的平均值。
#Syntax　語法
#statistics.median(data)
#Parameter Values 參數值
#Parameter：Description
#data：Required. The data values to be used (can be any sequence, list or iterator)
#必填。要使用的資料值（可以是任何序列、清單或反覆運算器）
#Note: If data is empty, it returns a StatisticsError.
#注意：如果數據為空，則返回統計信息錯誤。
#Technical Details 技術細節
#Return Value:	A float value, representing the median (middle value) of the given data
#返回值：	一個值，表示給定數據的中位數（中間值）float
#Python Version:	3.4
