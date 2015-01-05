randomgen
=========

Generate random passwords.

Usage
-----
```
usage: randomgen.py [-h] [-c COUNT] [-e {base10,base16,BASE16,base58,lower}]
                    [-g GROUP_SIZE] [-l LENGTH] [-s SEP]

optional arguments:
  -h, --help            show this help message and exit
  -c COUNT, --count COUNT
                        number of passwords generated
  -e {base10,base16,BASE16,base58,lower}, --elems {base10,base16,BASE16,base58,lower}
                        the set to choose elements from
  -g GROUP_SIZE, --group-size GROUP_SIZE
                        the number of elements in a group separated by the
                        periodic separator
  -l LENGTH, --length LENGTH
                        length of passwords generated
  -s SEP, --sep SEP     the periodic separator string to use
```
