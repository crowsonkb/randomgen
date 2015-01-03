randomgen
=========

Generate random passwords.

```
usage: randomgen.py [-h] [-c COUNT] [-l LENGTH]
                    [-s {base10,base16,BASE16,base58,lower}] [--sep SEP]
                    [--group-size GROUP_SIZE]

optional arguments:
  -h, --help            show this help message and exit
  -c COUNT, --count COUNT
                        number of passwords generated
  -l LENGTH, --length LENGTH
                        length of passwords generated
  -s {base10,base16,BASE16,base58,lower}, --set {base10,base16,BASE16,base58,lower}
                        the set to choose elements from
  --sep SEP             the periodic separator string to use
  --group-size GROUP_SIZE
                        the number of elements in a group separated by the
                        periodic separator
```
