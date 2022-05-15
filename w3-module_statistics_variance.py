#https://www.w3schools.com/python/ref_stat_variance.asp
#statistics.variance()：Calculates the variance from a sample of data
#根據數據樣本計算方差
#Calculate the variance from a sample of data:
#根據資料樣本計算方差：
# Import statistics Library
import statistics
# Calculate the variance from a sample of data
print(statistics.variance([1, 3, 5, 7, 9, 11]))
print(statistics.variance([2, 2.5, 1.25, 3.1, 1.75, 2.8]))
print(statistics.variance([-11, 5.5, -3.4, 7.1]))
print(statistics.variance([1, 30, 50, 100]))
#Definition and Usage 定義和用法
#The statistics.variance() method calculates the variance from a sample of data (from a population).
#該方法根據數據樣本（來自總體）計算方差。statistics.variance()
#A large variance indicates that the data is spread out, - a small variance indicates that the data is clustered closely around the mean.
#較大的方差表示數據分散 ， 較小的方差表示數據緊密圍繞均值聚類。
#Tip: To calculate the variance of an entire population, look at the statistics.pvariance() method.
#提示：要計算整個總體的方差，請查看該方法。statistics.pvariance()
#Syntax 語法
#statistics.variance(data, xbar)
#Parameter Values 參數值
#Parameter：Description
#data：Required. The data values to be used (can be any sequence, list or iterator)
#必填。要使用的資料值（可以是任何序列、清單或反覆運算器）
#xbar：Optional. The mean of the given data. If omitted (or set to None), the mean is automatically calculated
#自選。給定數據的平均值。如果省略（或設置為"無"），則會自動計算平均值
#Note: If data has less than two values, it returns a StatisticsError.
#注意：如果數據的值少於兩個，則返回統計信息錯誤。
#Technical Details 注意：如果數據的值少於兩個，則返回統計信息錯誤。
#Return Value:	A float value, representing the sample variance of the given data
#返回值：	一個值，表示給定數據的樣本方差float
#Python Version:	3.4

