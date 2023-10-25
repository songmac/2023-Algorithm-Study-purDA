#10진수 정숫값 입력 받아 2~36 진수로 변환 후 출력

def card_conv(x: int, r:int) -> str : # x,r 인수형 넣은 함수 스트링으로 반환
    """정숫값 x를 r진수로 변환한 뒤 그 수를 나타내는 문자열을 반환"""

    d = '' #변환 후 배열 넣을 문자열 자료
    dchar = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ' #0-9A-Z

    while x > 0 :
        d += dchar[x % r] #반환 할 문자열 d에 해당 문자 꺼내서 결합. 
        x //= r
        # x를 r로 계속 나눈 나머지를 x에 대입하다 x가 0이하 될 때 끝!
    return d[::-1] #역순으로 반환

# print(card_conv(283709153,31)) #함수 실행되는지 결과 확인.

#값 입력받고 실행
if __name__ == '__main__' : #임포트하지 않고 정의한 함수 실행
    print('10진수를 n진수로 변환합니다.')

    while True :
        while True : # 함수 실행 전 값들 입력. x, r = no, cd
            no = int(input('변환할 값으로 음이 아닌 정수를 입력하세요: '))
            if no > 0 :
                break
        while True :
            cd =  int(input('어떤 진수로 변환할까요?: '))
            if 2 <= cd <= 36 :
                break
        
        print(f'{cd}진수로는 {card_conv(no, cd)}입니다.')

        retry = input("한 번 더 변환할까요?(Y ... 예 / N ... 아니요): ")
        if retry in {'N', 'n'}: #집합 함수
            break
