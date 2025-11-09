import functools
def dec(func):
    @functools.wraps(func)
    def inner():
        print(f"تابع{func.__name__} فراخوانی شد")
        func()
        print(f"تابع{func.__name__} پایان یافت")
    return inner

@dec
def out():
    print("hello")
    
out()
    