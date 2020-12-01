def my_for(iterable, func):
    iterator = iter(iterable)

    while True:
        try:
            i = next(iterator)
        except StopIteration:
            break
        else:
            func(i)


my_for("Test string", print)
