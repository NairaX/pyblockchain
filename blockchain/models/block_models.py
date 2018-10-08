#!/usr/bin/env python
# encoding: utf-8


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
