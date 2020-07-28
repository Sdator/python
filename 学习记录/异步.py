

def test():
    print(11111)
    while True:
        a = yield 5
        print("a:", a, 22222222)


def main():
    a = test()
    print(type(a), a, 2222222)
    print(next(a), 33333333333)
    print("*"*20)
    print(next(a), 33333333333)

    print("*"*20)
    print(a.send(666), 33333333333)


if __name__ == "__main__":
    main()
