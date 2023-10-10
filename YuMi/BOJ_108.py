# n이 1,2,3이 아니면 아무것도 출력을 하지 않습니다.
input_str = input("정수를 입력하세요 : ")

# any함수를 이용하면 리스트로 주어지는 키워드 중 하나 이상이 특정 문자열에 포함되는 경우 
# true false로 반환
# 조건식이 여러개 이므로 문자열을 리스트로 만드는 코드 추가 하여 사용
if any(x in input_str for x in ["1", "2", "3"]) :
    print("1,2,3번 중 하나의 문자열입니다") #1,2,3이 포함된 경우 Nothing 출력
else : 
    pass # 그외 숫자는 패스1


#실습 코드 
#if n ==1 :
#   print("A")
#elif n == 2 : 
# print("B")...

