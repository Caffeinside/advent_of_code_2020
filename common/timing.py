from functools import wraps
from time import time


def timing(f):
    @wraps(f)
    def wrap(*args, **kw):
        start_time = time()
        result = f(*args, **kw)
        end_time = time()
        print(f'%r took: %2.4f sec' % (f.__name__, end_time - start_time))
        return result
    return wrap
