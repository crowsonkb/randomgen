#!/usr/bin/env python3

import argparse
import math
import random

alphabet = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'

parser = argparse.ArgumentParser()
parser.add_argument('-c', '--count', help='number of passwords generated',
    default=5, type=int)
parser.add_argument('-l', '--length', help='length of passwords generated',
    default=16, type=int)

args = parser.parse_args()
rng = random.SystemRandom()

print('\x1b[1mentropy: {:.1f} bits\x1b[0m'.format(
	math.log(len(alphabet), 2) * args.length))
for i in range(args.count):
    s = ''
    for j in range(args.length):
        s += rng.choice(alphabet)
    print(s)
