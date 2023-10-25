# 2-2 배열이란?
## 배열 원소의 최댓값 구하기
    1) a원소가 3개 일때
    maximum = a[0]
    if a[1] > maximum: maximum = a[1]
    if a[2] > maximum: maximum = a[2]

    2) a원소가 4개 일때
    maximum = a[0]
    if a[1] > maximum: maximum = a[1]
    if a[2] > maximum: maximum = a[2]
    if a[3] > maximum: maximum = a[3]

## 배열 a의 원소 중 최댓값을 구하는 max_of()함수를 정의하고, 최댓값을 구하는 과정
    def max_of(a):
    for i in range(!, len(a)):
    if a[i] > maximum:
    maximum = a[i]
![](2023-10-24-21-00-28.png)
