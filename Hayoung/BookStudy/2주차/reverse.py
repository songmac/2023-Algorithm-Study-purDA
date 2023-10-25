# 뮤터블 시퀀스 원소를 역순으로 정렬
from typing import Any, MutableSequence

def reverse_array(a: MutableSequence) -> None:
    n = len(a)
    for i in range(n // 2): 
        # 역순으로 바꿀 때는 배열 갯수의 반 번만 실행 하면 되므로 n//2
        a[i], a[n-i-1] = a[n-i-1], a[i] # n이 배열의 마지막 원소이고 n - i 실행 될 때마다 뒤에서 i번 옮겨가면서 순회
        
if __name__ == '__main__':
    print('배열 원소를 역순으로 정렬합니다.')
    nx = int(input('원소 수를 입력하세요.: '))
    x = [None] * nx # 원소 수가 nx인 리스트를 생성
    
    for i in range(nx):
        x[i] = int(input(f'x[{i}]값을 입력하세요.: '))
        
    reverse_array(x) # x를 역순으로 정렬
    
    print('배열 원소를 역순으로 정렬했습니다.')
    for i in range(nx):
        print(f'x[{i}] = {x[i]}')