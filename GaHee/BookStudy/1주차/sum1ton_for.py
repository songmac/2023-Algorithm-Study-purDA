# 1-8
## 1부터 n까지 정수의 합 구하기 2 (for문)

print('1부터 n까지 정수의 합을 구합니다.')

n = int(input('n값을 입력하세요 : '))

sum = 0
for i in range(1, n+1):
    sum += i
    
print(f'1부터 {n}까지 정수의 합은 {sum}입니다.')

# n = int(input('정수 n을 입력하세요.'))
# def sum(n):
#     result = (n * (n+1)) / 2
#     return result
# print(f'1부터 n까지의 합 : {sum(n)}')

