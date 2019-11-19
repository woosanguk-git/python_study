# map(function, list) 는 시퀀스의 모든 항목에 함수를 적용한 결과 리스트를 반복하낟.

def cube(x):
    return x*x*x

if __name__ == "__main__":
    li = list(map(cube, range(1,11)))
    print(li)