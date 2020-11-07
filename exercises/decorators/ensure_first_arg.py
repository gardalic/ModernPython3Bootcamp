""" Code along, write a decorator to insure the first argument is 'burrito' """

from functools import wraps

def ensure_first_arg_is(val):
    def inner(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            if args and args[0] != val:
                return f"First arg needs to be {val}!"
            else:
                return fn(*args, **kwargs)
        return wrapper
    return inner

