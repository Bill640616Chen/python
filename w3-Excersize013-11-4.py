
score=[[[0]*3]*3 for i in range(3) for j in range(1)]
print(score)
for a in range(3): 
    for b in range(1):
        for c in range(1):
            score[a][b][c]=2

        #索引[0][0]把[0,0]陣列取代為2
#        for d in range(3):
#            for e in range(3):
#                score[d][e][a]=3
            print('') #把每次遍歷分別輸出
            print(score)
#會從最內圈開始,有多的空間賦值,才能繼續給外圈的賦值
a =[[[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0]]]
a[0][1][0]=5
print(a)