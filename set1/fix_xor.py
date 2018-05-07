from __future__ import print_function, unicode_literals
import sys

INPUT = 0x1c0111001f010100061a024b53535009181c

SECOND = 0x686974207468652062756c6c277320657965

def fixed_xor(first, second):
    """ 
    XOR two values and return the result, hex-encoded.

    Expects both inputs to be python INTs 
    """
    return hex(first ^ second)

def main():
    if len(sys.argv) > 2:
        result = fixed_xor(sys.argv[1], sys.argv[2])
        print(result)
        return result
    result = fixed_xor(INPUT, SECOND)
    print(result)
    return result
    

if __name__ == '__main__':
    main()