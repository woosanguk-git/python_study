def slicing_sequence():
    # seq[시작]
    # seq[시작 : 끝]
    # seq[시작:끝:스텝]
    word = "Watch the stairs!"
    print(word[-1])
    print(word[-2])
    print(word[-2:])
    print(word[:-2])
    print(word[-0])
    print(word[0:5])
    print(word[:10:2])
    


if __name__ == "__main__":
    slicing_sequence()