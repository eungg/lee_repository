"""
문자열 S를 입력받은 후에, 각 문자를 R번 반복해 새 문자열 P를 만든 후 출력하는 프로그램을 작성하시오. 
즉, 첫 번째 문자를 R번 반복하고, 두 번째 문자를 R번 반복하는 식으로 P를 만들면 된다.
"""

a=int(input())

for i in range(a):
    r,s=input().split()
    for k in s:
        print(k*int(r),end='')
    print()
