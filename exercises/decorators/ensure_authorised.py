'''
@ensure_authorized
def show_secrets(*args, **kwargs):
    return "Shh! Don't tell anybody!"

show_secrets(role="admin") # "Shh! Don't tell anybody!"
show_secrets(role="nobody") # "Unauthorized"
show_secrets(a="b") # "Unauthorized"
'''

from functools import wraps


def ensure_authorized(fn):
    @wraps(fn)
    def inner(*args, **kwargs):
        if kwargs.get("role") == "admin":
            return fn(*args, **kwargs)
        return "Unauthorized"
    return inner


@ensure_authorized
def show_secrets(*args, **kwargs):
    return "Shh! Don't tell anybody!"


print(show_secrets(role="admin"))  # "Shh! Don't tell anybody!"
print(show_secrets(role="nobody"))  # "Unauthorized"
print(show_secrets(a="b"))  # "Unauthorized"
