# "OOXXOXXOOO"와 같은 OX퀴즈의 결과가 있다. 
# O는 문제를 맞은 것이고, X는 문제를 틀린 것이다. 
# 문제를 맞은 경우 그 문제의 점수는 그 문제까지 연속된 O의 개수가 된다. 
# OX퀴즈의 결과가 주어졌을 때, 점수를 구하는 프로그램을 작성하시오.


a=int(input())

for i in range(a):
    b=input()
    st=list(b)
    sum=0
    c=1
    
    for sc in st:
       if sc=='O':
            sum+=c
            c+=1
       else:
            c=1
            
    print(sum)
