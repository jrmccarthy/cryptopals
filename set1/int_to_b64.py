from __future__ import print_function, unicode_literals
import sys

# Our conversion "table" from integers to the proper b64 character
BASE64 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'

INPUT = 0x49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d

def int_to_base64(input, result=u''):
    """ Given an integer, turn it into a unicode string representing it in base 64 """
    # Grab the left-most digit
    this_digit = unicode(BASE64[input % 64])
    # If there's more digits, grab them recursively
    if input / 64 > 0:
        return int_to_base64((input / 64), this_digit) + result
    else:
        return result + this_digit

def main():
    if len(sys.argv) > 1 and sys.argv[1]:
        result = int_to_base64(sys.argv[1])
        print(result)
        return result
    result = int_to_base64(INPUT)
    print(result)
    return result
    

if __name__ == '__main__':
    main()