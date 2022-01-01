# 흔한 수학 문제 중 하나는 주어진 점이 어느 사분면에 속하는지 알아내는 것이다.

a=int(input())
b=int(input())

if a>0 and b>0:
    print("1")
elif a<0 and b>0:
    print("2")
elif a<0 and b<0:
    print("3")
else:
    print("4")
