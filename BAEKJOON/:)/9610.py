'''
2차원 좌표 상의 여러 점의 좌표 (x,y)가 주어졌을 때, 각 사분면과 축에 점이 몇 개 있는지 구하는 프로그램을 작성하시오.

첫째 줄에 점의 개수 n (1 ≤ n ≤ 1000)이 주어진다. 
다음 n개 줄에는 점의 좌표 (xi, yi)가 주어진다. (-106 ≤ xi, yi ≤ 106)

각 사분면과 축에 점이 몇 개 있는지를 예제 출력과 같은 형식으로 출력한다.
'''

n=int(input())
q1=q2=q3=q4=axis=0
    
for i in range(n):
    a,b=map(int,input().split())

    if a==0 or b==0:
        axis+=1
    elif a>0 and b>0:
        q1+=1
    elif a<0 and b>0:
        q2+=1
    elif a<0 and b<0:
        q3+=1
    elif a>0 and b<0:
        q4+=1

print("Q1:",q1)
print("Q2:",q2)
print("Q3:",q3)
print("Q4:",q4)
print("AXIS:",axis)
