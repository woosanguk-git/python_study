# zip() 는 2개 이상의 시퀀스를 인수로 취하여 짧은 길이의 시퀀스를 기준으로 각 항목이 순서대로 1:1 대응하는 새로운 튜플 시퀀스를 만든다.

if __name__ == "__main__":
    a = [1,2,3,4,5]
    b = ['a','b','c','d','e']

    print(list(zip(a,b)))