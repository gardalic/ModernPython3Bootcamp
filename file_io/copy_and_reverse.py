"""Write a function called copy, which takes in a file name and a new file name, _copies and reverses_ the contents of the first file to the second file."""

def copy_and_reverse(file1, file2):
    with open(file1) as f:
        contents = f.read()
    
    with open(file2, 'w') as f:
        f.write(contents[::-1])