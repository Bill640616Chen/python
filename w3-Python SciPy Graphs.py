#https://www.w3schools.com/python/scipy/scipy_graphs.php
#SciPy Graphs SciPy圖表
#Working with Graphs 與圖形配合工作
#Graphs are an essential data structure.
#圖形是一種基本的數據結構。
#SciPy provides us with the module scipy.sparse.csgraph for working with such data structures.
#SciPy 為我們提供了用於處理此類數據結構的模組
# scipy.sparse.csgraph(壓縮稀疏圖,compress sparse graph)。
#Adjacency Matrix 相鄰矩陣
#Adjacency matrix is a nxn matrix where n is the number of elements in a graph.
#相鄰矩陣是 nxn 矩陣，其中 n 是圖表中的元素數。
#And the values represents the connection between the elements.
#值表示元素之間的連接。
#For a graph like this, with elements A, B and C, the connections are:
#對於這樣的圖形，與元素 A、B 和 C 的連接是：
#A & B are connected with weight 1.
#A & B 與重量 1 連接。
#A & C are connected with weight 2.
#A & C 與重量 2 連接。
#C & B is not connected.
#C & B 未連接。
#The Adjency Matrix would look like this:
#判斷矩陣看起來是這樣的：
'''
      A B C
   A:[0 1 2]  
   B:[1 0 0]
   C:[2 0 0]
'''
#A至A是0,A至B是1,A至C是2
#B至A是1,B至B是0,B至C是0
#C至A是2,C至B是0.C至C是0
#Below follows some of the most used methods for working with adjacency matrices.
#下面遵循一些最常用的方法與相鄰矩陣的工作。

print("---------------Connected Components 連接元件")
#Connected Components 連接元件
#Find all of the connected components with the connected_components() method.
#使用connected_components（）方法查找所有連接的元件。
import numpy as np
from scipy.sparse.csgraph import connected_components
from scipy.sparse import csr_matrix
arr = np.array([
  [0, 1, 2],
  [1, 0, 0],
  [2, 0, 0]
])
newarr = csr_matrix(arr)
print(connected_components(newarr))

print("---Dijkstra---指定一個點 (源點) 到其餘各個頂點的最短路徑")
#Dijkstra 演算法
#內容是指定一個點 (源點) 到其餘各個頂點的最短路徑，
# 也稱作「單源最短路徑」
#Use the dijkstra method to find the shortest path in a graph from one element to another.
#使用 dijkstra 方法在圖表中尋找從一個元素到另一個元素的最短路徑。
#It takes following arguments:
#需要以下參數：
#1.return_predecessors: boolean (True to return whole path of traversal otherwise False).
#return_predecessors： 布林 （真正的傳回整個路徑的穿越否則錯誤 ） 。
#2.indices: index of the element to return all paths from that element only.
#指數：僅返回該元素的所有路徑的元素指數。
#3.limit: max weight of path.
#限制：路徑的最大重量。
#Find the shortest path from element 1 to 2:
#尋找從元素 1 到 2 的最短路徑：
import numpy as np
from scipy.sparse.csgraph import dijkstra
from scipy.sparse import csr_matrix
arr = np.array([
  [0, 1, 2],
  [1, 0, 0],
  [2, 0, 0]
])
newarr = csr_matrix(arr)
print(dijkstra(newarr, return_predecessors=True, indices=0))
#return_predecessors：傳回前矩陣
# return the size (N, N) predecesor matrix

print("---Floyd Warshall---是解決任意兩點間的最短路徑的一種演算法")
#Floyd Warshall 演算法
#弗洛伊德演算法或佛洛依德演算法，是解決任意兩點間的最
# 短路徑的一種演算法，可以正確處理有向圖或負權（但不可
# 存在負權迴路）的最短路徑問題，同時也被用於計算有向圖
# 的遞移閉包
#Use the floyd_warshall() method to find shortest path between all pairs of elements.
#使用floyd_warshall（）方法在所有元素對之間找到最短的路徑。
#Find the shortest path between all pairs of elements:
#尋找所有對元素之間的最短路徑：
import numpy as np
from scipy.sparse.csgraph import floyd_warshall
from scipy.sparse import csr_matrix
arr = np.array([
  [0, 1, 2],
  [1, 0, 0],
  [2, 0, 0]
])
newarr = csr_matrix(arr)
print(floyd_warshall(newarr, return_predecessors=True))
#return_predecessors：傳回前矩陣
# return the size (N, N) predecesor matrix

print("---Bellman Ford---求解單源最短路徑問題的一種演算法,與Dijkstra類似")
#Bellman Ford 貝爾曼-福特演演算法
#求解單源最短路徑問題的一種演算法,與Dijkstra類似
#https://reurl.cc/82e0GR
#The bellman_ford() method can also find the 
# shortest path between all pairs of elements, 
# but this method can handle negative weights as well.
#bellman_ford（）方法也可以找到所有對元素之間的
# 最短路徑，但該方法也可以處理負權重。
#Find shortest path from element 1 to 2 with given graph with a negative weight:
#尋找從元素 1 到 2 的最短路徑，並使用負權重的給定圖形：
import numpy as np
from scipy.sparse.csgraph import bellman_ford
from scipy.sparse import csr_matrix
arr = np.array([
  [0, -1, 2],
  [1, 0, 0],
  [2, 0, 0]
])
newarr = csr_matrix(arr)
print(bellman_ford(newarr, return_predecessors=True, indices=0))

print("------------Depth First Order 深度優先搜尋法")
#Depth First Order 深度優先搜尋法
#DFS, Depth-first Search
#The depth_first_order() method returns a depth first traversal from a node.
#depth_first_order（）方法從節點返回深度第一次穿越。
#This function takes following arguments:
#此功能需要以下參數：
#the graph. 圖表。
#the starting element to traverse graph from.
#從圖形中穿越圖的起始元素。
#Traverse the graph depth first for given adjacency matrix:
#首先為給定的相鄰矩陣「遍歷」圖形深度：
#Traversal中文稱作「遍歷」
#圖的遍歷，也就是指通盤地讀取圖的資訊：決定好從
# 哪裡開始讀，依照什麼順序讀，要讀到哪裡為止。 
# 詳細地設計好流程，始能通盤地讀取圖的資訊；如果
# 設計得漂亮，在解決圖的問題時，還可以一邊讀取圖
# 的資訊，一邊順手解決問題呢！
import numpy as np
from scipy.sparse.csgraph import depth_first_order
from scipy.sparse import csr_matrix
arr = np.array([
  [0, 1, 0, 1],
  [1, 1, 1, 1],
  [2, 1, 1, 0],
  [0, 1, 0, 1]
])
newarr = csr_matrix(arr)
print(depth_first_order(newarr, 1))

print("----------Breadth First Order 廣度優先搜尋法")
#Breadth First Order 廣度優先搜尋法
#BFS, Breadth-first Search
#The breadth_first_order() method returns a breadth first traversal from a node.
#breadth_first_order（）方法從節點返回寬度第一次橫穿。
#This function takes following arguments:
#此功能需要以下參數：
#1.the graph. 圖表。
#2.the starting element to traverse graph from.
#從圖形中穿越圖的起始元素。
#Traverse the graph breadth first for given adjacency matrix:
#首先為給定的相鄰矩陣「遍歷」圖寬度：
import numpy as np
from scipy.sparse.csgraph import breadth_first_order
from scipy.sparse import csr_matrix
arr = np.array([
  [0, 1, 0, 1],
  [1, 1, 1, 1],
  [2, 1, 1, 0],
  [0, 1, 0, 1]
])
newarr = csr_matrix(arr)
print(breadth_first_order(newarr, 1))