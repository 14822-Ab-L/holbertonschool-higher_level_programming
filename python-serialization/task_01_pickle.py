#!/usr/bin/env python3
"""Serialize and deserialize a custom Python object."""

import pickle


class CustomObject:
    """Represent a person with basic attributes."""

    def __init__(self, name, age, is_student):
        """Initialise the object's attributes."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Print the object's attributes."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Save this object to a file using pickle."""
        try:
            with open(filename, "wb") as file:
                pickle.dump(self, file)
        except (OSError, pickle.PickleError, AttributeError, TypeError):
            return None

    @classmethod
    def deserialize(cls, filename):
        """Load an object from a pickle file."""
        try:
            with open(filename, "rb") as file:
                obj = pickle.load(file)
        except (
            OSError,
            pickle.PickleError,
            EOFError,
            AttributeError,
            ImportError,
            IndexError,
            TypeError,
            ValueError,
        ):
            return None

        if not isinstance(obj, cls):
            return None

        return obj
