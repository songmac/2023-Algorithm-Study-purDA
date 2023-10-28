# [Do it! 실습 2-3] 배열 원소의 최댓값을 구해서 출력하기(원솟값을 입력받음)

from max import max_of # max.py을 실행하려는 스크립트 파일과 같은 경로에 저장해야 함

print('배열의 최댓값을 구합니다.')
print('주의: "End"를 입력하면 종료합니다.')

number = 0
x = []                  # 빈 리스트

while True:
    s = input(f'x[{number}]를 입력하세요.: ')
    if s == 'End':
        break
    x.append(int(s))    # 배열의 끝에 추가
    number += 1

print(f'{number}개를 입력했습니다.')
print(f'최댓값은 {max_of(x)}입니다.')