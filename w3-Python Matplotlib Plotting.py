#https://www.w3schools.com/python/matplotlib_plotting.asp
#Python Matplotlib Plotting 繪圖庫標圖
#Plotting x and y points 繪圖 x 和 y 點
#The plot() function is used to draw points 
# (markers) in a diagram.
#plot()功能用於在圖表中繪製點（標記）。
#By default, the plot() function draws a line from 
# point to point.
#默認情況下，plot()函數從點到點繪製一條線。
#The function takes parameters for specifying points 
# in the diagram.
#該函數需要參數來指定圖表中的點。
#Parameter 1 is an array containing the points on 
# the x-axis.
#參數 1 是包含 x 軸上的點的陣列。
#Parameter 2 is an array containing the points on 
# the y-axis.
#參數 2 是包含 y 軸上的點的陣列。
#If we need to plot a line from (1, 3) to (8, 10), 
# we have to pass two arrays [1, 8] and [3, 10] to 
# the plot function.
#如果我們需要繪製從 （1、3） 到 （8、10） 的行，則必須
# 將兩個陣列 [1、8] 和 [3，10] 傳遞到繪圖函數。
#Draw a line in a diagram from position (1, 3) to position (8, 10):
print("--------------------------在圖表中繪製一條線")
#在圖表中繪製一條線，從位置 （1，3） 到位置 （8，10）：
import matplotlib.pyplot as plt
import numpy as np
xpoints = np.array([1, 8])
ypoints = np.array([3, 10])
plt.plot(xpoints, ypoints)
plt.show()
#plot()功能用於在圖表中繪製點（標記）
#The x-axis is the horizontal axis.
#x 軸是水平軸。
#The y-axis is the vertical axis.
#y 軸是垂直軸。

print("--------------Plotting Without Line 無線繪圖")
#Plotting Without Line 無線繪圖
#To plot only the markers, you can use shortcut string notation parameter 'o', which means 'rings'.
#要僅繪製標記，您可以使用快捷方式字串符號參數"o"，意思是"環"。
#Draw two points in the diagram, one at position (1, 3) and one in position (8, 10):
#在圖表中繪製兩點，一個在位置（1，3）和一個在位置（8，10）：
import matplotlib.pyplot as plt
import numpy as np
xpoints = np.array([1, 8])
ypoints = np.array([3, 10])
plt.plot(xpoints, ypoints, 'o')
plt.show()
#plot()功能用於在圖表中繪製點（標記）
#You will learn more about markers in the next chapter.
#您將在下一章中瞭解更多有關標記的詳細情況。

print("----------------------Multiple Points 多點")
#Multiple Points 多點
#You can plot as many points as you like, just make sure you have the same number of points in both axis.
#您可以繪製盡可能多的點，只要確保您在兩個軸中具有相同的點數。
#Draw a line in a diagram from position (1, 3) to (2, 8) then to (6, 1) and finally to position (8, 10):
#在圖表中繪製一條線，從位置 （1，3） 到 （2， 8）， 然後繪製到 （6， 1）， 最後到位置 （8， 10）：
import matplotlib.pyplot as plt
import numpy as np
xpoints = np.array([1, 2, 6, 8])
ypoints = np.array([3, 8, 1, 10])
plt.plot(xpoints, ypoints)
plt.show()

print("------------------Default X-Points 默認 X 點")
#Default X-Points 默認 X 點
#If we do not specify the points in the x-axis, they will get the default values 0, 1, 2, 3, (etc. depending on the length of the y-points.
#如果我們沒有指定 x 軸中的點，它們將獲得預設值 0、1、2、3（等取決於 y 點的長度）。
#So, if we take the same example as above, and leave out the x-points, the diagram will look like this:
#因此，如果我們以上述相同的示例為例，而將 x 點排除在外，則圖表將如下所示：
#Plotting without x-points:
#無 x 點的繪圖：
import matplotlib.pyplot as plt
import numpy as np
ypoints = np.array([3, 8, 1, 10, 5, 7])
plt.plot(ypoints)
plt.show()
#如果我們沒有指定 x 軸中的點，它們將獲得預設值 0、1、2、3等,取決於 y 點的長度
#The x-points in the example above is [0, 1, 2, 3, 4, 5].
#上表中的 x 點為 [0、1、2、3、4、5]。

