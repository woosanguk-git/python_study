# join 은 문자혈을 합쳐준다.
#  + 보다 단어가 많을 때 효율적이다.

def using_join():
    words = ["커피", "는", "라떼로"]
    sentence = "".join(words)
    print(sentence)


if __name__ == "__main__":
    using_join()