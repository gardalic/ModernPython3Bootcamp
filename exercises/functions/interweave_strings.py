"""
    Write a function interleave that accepts two strings.  It should return a new string containing the 2 strings interwoven or zipped together. For example:
    interleave('hi','ha') # 'hhia'
    interleave('aaa', 'zzz')# 'azazaz'
    interleave('lzr','iad')#  'lizard'
"""

def interleave(first, second):
    return "".join("".join(x) for x in zip(first, second))

print(interleave('aaa', 'zzz'))