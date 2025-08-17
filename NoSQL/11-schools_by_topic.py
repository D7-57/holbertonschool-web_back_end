#!/usr/bin/env python3
"""Return schools that cover a specific topic."""


def schools_by_topic(mongo_collection, topic):
    """Return a list of school documents"""
    return list(mongo_collection.find({"topics": topic}))
