# Copyright (c) 2016-2018 Hirochika Asai <asai@jar.jp>
# All rights reserved.
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--input-file', type=str, default="-")
parser.add_argument('--split-mode', type=int, default=2)



"""
Main routine
"""
def main():
    ## Parse the arguments
    args = parser.parse_args()
    ## Input file
    if args.input_file == "-":
        fp = sys.stdin
    else:
        try:
            fp = open(args.input_file, "r")
        except:
            print("Cannot open {}".format(args.input_file), file=sys.stderr)
    ## Split mode
    mode = args.split_mode

    for ln in fp:
        prefix = ln.strip()
        p = prefix.split("/")
        if mode == 2:
            r = split2(p[0], int(p[1]))
        elif mode == 4:
            r = split4(p[0], int(p[1]))
        else:
            r = [prefix]
        print(r)

    return None

"""
Integer to prefix string format
"""
def bit2prefix(bs, length, nr):
    c = bs | (nr << (32 - length))
    y = "{}.{}.{}.{}".format((c >> 24), (c >> 16) & 0xff, (c >> 8) & 0xff, c & 0xff)
    p = "{}/{}".format(y, length)
    return p

"""
Split prefix (mode=2)
"""
def split2(prefix, length):
    results = []
    a = prefix.split(".")
    b = (int(a[0]) << 24) | (int(a[1]) << 16) | (int(a[2]) << 8) | int(a[3])
    if length < 16 and length != 0:
        ## Split into 8
        for i in range(8):
            p = bit2prefix(b, length + 3, i)
            results.append(p)
    elif length < 20 and length != 0:
        ## Split into 4
        for i in range(4):
            p = bit2prefix(b, length + 2, i)
            results.append(p)
    elif length < 24 and length != 0:
        ## Split into 2
        for i in range(2):
            p = bit2prefix(b, length + 1, i)
            results.append(p)
    else:
        p = "{}/{}".format(prefix, length)
        results.append(p)
    return results

"""
Split prefix (mode=4)
"""
def split4(prefix, length):
    results = []
    a = prefix.split(".")
    b = (int(a[0]) << 24) | (int(a[1]) << 16) | (int(a[2]) << 8) | int(a[3])
    if length < 16 and length != 0:
        ## Split into 16
        for i in range(16):
            p = bit2prefix(b, length + 4, i)
            results.append(p)
    elif length < 20 and length != 0:
        ## Split into 8
        for i in range(8):
            p = bit2prefix(b, length + 3, i)
            results.append(p)
    elif length < 23 and length != 0:
        ## Split into 4
        for i in range(4):
            p = bit2prefix(b, length + 2, i)
            results.append(p)
    elif length < 24 and length != 0:
        ## Split into 2
        for i in range(2):
            p = bit2prefix(b, length + 1, i)
            results.append(p)
    else:
        p = "{}/{}".format(prefix, length)
        results.append(p)
    return results

"""
Call the main routine
"""
if __name__ == "__main__":
    main()

