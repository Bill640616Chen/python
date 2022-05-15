#https://www.w3schools.com/python/matplotlib_line.asp
#Python Matplotlib Line 繪圖庫線
#Linestyle 線型
#You can use the keyword argument linestyle, or shorter ls, to change the style of the plotted line:
#您可以使用關鍵字參數行樣式或較短的 ls 來更改繪圖行的樣式：
print("---------------------------------使用點虛線")
#Use a dotted line:使用點虛線：
import matplotlib.pyplot as plt
import numpy as np
ypoints = np.array([3, 8, 1, 10])
plt.plot(ypoints, linestyle = 'dotted')
plt.show()
print("---------------------------------使用線虛線")
#Use a dashed line:使用線虛線：
plt.plot(ypoints, linestyle = 'dashed')
plt.show()

print("------------------------Shorter Syntax更短的語法")
#Shorter Syntax更短的語法
#The line style can be written in a shorter syntax:
#線樣式可以用較短的語法書寫：
#linestyle can be written as ls
#線型可以寫成 ls 。
#dotted can be written as :
#點虛線可以寫為 ：
#dashed can be written as --
#線可以寫成--
#Shorter syntax:更短的語法
plt.plot(ypoints, ls = ':')
plt.show()
plt.plot(ypoints,'--')
plt.show()

print("------------------------------------線樣式")
#Line Styles 線樣式
#You can choose any of these styles:
#您可以選擇以下任何樣式：
plt.plot(ypoints, '-') #Solid line實心線
plt.show()
plt.plot(ypoints, ':') #Dotted line點虛線
plt.show()
plt.plot(ypoints, '--') #Dashed line線虛線	
plt.show()
plt.plot(ypoints, '-.') #dashdot line虛線/虛線(線+點)
plt.show()
plt.plot(ypoints, 'or') #None line(只有點沒有線)
plt.show()

print("------------------------------------線顏色")
#Line Color 線顏色
#You can use the keyword argument color or the shorter c to set the color of the line:
#您可以使用關鍵字參數顏色或較短的 c 來設定列的顏色：
#Set the line color to red:將線顏色設定為紅色：
import matplotlib.pyplot as plt
import numpy as np
ypoints = np.array([3, 8, 1, 10])
plt.plot(ypoints, color = 'HotPink')
plt.show()
#color = "六價色值"或"顏色名稱"
#六價色值https://www.w3schools.com/colors/colors_hexadecimal.asp
#顏色名稱https://www.w3schools.com/colors/colors_names.asp

print("------------------------------------線寬度")
#Line Width 線寬度
#You can use the keyword argument linewidth or the shorter lw to change the width of the line.
#您可以使用關鍵字參數線寬或較短的 lw 來更改線的寬度。
#The value is a floating number, in points:
#值是一個浮動數位，在點：
#Plot with a 10.5pt wide line:
#具有 10.5pt 寬線的繪圖：
import matplotlib.pyplot as plt
import numpy as np
ypoints = np.array([3, 8, 1, 10])
plt.plot(ypoints, linewidth = '10.5')
plt.show()

print("------------------------------------多行")
#Multiple Lines 多行
#You can plot as many lines as you like by simply adding more plt.plot() functions:
#只需添加更多 plt.plot（） 功能，即可繪製盡可能多的行圖。
#Draw two lines by specifying a plt.plot() function for each line:
#透過指定每行的 plt.plot（） 功能來繪製兩行：
import matplotlib.pyplot as plt
import numpy as np
y1 = np.array([3, 8, 1, 10])
y2 = np.array([6, 2, 7, 11])
y3 = np.array([1, 5, 2, 8])
plt.plot(y1,label='y1')
plt.plot(y2,label='y2')
plt.plot(y3,label='y3')
plt.legend()
plt.show()
#plt.legend()以plot()裡的label當標籤
#plt.legend([y1,y2,y3])列印陣列當作標籤
#plt.plot(y1,label=y1)列印陣列當作標籤,功能不見了
#plt.plot(y2,label=y2)列印陣列當作標籤,功能不見了
#plt.plot(y3,label=y3)列印陣列當作標籤,功能不見了
#You can also plot many lines by adding the points for the x- and y-axis for each line in the same plt.plot() function.
#您也可以通過添加同一 plt.plot （） 功能中每行 x 和 y 軸的點來繪製許多行。
#(In the examples above we only specified the points on the y-axis, meaning that the points on the x-axis got the the default values (0, 1, 2, 3).)
#（在上面的示例中，我們只指定了 y 軸上的點，這意味著 x 軸上的點得到了預設值 （0、1、2、3）。
#The x- and y- values come in pairs:
#x 值與 y 值成對：
#Draw two lines by specifiyng the x- and y-point values for both lines:
print("---------------按兩行的 x 點和 y 點值的規格繪製兩行")
#按兩行的 x 點和 y 點值的規格繪製兩行：
import matplotlib.pyplot as plt
import numpy as np
x1 = np.array([0, 1, 2, 3])
y1 = np.array([3, 8, 1, 10])
x2 = np.array([0, 1, 2, 3])
y2 = np.array([6, 2, 7, 11])
plt.plot(x1, y1, x2, y2)
plt.show()

