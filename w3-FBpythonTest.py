#FBpython Taiwan網友提問的答案
score = [0,85,35,65,27,68,94,20,100,58,78]
p = int(input('輸入學號: '))
if 1<=p<=10:
    result = lambda x: score[p]
    print(result(p))
else:
    print('輸入錯誤')
#試作
dict = {'1':0,'2':85,'3':35,'4':65,'5':27,'6':68,'7':94,'8':20,'9':100,'10':58,'11':78}
for k,v in dict.items():
    print(k,v)
