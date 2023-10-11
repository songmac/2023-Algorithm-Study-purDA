#a, b, c의 최댓값을 구하여 반환
def max3(a, b, c):
    maximum = a #단순한 대입문
    if b>maximum: maximum = b # 04~05행 if문으로 복합문. if와 콜론(:)사이에 있는 것은 조건식.
    if c>maximum: maximum = c # 조건식으로 평가한 결과에 따라 프로그램 실행 흐름이 변경되는 구조를 선택구조라 함
    return maximum # 
print(f'max3(3,2,1) = {max3(3,2,1)}')
print(f'max3(3,2,2) = {max3(3,2,2)}')
print(f'max3(3,1,2) = {max3(3,1,2)}')
print(f'max3(3,2,3) = {max3(3,2,3)}') 

# 좋은 알고리즘은 모든 경우에 일정한 값이 나오는 것.프린트로 모든 값을 넣어서 나오는지 확인
# 모든 자리에서 3이 최댓값으로 나오도록 max3 함수에 넣어서 결과를 봐야 함