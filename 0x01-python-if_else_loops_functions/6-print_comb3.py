#!/usr/bin/python3
for a in range(0, 9):
    for b in range(a + 1, 10):
        if int(str(a) + str(b)) > 0 and int(str(a) + str(b)) < 89:
            print("{:02d}, ".format(int(str(a) + str(b))), end='')
            print("{:d}".format(89))
