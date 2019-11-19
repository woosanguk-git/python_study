# generator 를 설명하기 위해 피보나치 수열을 예로 듬.


def fib_generator():
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a + b


if __name__ == "__main__":
    fib = fib_generator()
    print(next(fib))
    print(next(fib))
    print(next(fib))
    print(next(fib))
    print(next(fib))
    print(next(fib))
    print(next(fib))
    print(next(fib))
