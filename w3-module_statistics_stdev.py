#https://www.w3schools.com/python/ref_stat_stdev.asp
#statistics.stdev()：Calculates the standard deviation from a sample of data
#計算數據樣本的標準偏差
#Calculate the standard deviation of the given data:
#計算給定數據的標準偏差：
# Import statistics Library
import statistics
# Calculate the standard deviation from a sample of data
print(statistics.stdev([1, 3, 5, 7, 9, 11]))
print(statistics.stdev([2, 2.5, 1.25, 3.1, 1.75, 2.8]))
print(statistics.stdev([-11, 5.5, -3.4, 7.1]))
print(statistics.stdev([1, 30, 50, 100]))
#Definition and Usage 定義和用法
#The statistics.stdev() method calculates the standard deviation from a sample of data.
#該方法計算數據樣本的標準偏差。statistics.stdev()
#Standard deviation is a measure of how spread out the numbers are.
#標準偏差是衡量數字分佈程度的指標。
#A large standard deviation indicates that the data is spread out, - a small standard deviation indicates that the data is clustered closely around the mean.
#較大的標準差表示數據分散 ， 較小的標準差表示數據緊密圍繞均值聚類。
#Tip: Standard deviation is (unlike the Variance) expressed in the same units as the data.
#提示：標準偏差（與方差不同）以與數據相同的單位表示。
#Tip: Standard deviation is the square root of sample variance.
#提示：標準差是樣本方差的平方根。
#Tip: To calculate the standard deviation of an entire population, look at the statistics.pstdev() method. 
#提示：要計算整個總體的標準差，請查看該方法。statistics.pstdev()
#Syntax 語法
#statistics.stdev(data, xbar)
#Parameter Values 參數值
#Parameter：Description
#data：Required. The data values to be used (can be any sequence, list or iterator)
#必填。要使用的資料值（可以是任何序列、清單或反覆運算器）
#xbar：Optional. The mean of the given data. If omitted (or set to None), the mean is automatically calculated
#自選。給定數據的平均值。如果省略（或設置為"無"），則會自動計算平均值
#Note: If data has less than two values, it returns a StatisticsError. 
#注意：如果數據的值少於兩個，則返回統計信息錯誤。
#Technical Details 技術細節
#Return Value:	A float value, representing the standard deviation of the given data
#返回值：	一個值，表示給定數據的標準偏差float
#Python Version:	3.4

