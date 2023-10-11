def max3(a, b, c):
    """a, b, c의 최댓값을 구하여 반환""" #주석넣는 방법 중 하나
    maximum = a
    if b>maximum: maximum = b
    if c>maximum: maximum = c
    return maximum

print(f'max3(3,2,1) = {max3(3,2,1)}')
print(f'max3(3,2,2) = {max3(3,2,2)}')
print(f'max3(3,1,2) = {max3(3,1,2)}')
print(f'max3(3,2,3) = {max3(3,2,3)}') 
# 좋은 알고리즘은 모든 경우에 일정한 값이 나오는 것.프린트로 모든 값을 넣어서 나오는지 확인
# 모든 자리에서 3이 최댓값으로 나오도록 max3 함수에 넣어서 결과를 봐야 함