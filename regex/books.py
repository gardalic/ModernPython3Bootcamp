import re

titles = [
    "Significant Others (1987)",
    "Tales of the City (1978)",
    "The Days of Anna Madrigal (2014)",
    "Mary Ann in Autumn (2010)",
    "Further Tales of the City (1982)",
    "Babycakes (1984)",
    "More Tales of the City (1980)",
    "Sure of You (1989)",
    "Michael Tolliver Lives (2007)",
    "Test Movie Without Year"
]


def format_movie(movie) -> str:
    pattern = re.compile(r"^([\w ]+) \((\d{4})\)")
    return pattern.sub("\g<2> - \g<1>", movie)


formated_titles = []
for title in titles:
    formated_titles.append(format_movie(title))

formated_titles.sort()
print(formated_titles)
