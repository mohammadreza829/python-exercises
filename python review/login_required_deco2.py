import functools


def login_required(func):
    @functools.wraps(func)
    def inner(username):
        if username in lstt:
            return func(username)
        else:
            return "you are not logged in"

    return inner

lstt =["ali", "sara", "reza"]
@login_required
def hell(username):
    print(f"hello {username}")


# hell('ali')
hell("hacker")
