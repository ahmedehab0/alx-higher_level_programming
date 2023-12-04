#!/usr/bin/python3
def infinite_add(argv):
    arguments_len = len(argv) - 1
    if arguments_len == 0:
        print("{:d}".format(arguments_len))
        return
    total = 0
    for i in range(1, arguments_len + 1):
        total += int(argv[i])
    print("{:d}".format(total))


if __name__ == "__main__":
    import sys
    infinite_add(sys.argv)
