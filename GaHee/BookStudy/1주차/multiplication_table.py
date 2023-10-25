# 1-21
# 구구단 곱셈표 출력하기

print('--------------------------')
for i in range(1, 10):
    for j in range(1, 10):
        print(f'{i * j:3}', end='')
        # print(f'{i} * {j} = {i*j:3}')
    print()
print('--------------------------')