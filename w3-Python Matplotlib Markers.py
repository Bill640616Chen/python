#https://www.w3schools.com/python/matplotlib_markers.asp
#Python Matplotlib Markers 繪圖庫標記
#Markers 標記
#You can use the keyword argument marker to emphasize each point with a specified marker:
#您可以使用關鍵字參數標記來強調每個點，並指定標記：
print("--------------------------用圓圈標記每個點")
#Mark each point with a circle: 用圓圈標記每個點：
import matplotlib.pyplot as plt
import numpy as np
ypoints = np.array([3, 8, 1, 10])
plt.plot(ypoints, marker = 'o')
plt.show()
#用星標記每個點：
plt.plot(ypoints, marker = '*')
plt.show()
#Marker Reference 標記參考
#You can choose any of these markers:
#您可以選擇以下任何標記：
plt.plot(ypoints, marker = '.') #Point
plt.show()
plt.plot(ypoints, marker = ',') #Pixel
plt.show()
plt.plot(ypoints, marker = 'x') #X
plt.show()
plt.plot(ypoints, marker = 'X') #X (filled)
plt.show()
plt.plot(ypoints, marker = '+') #Plus
plt.show()
plt.plot(ypoints, marker = 'P') #Plus (filled)	
plt.show()
plt.plot(ypoints, marker = 's') #Square
plt.show()
plt.plot(ypoints, marker = 'D') #Diamond
plt.show()
plt.plot(ypoints, marker = 'd') #Diamond (thin)	
plt.show()
plt.plot(ypoints, marker = 'p') #Pentagon五角形
plt.show()
plt.plot(ypoints, marker = 'H') #Hexagon六角形
plt.show()
plt.plot(ypoints, marker = 'h') #Hexagon六角形
plt.show()
plt.plot(ypoints, marker = 'v') #Triangle Down倒三角	
plt.show()
plt.plot(ypoints, marker = '^') #Triangle Up正三角	
plt.show()
plt.plot(ypoints, marker = '<') #Triangle Left左三角
plt.show()
plt.plot(ypoints, marker = '>') #Triangle Right右三角
plt.show()
plt.plot(ypoints, marker = '1') #Tri Down
plt.show()
plt.plot(ypoints, marker = '2') #Tri Up
plt.show()
plt.plot(ypoints, marker = '3') #Tri Left
plt.show()
plt.plot(ypoints, marker = '4') #Tri Right
plt.show()
plt.plot(ypoints, marker = '|') #Vline垂直線
plt.show()
plt.plot(ypoints, marker = '_') #Hline水平線
plt.show()

print("---------------用圓圈標記每個點,'o:r'(r:紅色)")
#Format Strings fmt 格式字串 fmt
#You can use also use the shortcut string notation parameter to specify the marker.
#您也可以使用快捷方式字串符號參數來指定標記。
#This parameter is also called fmt, and is written with this syntax:
#此參數也稱為 fmt，並用此語法編寫：
#marker|line|color
#標記|線|顏色
#Mark each point with a circle:
#用圓圈標記每個點：
import matplotlib.pyplot as plt
import numpy as np
ypoints = np.array([3, 8, 1, 10])
plt.plot(ypoints, 'o:r')
plt.show()
#The marker value can be anything from the Marker Reference above.
#標記值可以是上面的標記參考的任何東西。
#The line value can be one of the following:
#線值可以是以下值之一：
print("------------------------------------線參考")
#Line Reference
#線參考
plt.plot(ypoints, '-') #Solid line實心線
plt.show()
plt.plot(ypoints, ':') #Dotted line點虛線
plt.show()
plt.plot(ypoints, '--') #Dashed line線虛線	
plt.show()
plt.plot(ypoints, '-.') #Dashed/dotted line虛線/虛線(線+點)
plt.show()
#Note: If you leave out the line value in the fmt parameter, no line will be plottet.
#注意：如果遺漏了 fmt 參數中的線值，則不會繪製任何線。
#The short color value can be one of the following:
#短色值可是以下顏色之一：

print("----------------------------------顏色參考")
#Color Reference
#顏色參考
plt.plot(ypoints, 'r') #Red紅色
plt.show()
plt.plot(ypoints, 'g') #Green綠色
plt.show()
plt.plot(ypoints, 'b') #Blue藍色
plt.show()
plt.plot(ypoints, 'c') #Cyan青色
plt.show()
plt.plot(ypoints, 'm') #Magenta紫色
plt.show()
plt.plot(ypoints, 'y') #Yellow黃色
plt.show()
plt.plot(ypoints, 'k') #Black黑色
plt.show()
plt.plot(ypoints, 'w') #White白色
plt.show()

print("----------------------------------標記大小")
#Marker Size 標記大小
#You can use the keyword argument markersize or the shorter version, ms to set the size of the markers:
#您可以使用關鍵字參數標記或較短的版本 ms 來設定標記的大小：
#Set the size of the markers to 20:
#將標籤大小設定為 20：
import matplotlib.pyplot as plt
import numpy as np
ypoints = np.array([3, 8, 1, 10])
plt.plot(ypoints, 'o-.m', ms = 20)
plt.show()
#Format Strings fmt 格式字串 fmt
#"o(標記)--(線)r(顏色)"
#marker|line|color
#標記|線|顏色

print("----------------------------在標記的邊緣上色")
#Marker Color 標記顏色
#You can use the keyword argument markeredgecolor or the shorter mec to set the color of the edge of the markers:
#您可以使用關鍵字參數標記顏色或較短的 mec 來設定標記邊緣的顏色：
#Set the EDGE color to red:
#將 邊緣 顏色設定為紅色：
import matplotlib.pyplot as plt
import numpy as np
ypoints = np.array([3, 8, 1, 10])
plt.plot(ypoints, marker = 'o', ms = 20, mec = 'r')
plt.show()
#mec = 'r'標記的邊緣色
#ms = 20標記的大小
#You can use the keyword argument markerfacecolor or the shorter mfc to set the color inside the edge of the markers:
#您可以使用關鍵字參數標記面色或較短的 mfc 設定標記邊緣內的顏色：
#Set the FACE color to red:
print("-------------------------將面部顏色設定為紅色")
#將面部顏色設定為紅色：
import matplotlib.pyplot as plt
import numpy as np
ypoints = np.array([3, 8, 1, 10])
plt.plot(ypoints, marker = 'o', ms = 20, mfc = 'r')
plt.show()
plt.plot(ypoints, 'D:y', ms = 10, mec = 'm')
plt.show()
#mfc = marker face color標記面部顏色
#mec = marker edge color標記邊緣顏色
#Use both the mec and mfc arguments to color of the entire marker:
#使用 mec 和 mfc 參數來著色整個標記：
#Set the color of both the edge and the face to red:
print("--------------------將邊緣和面部的顏色設定為紅色")
#將邊緣和面部的顏色設定為紅色：
import matplotlib.pyplot as plt
import numpy as np
ypoints = np.array([3, 8, 1, 10])
plt.plot(ypoints, marker = 'o', ms = 10, mec = 'r', mfc = 'y')
plt.show()
#You can also use Hexadecimal color values:
#您也可以使用六價色值
#https://www.w3schools.com/colors/colors_hexadecimal.asp
#Mark each point with a beautiful green color:
print("-------------用六價色值--用美麗的綠色標記每個點")
#用美麗的綠色標記每個點：
plt.plot(ypoints, marker = 'o', ms = 20, mec = '#4CAF50', mfc = '#4CAF50')
plt.show()
#Or any of the 140 supported color names.
#或 140 個支援顏色名稱中的任何一個。
#https://www.w3schools.com/colors/colors_names.asp
plt.plot(ypoints, '^-.', ms = 10, mec = '#4CAF50',mfc = 'Navy')
plt.show()
#mec = '六價色值'或'名稱'
#mfc = '六價色值'或'名稱'
#Mark each point with the color named "hotpink":
print("-------------用色值名稱--用美麗的顏色標記每個點")
#用名為「粉紅」的顏色標記每個點：
plt.plot(ypoints, marker = 'o', ms = 20, mec = 'Navy', mfc = 'hotpink')
plt.show()
