# 1-12
## +와 -를 번갈아 출력하기 (1)

print('+와 -를 번갈아 출력합니다.')
n = int(input('몇 개를 출력할까요? : '))

for i in range(n):
    if i % 2:
        print('-', end='') # 홀수
    else:
        print('+', end='') # 짝수

print()

# 2가지 문제점 존재
# 1) for문을 반복할 때마다 if문 수행
# 2) 상황에 따라 유연한 수정이 어렵