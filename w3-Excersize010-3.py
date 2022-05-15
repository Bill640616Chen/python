while True:
    try:
        n = int(input()) #輸入被分解數字
        t = 0 #檢驗值
        k = 2 #最小質數、最小除數
        while n >= k:
            power = 0 #次方數，記得放在迴圈內(歸零次方數) 
        while n % k == 0: #檢驗是否整除，若整除=>執行以下程式碼；若不整除=>除數加一，加到除式整除為止
            n /= k
            power += 1 #意思：每除一次除數，次方數就加一
            if power > 1 and t == 0: #先將有次方的除數印出來
                print(f'{str(k)}^{str(power)}', end = '')
                t += 1 #檢驗值的功用：避免再次進入此判斷式
            elif power == 1 and t == 0: #若被除數只被整除一次＝次方數等於1，直接印出該除數
                print(str(k),end = '')
                t += 1 #檢驗值的功用：避免再次進入此判斷式
            elif power > 1: #處理第二個power大於1的質因數
                print(f' * {str(k)}^{str(power)}', end = '')
            elif power == 1: #處理第二個第二個power等於1的質因數
                print(f' * {str(k)}', end = '')
            else:
                k += 1 #都沒有滿足條件：除數加一繼續除到滿足上述其中條件4
    except:
        break
#毫無作用,只能輸入數字,無法做之後的計算,可能是縮排問題