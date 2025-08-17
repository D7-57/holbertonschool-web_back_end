#!/usr/bin/env python3
"""Insert a document"""


def insert_school(mongo_collection, **kwargs):
    """Insert a new document in the given collection"""
    result = mongo_collection.insert_one(dict(kwargs))
    return result.inserted_id
