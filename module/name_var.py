
# __name__ 변수에 대한 설명
# 파이썬은 모듈을 임포트할 때 마다 __name__ 이라는 변수를 만들고, 모듈 이름을 저장함.

text = "hello module"


def world():
    return "world"


if __name__ == "__main__":
    print(f"{__name__} 직접 실행됨.")
else:
    print(f"{__name__} 임포트 됨.")


# .py 를 직접 실행하면 파이썬은 __name__을 __main__으로 설정한다.