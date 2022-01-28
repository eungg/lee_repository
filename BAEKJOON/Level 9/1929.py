'''
M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.

첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다. (1 ≤ M ≤ N ≤ 1,000,000) M이상 N이하의 소수가 하나 이상 있는 입력만 주어진다.

한 줄에 하나씩, 증가하는 순서대로 소수를 출력한다
'''


#정답
def SOSU(num):
    if num == 1:
        return False
    else:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True
 
 
M, N = map(int, input().split())
 
for i in range(M, N + 1):
    if SOSU(i):
        print(i)
        
        
# 시간이 많이 걸리는 내 풀이 - (1 ≤ M ≤ N ≤ 1,000,000) 수의 범위가 커서 2부터 하나씩 나눠보기엔 너무 오래걸림
a,b = map(int,input().split())
sosu=[]

for num in range(a,b+1):
    error=0
    if num>1:
        for k in range(2,num):
            if num%k==0:
                error += 1
        if error==0:
            sosu.append(num)
            
for i in sosu:
    print(i)
