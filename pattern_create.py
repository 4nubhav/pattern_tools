import sys


def pattern_create(length,
                   set_a='ABCDEFGHIJKLMNOPQRSTUVWXYZ',
                   set_b='abcdefghijklmnopqrstuvwxyz',
                   set_c='0123456789'):
    string = ""
    a = b = c = 0

    while len(string) < length:
        if len(set_c) != 0:
            string += set_a[a] + set_b[b] + set_c[c]
            c += 1

            if c == len(set_c):
                c = 0
                b += 1

            if b == len(set_b):
                b = 0
                a += 1

            if a == len(set_a):
                a = 0
        else:
            string += set_a[a] + set_b[b]
            b += 1
            if b == len(set_b):
                b = 0
                a += 1
            if a == len(set_a):
                a = 0

    return string[:length]


def main():
    try:
        if len(sys.argv) == 2:
            print(pattern_create(int(sys.argv[1])))
        elif len(sys.argv) == 3:
            print("Error: At least two sets are required")
        elif len(sys.argv) == 4:
            print(pattern_create(int(sys.argv[1]), sys.argv[2], sys.argv[3], ""))
        elif len(sys.argv) == 5:
            print(pattern_create(int(sys.argv[1]), sys.argv[2], sys.argv[3], sys.argv[4]))
        else:
            raise ValueError
    except ValueError:
        print("Usage: python {} <length> [set a] [set b] [set c]".format(sys.argv[0]))
        print("Example: python {} 50 ABC def 123\n".format(sys.argv[0]))
        print("Ad1Ad2Ad3Ae1Ae2Ae3Af1Af2Af3Bd1Bd2Bd3Be1Be2Be3Bf1Bf")


if __name__ == "__main__":
    main()
