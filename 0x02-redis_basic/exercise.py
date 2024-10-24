#!/usr/bin/env python3
"""installed and configured redis to writing strings to it """
from typing import Union
import redis
import uuid


class Cache():
    """created a class for storing an instance of redis as a client"""
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[bytes, str, int, float]) -> str:
        """stores the inputed data and returns the random key"""
        random_key = str(uuid.uuid4())
        self._redis.set(random_key, data)

        return random_key
