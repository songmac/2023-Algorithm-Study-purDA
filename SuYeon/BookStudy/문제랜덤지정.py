import random

def BookStudy(num) :
  if num > 0 :
    prob = random.sample(range(1,num),7) #문제 7개 랜덤 뽑기
    mem = ['가희', '수연', '유미', '소희', '지우', '하영', '윤선']
    prob_mem_set = list(zip(prob, mem))

    for result in prob_mem_set :
      print(result)
      
    return result

  else :
    return print("문제 수를 잘못 입력하였습니다.")



chap= int(input('단원: '))
num= int(input('문제 수를 입력하세요: '))
result = BookStudy(num)



