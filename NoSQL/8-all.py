#!/usr/bin/env python3
"""List all documents"""


def list_all(mongo_collection):
    """Return all documents from the given collection"""
    return list(mongo_collection.find())
