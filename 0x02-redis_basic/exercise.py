#!/usr/bin/env python3
"""installed and configured redis to writing strings to it """
from typing import Union, Optional, Callable
import redis
import uuid


class Cache():
    """created a class for storing an instance of redis as a client"""
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """stores the inputed data and returns the random key"""
        random_key = str(uuid.uuid4())
        self._redis.set(random_key, data)

        return random_key

    def get(self, key: str, fn: Optional[Callable] = None)
    -> Union[str, bytes, int, float, None]:
        """method to use the redis"""
        value = self._redis.get(key)
        if value is None:
            return None
        if fn:
            return fn(value)
        return value

    def get_str(self, key: str) -> str:
        """converts the data to its readable format"""
        return self.get(key, fn=lambda d: d.decode('utf-8'))

    def get_int(self, key: int) -> int:
        """converts the data to its apprpopiate format which isint"""
        return self.get(key, fn=int)
