#!/usr/bin/env python3

"""Generate random passwords."""

import argparse
import math
import random
import sys

ALPHABET = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'

def bold(string):
    return '\x1b[1m' + string + '\x1b[0m'

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--count', help='number of passwords generated',
                        default=5, type=int)
    parser.add_argument('-l', '--length', help='length of passwords generated',
                        default=16, type=int)
    args = parser.parse_args()

    entropy = math.log(len(ALPHABET), 2) * args.length
    print(bold('entropy: {:.1f} bits'.format(entropy)), file=sys.stderr)

    rng = random.SystemRandom()
    for _ in range(args.count):
        chars = [rng.choice(ALPHABET) for _ in range(0, args.length)]
        print(''.join(chars))

if __name__ == '__main__':
    main()
