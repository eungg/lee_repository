# N개의 숫자가 공백 없이 쓰여있다. 이 숫자를 모두 합해서 출력하는 프로그램을 작성하시오.

a=input()
b=input()

total=0
for i in b:
  total += int(i)
  
print(total)
