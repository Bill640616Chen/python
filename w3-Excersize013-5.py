#IndexError: list index out of range
#File "c:\Users\user\hello-world\w3-Excersize013-5.py", 
# line 12, in <module> n2=list(number[1])
dict1={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
dict2=dict(zip(dict1.values(),dict1.keys()))
appear=""
while True:
    number=input("").split(" ")
    if number == ["#"]:
        break
    n1=list(number[0])
    n2=list(number[1])
    add1=0
    add2=0
    for i in range (len(n1)-1):
        if dict1[n1[i]]<dict1[n1[i+1]]:
            add1-=dict1[n1[i]]
        else:
            add1+=dict1[n1[i]]
    add1+=dict1[n1[len(n1)-1]]
    for i in range (len(n2)-1):
        if dict1[n2[i]]<dict1[n2[i+1]]:
            add2-=dict1[n2[i]]
        else:
            add2+=dict1[n2[i]]
    add2+=dict1[n2[len(n2)-1]]
    if add1>=add2:
        add3=add1-add2
    else:
        add3=add2-add1
    if add3==0:
        print("ZERO")
    else:
        time=0
        while True:
            if add3>=1000:
                time=add3//1000
                add3=add3%1000
            else:
                break
        while True: 
            if time>0:
                time-=1
                appear+="M"
            else:
                break
        time=0
        while True:
            if add3>=100:
                time=add3//100
                add3=add3%100
            else:
                break
        while True:
            if time ==4:
                appear+="CD"
                time-=4
            if time == 9:
                appear+="CM"
                time-=9
            if time>=5:
                time-=5
                appear+="D"
            if time>0:
                time-=1
                appear+="C"
            else:
                break
        time=0
        while True:
            if add3>=10:
                time=add3//10
                add3=add3%10
            else:
                break
        while True:
            if time ==4:
                appear+="XL"
                time-=4
            if time == 9:
                appear+="XC"
                time-=9
            if time>=5:
                time-=5
                appear+="C"
            if time>0:
                time-=1
                appear+="X"
            else:
                break
        while True:
            if add3 ==4:
                appear+="IV"
                add3-=4
            if add3 == 9:
                appear+="IX"
                add3-=9
            if add3>=5:
                add3-=5
                appear+="V"
            if add3>0:
                add3-=1
                appear+="I"
            else:
                break
    print(appear)