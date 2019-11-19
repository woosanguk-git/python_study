# break는 반복문 바로 빠져나가고
# continue는 반복문의 다음 단계로 전환한다.

for i in range(10):
    if i == 4:
        break
    print(i)
else:
    print("for end")

# 반복문에 else를 쓸 수 있는데 
# 반복문에서 리스트의 항목을 모두 순회했거나 while 문에서 조건이 false가 되었을 떄 실행된다. 
# 단, break 로 종료되었을때는 실행되지 않는다.

for i in range(10):
    if i == 4:
        continue
    print(i)
else:
    print("for end")

    