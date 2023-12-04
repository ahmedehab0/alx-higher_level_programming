#!/usr/bin/python3
def print_arg(argv):
    arguments_len = len(argv) - 1
    if arguments_len == 0:
        print("{:d} argument.".format(arguments_len))
        return
    else:
        if arguments_len == 1:
            print("{:d} argument:".format(arguments_len))
        else:
            print("{:d} arguments:".format(arguments_len))

        for i in range(1, arguments_len + 1):
            print("{:d}: {:s}".format(i, argv[i]))


if __name__ == "__main__":
    import sys
    print_arg(sys.argv)
