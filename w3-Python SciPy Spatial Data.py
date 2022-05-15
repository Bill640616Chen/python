#https://www.w3schools.com/python/scipy/scipy_spatial_data.php
#SciPy Spatial Data 空間數據
#Working with Spatial Data 處理空間數據
#Spatial data refers to data that is represented in a geometric space.
#空間數據是指在幾何空間中表示的數據。
#E.g. points on a coordinate system.
#例如，座標系統上的點。
#We deal with spatial data problems on many tasks.
#我們處理許多任務的空間數據問題。
#E.g. finding if a point is inside a boundary or not.
#例如，查找某個點是否在邊界內。
#SciPy provides us with the module scipy.spatial, which has functions for working with spatial data.
#SciPy 為我們提供了用於處理空間數據的模組 scipy.spatial。
#Triangulation 三角測量
#A Triangulation of a polygon is to divide the polygon into multiple triangles with which we can compute an area of the polygon.
#多邊形的三角測量是將多邊形分成多個三角形，我們可以用這些三角形計算多邊形的區域。
#A Triangulation with points means creating surface composed triangles in which all of the given points are on at least one vertex of any triangle in the surface.
#帶點的三角測量意味著創建表面組成的三角形，其中所有給定點至少位於表面任何三角形的一個頂點上。
#One method to generate these triangulations through points is the Delaunay() Triangulation.
print("-------通過點生成這些三角測量的一種方法是Delaunay()三角測量")
#通過點生成這些三角測量的一種方法是Delaunay()三角測量。
#Create a triangulation from following points:
#從以下點建立三角測量：
import numpy as np
from scipy.spatial import Delaunay
import matplotlib.pyplot as plt
points = np.array([
  [2, 4],
  [3, 4],
  [3, 0],
  [2, 2],
  [4, 1]
])
simplices = Delaunay(points).simplices
plt.triplot(points[:, 0], points[:, 1], simplices)
plt.scatter(points[:, 0], points[:, 1], color='r')
plt.legend() #顯示標籤
plt.show()
#[2, 4],[X軸,Y軸]
#Note: The simplices property creates a generalization of the triangle notation.
#注：簡單屬性創建三角形符號的概括。

print("----覆蓋所有給定點----使用ConvexHull()方法創建凸殼")
#Convex Hull 凸包算法
#A convex hull is the smallest polygon that covers all of the given points.
#凸殼是最小的多邊形，覆蓋所有給定點。
#Use the ConvexHull() method to create a Convex Hull.
#使用ConvexHull()方法創建凸殼。
#Create a convex hull for following points:
#創建凸殼以用於以下點：
import numpy as np
from scipy.spatial import ConvexHull
import matplotlib.pyplot as plt
points = np.array([
  [2, 4],
  [3, 4],
  [3, 0],
  [2, 2],
  [4, 1],
  [1, 2],
  [5, 0],
  [3, 1],
  [1, 2],
  [0, 2]
])
hull = ConvexHull(points)
hull_points = hull.simplices
plt.scatter(points[:,0], points[:,1])
for simplex in hull_points:
  plt.plot(points[simplex,0], points[simplex,1], 'k-')
plt.show()

print("-------------------KDTrees 線段樹算法")
#KDTrees 線段樹算法
#KDTrees are a datastructure optimized for nearest neighbor queries.
#KDTrees 是一種數據結構，針對最近的鄰居查詢進行了優化。
#E.g. in a set of points using KDTrees we can efficiently ask which points are nearest to a certain given point.
#例如，在使用 KDTrees 的一組點中，我們可以有效地詢問哪些點最接近某個給定點。
#The KDTree() method returns a KDTree object.
#KDTree（）方法返回 KD 樹物件。
#The query() method returns the distance to the nearest neighbor and the location of the neighbors.
#query()方法將距離返回到最近的鄰居和鄰居的位置。
#Find the nearest neighbor to point (1,1):
#查找最近的鄰居點 （1，1）：
from scipy.spatial import KDTree
points = [(1, -1), (2, 3), (-2, 3), (2, -3)]
kdtree = KDTree(points)
res = kdtree.query((1, 1))
print(res)

print("-------------------KDTrees 線段樹算法")
#Distance Matrix 距離矩陣
#There are many Distance Metrics used to find various types of distances between two points in data science, Euclidean distsance, cosine distsance etc.
#在數據科學中，有許多距離指標用於查找兩個點之間的不同類型的距離，即歐幾里德分差、共生差異等。
#The distance between two vectors may not only be the length of straight line between them, it can also be the angle between them from origin, or number of unit steps required etc.
#兩個向量之間的距離可能不僅是它們之間的直線長度，也可以是它們之間的角度從起源，或單位步驟的數量等。
#Many of the Machine Learning algorithm's performance depends greatly on distance metrices. E.g. "K Nearest Neighbors", or "K Means" etc.
#機器學習演算法的許多性能在很大程度上取決於距離指標。例如，"K 最近的鄰居"或"K 意味著"等。
#Let us look at some of the Distance Metrices:
#讓我們看看一些距離指標：
#Euclidean Distance 歐幾里德距離 (輾轉相除法)
#Find the euclidean distance between given points.
#找出兩點之間的歐幾里德距離
from scipy.spatial.distance import euclidean
p1 = (1, 0)
p2 = (10, 2)
res = euclidean(p1, p2)
print(res)

print("-----------------Cityblock Distance")
#Cityblock Distance (Manhattan Distance)
#城市街區距離（曼哈頓距離）
#Is the distance computed using 4 degrees of movement.
#是使用 4 度運動計算距離。
#E.g. we can only move: up, down, right, or left, not diagonally.
#例如，我們只能移動：向上、向下、向右或向左移動，而不是對角線移動。
#Find the cityblock distance between given points:
#尋找給定點之間的城市塊距離：
from scipy.spatial.distance import cityblock
p1 = (1, 0)
p2 = (10, 2)
res = cityblock(p1, p2)
print(res)

print("-----------------Cosine Distance")
#Cosine Distance 餘弦距離
#Is the value of cosine angle between the two points A and B.
#是A點和B兩點之間的cosine角度值。
#Find the cosine distsance between given points:
#查找給定點之間的cosine差異：
from scipy.spatial.distance import cosine
p1 = (1, 0)
p2 = (10, 2)
res = cosine(p1, p2)
print(res)

print("-----------------Hamming Distance")
#Hamming Distance 漢明距離(位運算)
#Is the proportion of bits where two bits are difference.
#是兩個位不同位的比例。
#It's a way to measure distance for binary sequences.
#這是測量二進位序列距離的一種方式。
#Find the hamming distance between given points:
#查找給定點之間的漢明距離：
from scipy.spatial.distance import hamming
p1 = (True, False, True)
p2 = (False, True, True)
res = hamming(p1, p2)
print(res)