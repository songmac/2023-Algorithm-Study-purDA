#선형 검색 for문 보초법 되는지 확인
from typing import Any, Sequence
import copy

def seq_search(seq: Sequence, key: Any) -> int:
    a = copy.deepcopy(seq) # seq 복사
    a.append(key) 

    i = 0
    for i in range(len(a)) :
        if a[i] == key :
            return -1 if i == len(seq) else i
        
if __name__ == '__main__' :
    num = int(input('원소 수를 입력하세요: '))
    x = [None]*num # 함수의 seq 값/원소 수 num인 배열 생성

    for i in range(num) :
        x[i] = int(input(f'x[{i}]: '))

    ky = int(input('검색할 값을 입력하세요: ')) # 검색할 키 입력

    idx = seq_search(x, ky) #배열 x에서 key값과 같은 원소 검색

    if idx == -1 :
        print('검색값을 갖는 원소가 존재하지 않습니다.')
    else :
        print(f'검색값은 x[{idx}]에 있습니다.')