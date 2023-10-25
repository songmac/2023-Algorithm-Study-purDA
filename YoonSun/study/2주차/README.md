# 2-1 자료구조와 배열
배열은 리스트와 튜플로 구현 가능
# 2-2 배열이란?
## 배열을 사용하는 기본 알고리즘
### 배열 원소의 최댓값 구하기
    1) a원소가 3개 일때
    maximum = a[0]
    if a[1] > maximum: maximum = a[1]
    if a[2] > maximum: maximum = a[2]

    2) a원소가 4개 일때
    maximum = a[0]
    if a[1] > maximum: maximum = a[1]
    if a[2] > maximum: maximum = a[2]
    if a[3] > maximum: maximum = a[3]

    1. 첫 번째 원소 a[0]의 값을 maximum에 대입
    2. if 문을 실행하는 과정에서 필요에 따라 maximum을 업데이트(원소 수가 n이 
       면 if 문은 n - 1번 실행)
    3. maximum과 비교하거 나 maximum에 대입하는 원소의 인덱스는 1, 2, 3으로
       1씩 증가

### 배열 a의 원소 중 최댓값을 구하는 max_of()함수를 정의하고, 최댓값을 구하는 과정

    def max_of(a):
    for i in range(!, len(a)):
    if a[i] > maximum:
    maximum = a[i]
1) a［0]에 주목하여 a［0]의 값을 maximum에 대입

<img width="245" alt="image" src="https://github.com/yoonandmoon/2023-Algorithm-Study-purDA/assets/99366732/90739ca8-9e50-470c-9f39-812620fa9f54">

2)  a［l］〜a［4］까지 차례대로 주목합니다. 
=> 스캔 : 배열원소를 하나씩 차례로 주목하여 살펴보는 방식
