#!/usr/bin/env python3
"""Update the topics of school documen"""
from typing import List


def update_topics(mongo_collection, name: str, topics: List[str]) -> None:
    """Change all topics of school document"""
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
