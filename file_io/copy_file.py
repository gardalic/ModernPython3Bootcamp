"""Write a function called copy, which takes in a file name and a new file name and copies the contents of the first file to the second file."""


def copy(file1, file2):
    with open(file1) as f:
        contents = f.read()

    with open(file2, "w") as f2:
        f2.write(contents)
