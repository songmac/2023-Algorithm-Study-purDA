[BOOK-1- 12]
# 반복 과정에서 조건 판단하기
# 특정 문자를 줄바꿈없이 연속으로 출력하는 프로그램

print('+와-를 번갈아 출력합니다.')
n = int(input('몇개를 출력할까요?: '))

for i in range(n):
    if i%2:
        print('-',end='')
    else:
        print('+',end='')

print()
