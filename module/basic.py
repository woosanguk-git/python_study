# 모듈은 def를 사용하여 정의한다.
# 모듈을 새ㅓㅇ할 떄 함수 또는 메서드에서 가변 객체를 기본값으로 사용하는 것은 좋지 않다.
# 좋은 예

def append(number, number_list = None):
    if number_list is None :
        number_list = []
    number_list.append(number)
    return number_list



# 패키지는 모듈과 __init__.py 파일이 있는 디렉터리다.
# 파이썬은 __init__.py 파일이 있는 디렉터리를 패키지로 취급.
# 디렉토리에 __init__파일 참고
