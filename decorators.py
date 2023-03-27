import functools
import inspect

def debug(func):
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        all_vars = inspect.getframeinfo(inspect.currentframe().f_back)[0].f_locals
        print(f"Calling {func.__name__} with arguments: {args}, {kwargs}")
        print("Local variables:")
        for var_name, var_value in all_vars.items():
            print(f"\t{var_name} = {var_value}")
 
        return func(*args, **kwargs)
    return wrapper_debug
