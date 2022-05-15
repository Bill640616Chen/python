#https://www.w3schools.com/python/matplotlib_subplots.asp
#Python Matplotlib Subplots 繪圖庫子圖
#Display Multiple Plots 顯示多個繪圖
#With the subplots() function you can draw multiple plots in one figure:
#使用subplots()功能，您可以在一個圖中繪製多個繪圖：
print("------------------------------繪製 2 個繪圖")
#Draw 2 plots:繪製 2 個繪圖：
import matplotlib.pyplot as plt
import numpy as np
#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])
plt.subplot(1, 2, 1) #same as(121)
plt.plot(x,y)
#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])
plt.subplot(1, 2, 2) #same as(122)
plt.plot(x,y)
plt.show()
#subplot(nrows, ncols, index, **kwargs)
#subplot(列,欄,索引(第幾個圖))
#列欄的意思為圖的排列,索引為排第幾個圖

print("------------------------------繪製 2 個繪圖")
#The subplots() Function 子圖（） 功能
#The subplots() function takes three arguments that describes the layout of the figure.
#子圖（）函數需要三個參數來描述圖形的佈局。
#The layout is organized in rows and columns, which are represented by the first and second argument.
#佈局按列和欄進行組織，第一個和第二個參數表示。
#The third argument represents the index of the current plot.
#第三個參數表示當前繪圖的索引。
plt.subplot(1, 2, 1)
#the figure has 1 row, 2 columns, and this plot is the first plot.
#圖有 1 列， 2 欄，這個圖是第一個圖。
plt.subplot(1, 2, 2)
#the figure has 1 row, 2 columns, and this plot is the second plot.
#圖有 1 列， 2 欄，這個圖是第二個圖。
#So, if we want a figure with 2 rows an 1 column 
# (meaning that the two plots will be displayed on 
# top of each other instead of side-by-side), we 
# can write the syntax like this:
#因此，如果我們想要一個數位與 2 列 1 欄 （這意味著兩個
# 情節將顯示在一起， 而不是並排）， 我們可以寫這樣的語法：
#Draw 2 plots on top of each other:
#在彼此之上繪製 2 個繪圖：
import matplotlib.pyplot as plt
import numpy as np
#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])
plt.subplot(2, 1, 1)
plt.plot(x,y)
#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])
plt.subplot(2, 1, 2)
plt.plot(x,y)
plt.show()
#subplot(列,欄,索引(第幾個圖))
#列欄的意思為圖的排列,索引為排第幾個圖
#You can draw as many plots you like on one figure, just descibe the number of rows, columns, and the index of the plot.
#你可以在一個圖上繪製盡可能多的繪圖，只需將列數、欄數和圖的索引分除以內即可。
print("------------------------------繪製 6 個繪圖")
#Draw 6 plots: 繪製6個圖
import matplotlib.pyplot as plt
import numpy as np
#plot 1
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])
plt.subplot(2, 3, 1)
plt.plot(x,y)
#plot 2
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])
plt.subplot(2, 3, 2)
plt.plot(x,y,c='r',ls='-.',lw=1)
#plot 3
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])
plt.subplot(2, 3, 3)
plt.plot(x,y)
#plot 4
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])
plt.subplot(2, 3, 4)
plt.plot(x,y)
#plot 5
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])
plt.subplot(2, 3, 5)
plt.plot(x,y)
#plot 6
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])
plt.subplot(2, 3, 6)
plt.plot(x,y)
plt.show()

print("---------------------------------Title 標題")
#Title 標題
#You can add a title to each plot with the title() function:
#您可以在每個分頁中新增title() 功能：
#2 plots, with titles:2 個繪圖，標題：
import matplotlib.pyplot as plt
import numpy as np
#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])
plt.subplot(1, 2, 1)
plt.plot(x,y)
plt.title("SALES")
#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])
plt.subplot(1, 2, 2)
plt.plot(x,y)
plt.title("INCOME")
plt.show()

print("--------------------suptitle()-為整個圖添加標題")
#Super Title 超級標題()
#You can add a title to the entire figure with the suptitle() function:
#您可以新增標題到整個圖形與suptitle()功能：
#Add a title for the entire figure:
#為整個圖添加標題：
import matplotlib.pyplot as plt
import numpy as np
#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])
plt.subplot(1, 2, 1)
plt.plot(x,y)
plt.title("SALES")
#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])
plt.subplot(1, 2, 2)
plt.plot(x,y)
plt.title("INCOME")
plt.suptitle("MY SHOP")
plt.show()