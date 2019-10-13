def declare_sequence():
    l = []
    print(type(l))
    s = ""
    print(type(s))

    t = ()
    print(type(t))

    ba = bytearray(b"")
    print(type(ba))

    b = bytes([])
    print(type(b))


if __name__ == "__main__":
    declare_sequence()