# 정수 N이 주어졌을 때, 소인수분해하는 프로그램을 작성하시오.

a=int(input())

i=2

while a!=1:
    if a%i == 0:
        a=a/i
        print(i)
    else:
        i+=1
