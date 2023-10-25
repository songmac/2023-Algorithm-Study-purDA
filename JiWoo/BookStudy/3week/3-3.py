#선형검색 알고리즘 '보초법'

from typing import Any, Sequence
import copy

def seq_search(seq: Sequence, key: Any) -> int :
    """시퀀스 seq에서 key와 일치하는 원소를 선형 검색(보초법)"""
    a = copy.deepcopy(seq) # seq 복사
    a.append(key) # seq 복사한 a에 검색어 추가(추가는 항상 맨 마지막에)

    i = 0
    while True :
        if a[i] == key :
            break
        i += 1
    return -1 if i == len(seq) else i #인덱스 수랑 자료의 길이가 같으면 -1(검색X), 아니면 검색성공

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