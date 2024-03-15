#체인법으로 해시 함수 구현하기
from __future__ import annotations
from typing import Any, Type
import hashlib

#node 클래스는 개별 버킷을 나타냄
#키와 값이 짝을 이루는 구조 
#키에 해시 함수를 적용하여 해시값을 구함

class Node: 
        
    #초기화 : 빈 해시 테이블 생성 
    def __init__(self, key : Any, value : Any, next: Node) -> None:
        self.key = key # 키(임의의 자료형)
        self.value = value #값 (임의의 자료형)
        self.next = next #뒤쪽 노드를 참조 (node형)
    

class ChainedHash:

    def __init__(self, capacity: int) -> None:
        self.capacity = capacity             # 해시 테이블의 크기를 지정
        self.table = [None] * self.capacity  # 해시 테이블(리스트)을 선언
    
    def hash_value(self, key:Any) -> int:
        #키에 해당하는 해시값을 구함
        if isinstance(key, int):
            return key % self.capacity #capacity:해시 테이블의 크기
        #sha256알고리즘: hashlib 모듈에서 제공하는 해시 알고리즘
        #encode : sha256알고리즘에는 바이트 문자열의 인수를 전달 key - str로 변환 뒤 바이트 문자열 생성
        #hexdigest : 해시값 16진수 문자열로
        #16진수 문자열을 다시 int로 변환
        return(int(hashlib.sha256(str(key).encode()).hexdigest, 16) % self.capacity)
    
    def search(self, key:Any) -> Any:
        #key인 원소를 검색하여 값을 반환
        hash = self.hash_value(key) # 검색하는 키의 해시값
        p = self.table[hash] #노드를 주목
        
        while p is not None:
            if p.key == key: 
                return p.value #검색 성공
            p = p.next # 뒤쪽 노드 주목
        return None # 검색실패
    
    def add(self, key:Any, value :Any) -> bool:
        hash = self.hash_value(key) #추가하는 키의 해시값
        p = self.table[hash]
        
        while p is not None:
            if p.key == key:
                return False #추가 실패
            p = p.next #뒤쪽 노드 주목
        
        temp = Node(key, value, self.table[hash])
        self.table[hash] = temp
        return True #노드 추가 성공
    
    def remove(self, key:Any) -> bool:
        hash = self.hash_value(key)
        p = self.table[hash]
        pp = None
        
        while p is not None:
            if p.key == key:
                if pp is None:
                    self.table[hash] = p.next
                else : 
                    pp.next = p.next
                return True
            pp = p
            p = p.next
        return False
    
    def dump(self) -> None:
        for i in range(self.capacity):
            p = self.table[i]
            print(i, end=" ")
            while p is not None:
                print(f' -> {p.key}({p.value})', end='')
                p = p.next
            print()

                    