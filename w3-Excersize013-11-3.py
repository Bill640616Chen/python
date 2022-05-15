score=[[[[[[1]*2]*2]*2]*2]*2]*2
for a in range(2): 
    for b in range(2):
        score[a][b]=2 
        print('')
        print(score)
print('----------------------------------')
score=[[[[[[1]*2]*2]*2]*2]*2]*2
print(score)
print('----------------------------------')
score[0][0]=2
print(score)
print('----------------------------------')
score[0][1]=2
print(score)
print('----------------------------------')
score[1][0]=2
print(score)
print('----------------------------------')
score[1][1]=2
print(score)
print('----------------------------------')
def x(y):
    for a in range(2): 
        for b in range(2):
            score[a][b]=2 
            print('')
            print(y)
x(score)            
'''
        for c in range(2):
            for d in range(2):
                score[c][d]=3
                for e in range(2):
                    for f in range(2):
                        score[e][f]=4
                        for g in range(2):
                            for h in range(2):
                                score[g][h]=5
                                for i in range(2):
                                    for j in range(2):
                                        score[g][h]=6
'''
