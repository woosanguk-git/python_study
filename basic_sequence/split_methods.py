# A.splitlines()
#  => A 문자열에 대해 줄바꿈 문자를 기준으로 분리한 결과를 문자열 리스트로 반환
slayers = 'BOB\nEDDY'
print(slayers.splitlines())


# A.splint(t,n) 
# A 문자열에서 t를 기준으로 정수 n번 만큼 분리한 문자열 리스트 반환
# n 지정하지 않으면 대상 문자열을 t만큼 최대한 분리
# t도 지정하지 않으면 공백을 기준으로 최대한 분리

ex_string = "bye*hello-q*thankyou"
print(ex_string.split('*'))
