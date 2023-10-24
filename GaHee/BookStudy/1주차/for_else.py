# 1-18
# else 문이 뒤따르는 for문 !
## 10-99 사이의 난수 n개 생성하기 (13이 나오면 중단)

import random

n = int(input('난수의 개수를 입력하세요. : '))

for _ in range(n):
    r = random.randint(10, 99)
    print(r, end=' ')
    if r == 13:
        print('')
        print('프로그램을 중단합니다.')
        break
else:
    print('난수 생성을 종료합니다.')
    

'''
- 13 이후 난수는 출력되지 않고, else문도 실행되지 않는다.
- 13이 나오지 않으면 반복이 끝난 다음 else문이 실행됨.
- 개선할 점
  : 건너뛰는 판단을 하려면 비용이 많이 든다.
  : 건너뛰어야 하는 값을 모르거나, 건너뛰어야 하는 값이 변화하면 매번 if, continue문을 사용해야 함.

'''