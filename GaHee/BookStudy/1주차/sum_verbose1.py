# 1-10
## a부터 b까지 정수의 합 구하기 1

print('a부터 b까지 정수의 합을 구합니다.')

a = int(input('정수 a를 입력하세요 : '))
b = int(input('정수 b를 입력하세요 : '))

if a > b:
    a, b = b, a

sum = 0
for i in range(a, b+1):
    if i < b:
        print(f'{i} + ', end = '')
    else:
        print(f'{i} = ', end = '')
    
    sum += i

print(sum)


"""
- 위 if문은 그다지 좋지 않은 방법 !
- 이유 : 예를 들어 a가 1이고 b가 10,000d일 때,
  i < b인 경우 명령어가 9,999번 실행되고,
  else일 때의 명령어가 1번 실행됨.
- 1번 실행을 위해 9,999번이 실행되는 셈이다.

=> 이럴 때는 for문 안의 if문을 제외해 별도로 두는 것이 좋다.
"""