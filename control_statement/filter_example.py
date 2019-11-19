# filter()는 시퀀스의 항목들 중 함수조건이 참인 항목만 추출해서 구성된 시퀀스를 반화한다.


def f(x):
    return x % 2 != 0 and x % 3 != 0

if __name__ == "__main__":
    print(f(17))
    print(f(33))
    l = list(filter(f, range(2,25)))
    print(l)
    