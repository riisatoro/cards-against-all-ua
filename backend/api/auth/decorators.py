from functools import wraps
from typing import Optional

from fastapi import Header


def login_required(func):
    @wraps(func)
    def wrapper(access: Optional[str] = Header('Authentication'), *args, ** kwargs):
        print(args, kwargs, access)
        return func(*args, **kwargs)
    
    return wrapper