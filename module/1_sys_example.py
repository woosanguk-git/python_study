import sys

def main():
    for arg in sys.argv[1:]:
        print(arg)

def print_dir():
    # dir() 내장함수는 모듈이 정의하는 모든 유형의 이름(모듈, 변수, 함수) 을 찾는데 사용된다.
    # 이름 기준으로 정렬된 문자열 리스트 반환한다.
    return dir(sys)

if __name__ == "__main__":
    main()
    print(print_dir())