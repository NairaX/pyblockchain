#!/usr/bin/env python
# encoding: utf-8

import json

from hashlib import sha256


class Hasher(object):

    @staticmethod
    def hash(index, timestamp, previous_hash, nonce, difficulty, data):
        params = {
            'index': index,
            'timestamp': timestamp,
            'previous_hash': previous_hash,
            'nonce': nonce,
            'difficulty': difficulty,
            'data': data,
        }
        seed = json.dumps(params, sort_keys=True).encode()
        return sha256(seed).hexdigest()

    @classmethod
    def get_hash(cls, block):
        return cls.hash(block.__dict__)
