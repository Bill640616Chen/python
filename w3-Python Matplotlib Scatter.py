#https://www.w3schools.com/python/matplotlib_scatter.asp
#Python Matplotlib Scatter 繪圖庫散射
#Creating Scatter Plots 創建散射繪圖
#With Pyplot, you can use the scatter() function to draw a scatter plot.
#使用 Pyplot，您可以使用scatter()功能繪製散射圖。
#The scatter() function plots one dot for each observation. It needs two arrays of the same length, one for the values of the x-axis, and one for values on the y-axis:
#scatter()函數為每次觀察繪製一個點。它需要兩個長度相同的陣列，一個用於 x 軸的值，另一個用於 y 軸上的值：
#A simple scatter plot:
print("--------------------------------簡易散射圖")
#簡易散射圖：
from typing import ChainMap
import matplotlib.pyplot as plt
import numpy as np
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
plt.scatter(x, y,c='DeepPink')
plt.show()
#The observation in the example above is the result of 13 cars passing by.
#上例中的觀察是13輛車經過的結果。
#The X-axis shows how old the car is.
#X 軸顯示汽車的年齡。
#The Y-axis shows the speed of the car when it passes.
#Y 軸顯示汽車通過時的速度。
#Are there any relationships between the observations?
#觀測結果之間有關係嗎？
#It seems that the newer the car, the faster it drives, but that could be a coincidence, after all we only registered 13 cars.
#看來，汽車越新，開得越快，但這可能是巧合，畢竟我們只註冊了13輛車。

print("----------------------------------比較繪圖")
#Compare Plots 比較繪圖
#In the example above, there seems to be a relationship between speed and age, but what if we plot the observations from another day as well? Will the scatter plot tell us something else?
#在上面的例子中，速度和年齡之間似乎有一定的關係，但如果我們也從另一天開始繪製觀測圖呢？散射情節會告訴我們別的事情嗎？
#Draw two plots on the same figure:
#在同一圖上繪製兩個繪圖：
import matplotlib.pyplot as plt
import numpy as np
#day one, the age and speed of 13 cars:
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
plt.scatter(x, y)
#day two, the age and speed of 15 cars:
x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
plt.scatter(x, y)
plt.show()
#Note: The two plots are plotted with two different colors, by default blue and orange, you will learn how to change colors later in this chapter.
#注意：這兩個繪圖繪製有兩種不同的顏色，默認情況下是藍色和橙色，您將在本章的稍後學習如何更改顏色。
#By comparing the two plots, I think it is safe to say that they both gives us the same conclusion: the newer the car, the faster it drives.
#通過比較這兩個情節，我認為可以肯定地說，它們都給了我們相同的結論：汽車越新，開得越快。

print("--------------------------------------顏色")
#Colors 顏色
#You can set your own color for each scatter plot with the color or the c argument:
#您可以設定自己的顏色為每個散射情節與顏色或 c 參數：
#Set your own color of the markers:
#設定標記的顏色：
import matplotlib.pyplot as plt
import numpy as np
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
plt.scatter(x, y, color = 'hotpink')
x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
plt.scatter(x, y, c = '#88c999')
plt.show()

print("--------------------------------每個點的顏色")
#Color Each Dot 每個點的顏色
#You can even set a specific color for each dot by using an array of colors as value for the c argument:
#您甚至可以通過使用顏色陣列為 c 參數設定特定顏色：
#Note: You cannot use the color argument for this, only the c argument.
#注意：你不能為此使用顏色參數，只能使用 c 參數。
#Set your own color of the markers:
#設定標記的顏色：
import matplotlib.pyplot as plt
import numpy as np
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
colors = np.array(["red","green","blue","yellow","pink","#ADFF2F","orange","purple","beige","brown","gray","cyan","magenta"])
plt.scatter(x, y, c=colors)
plt.show()
#colors = np.array(["green","#ADFF2F"])可以是名稱和六價

print("------------------------------ColorMap 彩色圖")
#ColorMap 彩色圖
#The Matplotlib module has a number of available colormaps.
#Matplotlib模組有許多可用的色圖。
#A colormap is like a list of colors, where each color has a value that ranges from 0 to 100.
#色圖就像顏色清單，其中每種顏色的值範圍從 0 到 100 不等。
#Here is an example of a colormap:
#下面是色圖示例：
#This colormap is called 'viridis' and as you can see it ranges from 0, which is a purple color, and up to 100, which is a yellow color.
#此色圖稱為"viridis"，正如您所看到的，其範圍從 0（紫色）到 100（黃色）不等。
#How to Use the ColorMap 如何使用彩色圖
#You can specify the colormap with the keyword argument cmap with the value of the colormap, in this case 'viridis' which is one of the built-in colormaps available in Matplotlib.
#您可以使用帶有關鍵字參數 cmap 的色圖指定顏色圖，該圖具有色圖的價值，在此例中，是 Matplotlib 中可用的內置色圖之一。
#In addition you have to create an array with values (from 0 to 100), one value for each of the point in the scatter plot:
#此外，您還必須創建一個具有值（從 0 到 100）的陣列，散射圖中每個點的一個值：
#Create a color array, and specify a colormap in the scatter plot:
#建立顏色陣列，並在散射圖中指定顏色圖：
import matplotlib.pyplot as plt
import numpy as np
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])
plt.scatter(x, y, c=colors, cmap='Purples')
plt.show()
#cmap的種類有https://matplotlib.org/stable/tutorials/colors/colormaps.html
#You can include the colormap in the drawing by including the plt.colorbar() statement:
print("------------plt.colorbar()語句在繪圖中包括色圖")
#您可以透過包含 plt.colorbar()語句在繪圖中包括色圖：
#Include the actual colormap:
#包括實際色圖：
import matplotlib.pyplot as plt
import numpy as np
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])
plt.scatter(x, y, c=colors, cmap='viridis')
plt.colorbar()
plt.show()
#Available ColorMaps 可用彩色圖
#You can choose any of the built-in colormaps:
#您可以選擇任何內建的色圖：
#https://matplotlib.org/stable/tutorials/colors/colormaps.html
#所有的名稱後面加上_r,代表原色圖顛倒放,e.g. viridis_r

print("------------------------------------Size 大小")
#Size 大小
#You can change the size of the dots with the s argument.
#您可以通過參數更改點的大小。
#Just like colors, make sure the array for sizes has the same length as the arrays for the x- and y-axis:
#與顏色一樣，請確保大小的陣列長度與 x 軸和 y 軸的陣列長度相同：
#Set your own size for the markers:
#為標記設定您自己的大小：
import matplotlib.pyplot as plt
import numpy as np
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
sizes = np.array([20,50,100,200,500,1000,60,90,10,300,600,800,75])
plt.scatter(x, y, s=sizes)
plt.show()

print("-------------------------Alpha 阿爾法(透明度)")
#Alpha 阿爾法(透明度)
#You can adjust the transparency of the dots with the alpha argument.
#您可以使用 alpha 參數調整點的透明度。
#Just like colors, make sure the array for sizes has the same length as the arrays for the x- and y-axis:
#與顏色一樣，請確保大小的陣列長度與 x 軸和 y 軸的陣列長度相同：
#Set your own size for the markers:
#為標記設定您自己的大小：
import matplotlib.pyplot as plt
import numpy as np
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
sizes = np.array([20,50,100,200,500,1000,60,90,10,300,600,800,75])
plt.scatter(x, y, s=sizes, alpha=0.5)
plt.show()
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
sizes = np.array([20,50,100,200,500,1000,60,90,10,300,600,800,75])
a = np.array([0.1,0.2,0.5,0.3,0.7,0.9,0.4,0.6,0.4,0.3,0.5,0.1,0.2])
plt.scatter(x, y, s=sizes, alpha=a)
plt.show()
#alpha的值只能介於0到1之間

print("-------------------------結合顏色大小和阿爾法")
#Combine Color Size and Alpha 結合顏色大小和阿爾法
#You can combine a colormap with different sizes on the dots. This is best visualized if the dots are transparent:
#您可以將色圖與點上不同大小的色圖組合在一起。如果點是透明的，則最好可視化：
#Create random arrays with 100 values for x-points, y-points, colors and sizes:
#建立具有 100 個值的隨機陣列，用於 x 點、y 點、顏色和大小：
import matplotlib.pyplot as plt
import numpy as np
x = np.random.randint(100, size=(100))
y = np.random.randint(100, size=(100))
colors = np.random.randint(100, size=(100))
sizes = 10 * np.random.randint(100, size=(100))
#a = np.random.randint(0,1)
#c = np.random.randint(257)
plt.scatter(x, y, c=colors, s=sizes, alpha=0.5, cmap='nipy_spectral')
plt.colorbar()
plt.show()