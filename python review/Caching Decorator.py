import functools

def cache_result(func):

    catch = {}
    
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if args in catch:
            return catch[args]
        else:
            result = func(*args, **kwargs)
            catch[args] = result
            return result
    
    return wrapper


@cache_result
def expensive_calculation(n):
    print(f"⏳ محاسبه برای {n}...")
    return n ** 2

print(expensive_calculation(5)) 
print(expensive_calculation(5))  
print(expensive_calculation(10)) 
