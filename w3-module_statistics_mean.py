#https://www.w3schools.com/python/ref_stat_mean.asp
#statistics.mean()：Calculates the mean (average) of the given data
#計算給定資料的平均值（平均值）
#Calculate the average of the given data:
#計算給定資料的平均值：
# Import statistics Library
import statistics
# Calculate average values
print(statistics.mean([1, 3, 5, 7, 9, 11, 13]))
print(statistics.mean([1, 3, 5, 7, 9, 11]))
print(statistics.mean([-11, 5.5, -3.4, 7.1, -9, 22]))
#Definition and Usage 定義和用法
#The method calculates the mean (average) of the given data set.statistics.mean()
#該方法計算給定數據集的平均值（平均值）。statistics.mean()
#Tip: Mean = add up all the given values, then divide by how many values there are.
#提示：均值 = 將所有給定值相加，然後除以有多少個值。
#Syntax 語法
#statistics.mean(data)
#Parameter Values 參數值
#Parameter：Description
#data：Required. The data values to be used (can be any sequence, list or iterator)
#注意：如果數據為空，則返回統計信息錯誤。
#Note: If data is empty, it returns a StatisticsError.
#注意：如果數據為空，則返回統計信息錯誤。
#Technical Details 技術細節
#Return Value:	A value, representing the average of the given datafloat
#返回值：	一個值，表示給定數據的平均值float
#Python Version:	3.4
