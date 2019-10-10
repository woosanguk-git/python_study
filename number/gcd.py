def finding_gcd(num1, num2):
    while(num2 != 0):
        print(num1, num2)
        result = num2
        num1, num2 = num2,  num1 % num2
        # num2 가 0이 되면 종료.
    return result

if __name__=="__main__":
    print(finding_gcd(60,48))
    