

# 나의 긴 코드

a,b=input().split()

a_list=list(a)
a_list.reverse()
A=int(''.join(a_list))

b_list=list(b)
b_list.reverse()
B=int(''.join(b_list))

if A>B:
    print(A)
else:
    print(B)
    
    
    
# 남의 짧은 코드

num1, num2 = input().split()
num1 = int(num1[::-1])  # [::-1] : 역순
num2 = int(num2[::-1])

if num1 > num2:
    print(num1)
else :
    print(num2)
