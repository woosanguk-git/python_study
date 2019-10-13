# class 기본적인 선언방법
# 구글 파이썬 스타일 가이드에선 한 클래스가 다른 클래스를 상속받지 않으면
# 최상위 클래스인 Object를 명시적으로 표기하는것을 권장


class SampleClass(object):
    pass


class OuterClass(object):
    class InnerClass(object):
        pass


class ParentClass(object):
    pass


class ChildClass(ParentClass):
    """부모 클래스 상속"""
    pass

# 다형성
# 서브 클래스 객체에서 슈퍼 클래스와 동명의 메서드를 호출하면
# 파이썬은 서브 클래스에 정의된 메서드를 사용한다는 뜻이다.
# 슈퍼클래스의 메서드를 호출해야 한다면 super() 메서드를 사용하여 호출할 수 있다.

# 파이썬에서 사용자 정의 클래스의 모든 객체는 기본적으로 해쉬 가능하다.
# 이 뜻은 hash() 속성을 호출할 수 있다는 뜻이며 불변 객체임을 의미한다.
# ▼ 예제


class Symbol(object):
    def __init__(self, value):
        self.value = value


if __name__ == "__main__":
    x = Symbol("Py")
    y = Symbol("Py")
    symbols = set()

    symbols.add(x)
    symbols.add(y)

    print(x is y)
    print( x == y) 
    print(len(symbols))
    
