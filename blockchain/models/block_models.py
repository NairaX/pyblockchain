#!/usr/bin/env python
# encoding: utf-8

import json


class Block(object):

    def __init__(self, index, timestamp, previous_hash, hash, nonce, difficulty, data):
        self.index = index
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.hash = hash
        self.nonce = nonce
        self.difficulty = difficulty
        self.data = data

    def __str__(self):
        return """Block -
            Index         : {index}
            Timestamp     : {timestamp}
            Previous hash : {previous_hash}
            Hash          : {hash}
            Nonce         : {nonce}
            Difficulty    : {difficulty}
            Data          : {data}
            """.format(**self.__dict__)

    @classmethod
    def genesis(cls):
        return cls(1, 'Genesis time', '', 'Genesis hash', 0, 1, 'Genesis block')

    def serialize(self):
        return {
            'Index': self.index,
            'Timestamp': self.timestamp,
            'Previous hash': self.previous_hash,
            'Hash': self.hash,
            'Nonce': self.nonce,
            'Difficulty': self.difficulty,
            'Data': self.data
        }

    @classmethod
    def deserialize(cls, json_obj):
        return cls(**json.loads(json_obj))
