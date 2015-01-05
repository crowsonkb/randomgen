#!/usr/bin/env python3

"""Generate random passwords."""

import argparse
import collections
import math
import random
import sys

ELEMENT_SETS = collections.OrderedDict([
    ('base10', '0123456789'),
    ('base16', '0123456789abcdef'),
    ('BASE16', '0123456789ABCDEF'),
    ('base58', '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'),
    ('lower', 'abcdefghijklmnopqrstuvwxyz'),
])

def bold(string):
    return '\x1b[1m' + string + '\x1b[0m'

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--count', help='number of passwords generated',
                        default=5, type=int)
    parser.add_argument('-e', '--elems', help='the set to choose elements from',
                        default='lower', choices=ELEMENT_SETS.keys())
    parser.add_argument('-g', '--group-size', help='the number of elements in a'
                        ' group separated by the periodic separator',
                        default=0, type=int)
    parser.add_argument('-l', '--length', help='length of passwords generated',
                        default=16, type=int)
    parser.add_argument('-s', '--sep', help='the periodic separator string to use',
                        default=' ', type=str)
    args = parser.parse_args()

    element_set = ELEMENT_SETS[args.elems]
    entropy = math.log(len(element_set), 2) * args.length
    print(bold('entropy: {:.1f} bits'.format(entropy)), file=sys.stderr)

    rng = random.SystemRandom()
    for _ in range(args.count):
        elements = []
        for i in range(args.length):
            elements.append(rng.choice(element_set))
            if args.group_size != 0:
                if i != args.length - 1 and (i+1) % args.group_size == 0:
                    elements.append(args.sep)
        print(''.join(elements))

if __name__ == '__main__':
    main()
