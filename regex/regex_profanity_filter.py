"""
    Define a function called censor  that accepts a single string. Rather than censoring any real
    profanity, we're going to censor any words that start with "frack".  This includes "fracking", "fracker",
    "frack", etc.  Replace the entire word with the string "CENSORED".  Your regex should be case insensitive.
    For example:
        censor("Frack you") # CENSORED you
        censor("I hope you fracking die") # I hope you CENSORED die
        censor("you fracking Frack") # you CENSORED CENSORED
"""
import re


def censor(text) -> str:
    pattern = re.compile(r"\bfrack\w*\b", re.IGNORECASE)
    # match = re.findall(pattern, text)
    # if re.findall(pattern, text):
    #     return re.sub(pattern, "CENSORED", text)
    # else:
    #     return text
    return re.sub(pattern, "CENSORED", text)


print(censor("Frack you"))  # CENSORED you
print(censor("I hope you fracking die"))  # I hope you CENSORED die
print(censor("you fracking Frack"))  # you CENSORED CENSORED
print(censor("no match test"))
