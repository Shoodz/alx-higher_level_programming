#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sum = 0
    for c in range(len(sys.argv) - 1):
    sum += int(sys.argv[c + 1])
    print(sum)
