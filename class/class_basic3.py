# 클래스의 합성 과 집합화:
# 한 클래스에서 다른 클래스의 인스턴스 변수를 포함하는 것을 말하며 클래스 간의 관계를 나타낸다.
# 파이썬의 모든 클래스는 상소글 사용한다.
# 대두분 클래스는 다양한 타입의 인스턴스 변수를 가지며 합성과 집합화를 사용한다.


# 합성은 클래스 A 와 B 가 강한 연관 관계를 맺으며 강한 생명주기를 ㅏㅈ느다.
# -> 의존성이 강하다는 뜻이다. (집 클래스에서 방 클래스를 갖는다.) 
# 집이 있으면 방이 있다.

# 집합화는 클래스 A ,B 가 연관 관계가 있지만, 생명주기가 약하며 독립적이다.
# 예를 들어 학생 클래스와 과목 클래스를 생각할 수 있다.
# 학생은 여러 과목을 수강할 수도 있고 안해도 된다.

import math


class Point(object):
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y 
        # data attribute

    def distance_from_origin(self):
        """ 원점으로부터의 거리 """
        return math.hypot(self.x, self.y)
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return "point ({0.x!r}, {0.y!r})".format(self)

    def __str__(self):
        return "({0.x!r}, {0.y!r})".format(self)

class Circle(Point):
    def __init__(self, radius, x=0, y=0):
        super().__init__(x,y)
        self.radius = radius
    
    def edge_distance_from_origin(self):
        return abs(self.distance_from_origin() - self.radius)
    

    def area(self):
        return math.pi*(self.radius**2)
    
    def circumference(self):
        """ 둘레 """
        return 2*math.pi*self.radius

    def __eq__(self, other):
        return self.radius == other.radius and super().__eq__(ohter)

    def __repr__(self):
        return "circle ({0.radius!r}, {0.x!r})".format(self)

    def __str__(self):
        return repr(self)


if __name__=="__main__":
    a = Point(4,5)
    print(a)
    print(a.__repr__())
    print(a.__str__())
    print(a.distance_from_origin())

    c = Circle(3,2,1)
    print(c)
    print(c.__repr__())
    print(c.__str__())
    print(c.circumference())
    print(c.edge_distance_from_origin())


    