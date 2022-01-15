# 알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 
# 단, 대문자와 소문자를 구분하지 않는다.

words = input().upper()
set_words = list(set(words))

cnt_list = []

for x in set_words :
    cnt = words.count(x)
    cnt_list.append(cnt) 

if cnt_list.count(max(cnt_list)) > 1 : 
    print('?')
else :
    max_index = cnt_list.index(max(cnt_list)) 
    print(set_words[max_index])
