from functools import wraps


def ensure_no_kwargs(fn):
    """ Raise error if kwargs are passed """
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if kwargs:
            raise ValueError("Don't pass kwargs")
        return fn(*args, **kwargs)
    return wrapper


@ensure_no_kwargs
def greet(name):
    print(f"Hi there {name}")


greet("Tony")
# greet(name="Tony")
