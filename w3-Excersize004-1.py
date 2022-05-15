
try:
    while True:
        y=int(input())
        if y%4==0 and y%100!=0 :
            print('閏年')
        else :
            print('平年') 
            break
    raise Exception('EOF')
except Exception as e:
     print(e)

