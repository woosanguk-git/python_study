# python if 문은 다른 언어의 switch 와 case문을 대체 한다.

if x< 0 :
     x = 0
elif x == 0:
    print("x  = 0")
else : 
    print(" xx ")


# for 
# pyton for 문은 모든 시퀀스 항목을 순서대로 순회한다.
names = ["a", "b", "c"]

for name in names:
    print(name)



# True or False
# 파이썬에서 거짓은 사전 정의된 상수 False 또는 숫자0, 특수 객체 None, 빈 컬렉션 시퀀스("", [], (), {}) 해당된다.
# 여기에 속하지 않는 것은 모두 참(True) 이다.
users = []
foo = 0
i =10
if not users:
    print("user 가 없습니다.")
if foo ==0:
    print(" foo is zero")
if i%10 ==0:
    print("...")