#!/usr/bin/env python
"""
Kenzie Assignment: String2
"""
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Instructions:
# Complete each of these string exercises in the same way as the
# previous String1 excercises.

# D. verbing
# Given a string, if its length is at least 3,
# add 'ing' to its end.
# Unless it already ends in 'ing', in which case
# add 'ly' instead.
# If the string length is less than 3, leave it unchanged.
# Return the resulting string.


def verbing(s):
    length = len(s)

    if length > 2:
        if s[-3:] == 'ing':
            s += 'ly'
        else:
            s += 'ing'

    return s


# E. not_bad
# Given a string, find the first appearance of the
# substring 'not' and 'bad'. If the 'bad' follows
# the 'not', replace the whole 'not'...'bad' substring
# with 'good'.
# Return the resulting string.
# So 'This dinner is not that bad!' yields:
# This dinner is good!
def not_bad(s):
    isNotBad = s.find('not')
    isBad = s.find('bad')

    if isBad > isNotBad:
        s = s.replace(s[isNotBad:(isBad+3)], 'good')

    return s


# F. front_back
# Consider dividing a string into two halves.
# If the length is even, the front and back halves are the same length.
# If the length is odd, we'll say that the extra char goes in the front half.
# e.g. 'abcde', the front half is 'abc', the back half 'de'.
# Given 2 strings, a and b, return a string of the form
#  aFront + b-front + a-back + b-back
# def front_back(a, b):
#     frontHalf = len(a)
#     backHalf = len(b)

#     if frontHalf % 2 == 0:
#         firstIndex = frontHalf // 2
#     else:
#         firstIndex = (frontHalf // 2) + 1

#     if backHalf % 2 == 0:
#         backIndex = backHalf // 2
#     else:
#         backIndex = (backHalf // 2) + 1

#     aFront = a[0:firstIndex]
#     a-back = a[firstIndex:]

#     b-front = b[0:backIndex]
#     b-back = b[backIndex:]

#     return a-front
#  + b-front + a-back + b-back

def front_back(a, b):
    lengthOfA = len(a)
    lengthOfB = len(b)

    if lengthOfA % 2 == 0:
        indexA = lengthOfA // 2
    else:
        indexA = (lengthOfA // 2) + 1

    if lengthOfB % 2 == 0:
        indexB = lengthOfB // 2
    else:
        indexB = (lengthOfB // 2) + 1

    aFront = a[0:indexA]
    aBack = a[indexA:]

    bFront = b[0:indexB]
    bBack = b[indexB:]

    return aFront + bFront + aBack + bBack

# Provided simple test() function used in main() to print
# what each function returns vs. what it's supposed to return.


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {}     expected: {}'.format(
        prefix, repr(got), repr(expected)))


# main() calls the above functions with interesting inputs,
# using the above test() to check if the result is correct or not.
def main():
    print('verbing')
    test(verbing('hail'), 'hailing')
    test(verbing('swiming'), 'swimingly')
    test(verbing('do'), 'do')

    print('')
    print('not_bad')
    test(not_bad('This movie is not so bad'), 'This movie is good')
    test(not_bad('This dinner is not that bad!'), 'This dinner is good!')
    test(not_bad('This tea is not hot'), 'This tea is not hot')
    test(not_bad("It's bad yet not"), "It's bad yet not")

    print('')
    print('front_back')
    test(front_back('abcd', 'xy'), 'abxcdy')
    test(front_back('abcde', 'xyz'), 'abcxydez')
    test(front_back('Kitten', 'Donut'), 'KitDontenut')


# This is called the 'import guard' -- it calls the main function.
if __name__ == '__main__':
    main()
