#https://www.w3schools.com/python/ref_cmath_isclose.asp
#Python cmath.isclose() Method
#Compare the closeness of two complex values:
#比較兩個複數值的接近度：
#Import cmath Library
import cmath
#compare the closeness of two complex values using relative tolerance
print(cmath.isclose(10+5j, 10+5j))
print(cmath.isclose(10+5j, 10.01+5j))
#Definition and Usage 定義和用法
#The method checks whether two complex values are close, or not. This method returns a Boolean value: if the values are close, otherwise .cmath.isclose()TrueFalse
#該方法檢查兩個複數值是否接近。此方法傳回一個布林值：如果值接近，否則 。cmath.isclose()TrueFalse
#This method uses a relative tolerance, or an absolute tolerance, to see if the values are close.
#此方法使用相對公差或絕對公差來查看值是否接近。
#Tip: It uses the following formula to compare the values:
#abs(a-b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)
#提示：它使用以下公式來比較這些值：abs（a-b）
#<= max（rel_tol * max（abs（a），abs（b）），abs_tol）
#Syntax 語法
#cmath.isclose(a, b, rel_tol = value, abs_tol = value)
#Parameter Values 參數值
#Parameter：Description
#a：Required. The first value to check for closeness
#必填。檢查接近度的第一個值
#b：Required. The second value to check for closeness
#必填。檢查接近度的第二個值
#rel_tol = value：Optional. The relative tolerance. It is the maximum allowed difference between value a and b. Default value is 1e-09
#自選。相對公差。它是值 a 和 b 之間允許的最大差值。預設值為 1e-09
#abs_tol = value：Optional. The minimum absolute tolerance. It is used to compare values near 0. The value must be at least 0
#自選。最小絕對公差。它用於比較接近 0 的值。該值必須至少為 0
#Technical Details 技術細節
#Return Value:：A value. if the values are close, otherwise boolTrueFalse
#返回值：	值。 如果值接近，否則bool True False
#Python Version:	3.5
#Compare the closeness of two complex values where absolute tolerance is defined:
#比較定義了絕對公差的兩個複數值的接近度：
#Import cmath Library
import cmath
#compare the closeness of two complex values using absolute tolerance
print(cmath.isclose(10+5j, 10+5j, abs_tol=0.005))
print(cmath.isclose(10+5j, 10.01+5j, abs_tol=0.005))
