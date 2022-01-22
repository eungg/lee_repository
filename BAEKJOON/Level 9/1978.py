# 주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

a=int(input())

nums=map(int,input().split())
so=0
    
for n in nums:
    error=0
    if n>1:
        for i in range(2,n):
            if n%i==0:
                error+=1
        if error==0:
            so+=1

print(so)
