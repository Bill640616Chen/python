#https://www.w3schools.com/python/ref_stat_median_grouped.asp
#statistics.median_grouped()：Calculates the median of grouped continuous data
#計算分組連續數據的中位數
#Calculate the median of grouped continuous data:
#計算群組連續資料的中位數：
# Import statistics Library
import statistics
# Calculate the median of grouped continuous data
print(statistics.median_grouped([1, 2, 3, 4]))
print(statistics.median_grouped([1, 2, 3, 4, 5]))
print(statistics.median_grouped([1, 2, 3, 4], 2))
print(statistics.median_grouped([1, 2, 3, 4], 3))
print(statistics.median_grouped([1, 2, 3, 4], 5))
#Definition and Usage 定義和用法
#The statistics.median_grouped() method calculates the median of grouped continuous data, calculated as the 50th percentile.
#該方法計算分組連續數據的中位數，計算為第50個百分位數。statistics.median_grouped()
#This method treats the data points as continuous data and calculates the 50% percentile median by first finding the median range using specified interval width (default is 1), and then interpolating within that range using the position of the values from the data set that fall in that range.
#此方法將數據點視為連續數據，並通過以下方式計算 50% 的百分位中位數：首先使用指定的區間寬度（預設值為 1）查找中位數範圍，然後使用落在該範圍內的數據集中的值的位置在該範圍內進行插值。
#Tip: The mathematical formula for Grouped Median is: GMedian = L + interval * (N / 2 - CF) / F.
#提示：分組中位數的數學公式為：GMedian = L + interval * （N / 2 - CF） / F。
#L = The lower limit of the median interval
#L = 中位數區間的下限
#interval = The interval width
#間隔 = 間隔寬度
#N = The total number of data points
#N = 資料點的總數
#CF = The number of data points below the median interval
#CF = 低於中位數間隔的數據點數
#F = The number of data points in the median interval
#F = 中位數區間中的數據點數
#Syntax 語法
#statistics.median_grouped(data, interval)
#Parameter Values 參數值
#Parameter：Description
#data：Required. The data values to be used (can be any sequence, list or iterator)
#必填。要使用的資料值（可以是任何序列、清單或反覆運算器）
#interval：Optional. The class interval. Default value is 1
#自選。類間隔。預設值為 1
#Note: If data is empty, it returns a StatisticsError.
#注意：如果數據為空，則返回統計信息錯誤。
#Technical Details 技術細節
#Return Value:	A float value, representing the median of grouped continuous data, calculated as the 50th percentile
#返回值：	一個值，表示分組連續數據的中位數，計算為第 50 個百分位數float
#Python Version:	3.4

