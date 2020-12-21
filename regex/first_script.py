import re

pattern = re.compile(r"\d{3} \d{3}-\d{4}")

res = pattern.search("1334sa")
print(res)

res = pattern.search("Call me at 310 455-9876 or 310 455-4536")
print(res)
print(res.group())