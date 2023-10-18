#최대값 구하는 함수
def max_of(a):
    max_int = a[0]
    for i in range(1, len(a)):
        if a[i] > max_int:
            max_int = a[i]
    return max_int


if __name__ == "__main__":
    print(max_of([100,22,44,66,0,88]))
