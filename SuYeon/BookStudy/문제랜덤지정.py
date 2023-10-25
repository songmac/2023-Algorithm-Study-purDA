import random

def BookStudy(prob_num) :

  prob_extract = random.sample(range(1,prob_num),7) #문제 7개 랜덤 뽑기
  members = ['가희', '수연', '유미', '소희', '지우', '하영', '윤선']
  prob_mem_set = list(zip(prob_extract, members))

  for show in prob_mem_set :
    print(show)

  return show

prob_num= int(input('문제 수를 입력하세요: '))
result = BookStudy(prob_num)
print(result)





