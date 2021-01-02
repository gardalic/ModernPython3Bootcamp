"""
titleize('this is awesome') # "This Is Awesome"
titleize('oNLy cAPITALIZe fIRSt') # "ONLy CAPITALIZe FIRSt"
"""


def titleize(sentence):
    return " ".join(["".join([word[0].upper(), word[1:]]) for word in sentence.split()])


print(titleize("oNLy cAPITALIZe fIRSt"))
