"""
    Write a function called combine_words which accepts a single string called word and any number of additional key word arguments.  If a prefix is provided, return the prefix followed by the word.  If a suffix is provided, return the word followed by the suffix.  If neither is provided, just return the word.  It might sound confusing, but the examples should make this a lot clearer!
"""


def combine_words(word, **kwargs):
    v_word = word
    if 'prefix' in kwargs:
        v_word = str(kwargs['prefix']) + v_word
    if 'suffix' in kwargs:
        v_word = v_word + str(kwargs['suffix'])
    return v_word


print(f"Just prefix: {combine_words('child', prefix='man')}")

print(f"Just suffix: {combine_words('child', suffix='ish')}")

print(f"Both: {combine_words('child', prefix='man', suffix='ish')}")
