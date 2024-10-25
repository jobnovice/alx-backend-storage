#!/usr/bin/env python3
"""installed and configured redis to writing strings to it """
from typing import Union, Optional, Callable
from functools import wraps
import redis
import uuid


def count_calls(method: Callable) -> Callable:
    """used a decorator to implement the INCR of redis"""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """wrapped the instance methods"""
        key = method.__qualname__
        self._redis.incr(key)

        return method(self, *args, **kwargs)
    return wrapper


class Cache():
    """created a class for storing an instance of redis as a client"""
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """stores the inputed data and returns the random key"""
        random_key = str(uuid.uuid4())
        self._redis.set(random_key, data)

        return random_key

    @count_calls
    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str,
                                                    bytes,
                                                    int,
                                                    float,
                                                    None]:
        """method to use the redis"""
        value = self._redis.get(key)
        if value is None:
            return None
        if fn:
            return fn(value)
        return value

    @count_calls
    def get_str(self, key: str) -> str:
        """converts the data to its readable format"""
        return self.get(key, fn=lambda d: d.decode('utf-8'))

    @count_calls
    def get_int(self, key: int) -> int:
        """converts the data to its apprpopiate format which isint"""
        return self.get(key, fn=int)
