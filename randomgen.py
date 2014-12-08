#!/usr/bin/env python3

"""Generate random passwords."""

import argparse
import math
import random
import sys

ALPHABET = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'

def bold(s):
    return '\x1b[1m' + s + '\x1b[0m'

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--count', help='number of passwords generated',
                        default=5, type=int)
    parser.add_argument('-l', '--length', help='length of passwords generated',
                        default=16, type=int)

    args = parser.parse_args()
    rng = random.SystemRandom()

    print(bold('entropy: {:.1f} bits').format(
        math.log(len(ALPHABET), 2) * args.length), file=sys.stderr)

    for _ in range(args.count):
        s = ''
        for _ in range(args.length):
            s += rng.choice(ALPHABET)
        print(s)

if __name__ == "__main__":
    main()
