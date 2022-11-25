"""List implementation of a set."""

from typing import (
    Generic, Iterable, TypeVar
)

T = TypeVar('T')


class ListSet(Generic[T]):
    """A set of elements of type T."""

    data: list[T]

    def __init__(self, init: Iterable[T]) -> None:
        """Initialise set with init."""
        self.data = list()
        for x in init:
            self.add(x)
    # O(n^2) time

    def __contains__(self, x: T) -> bool:
        """Test if x is in set."""
        return x in self.data
    # O(n), n is size of ListSet

    def __bool__(self) -> bool:
        """
        Return truth value of the set.

        A set is True if it is non-empty and False
        otherwise
        """
        return bool(self.data)
    # O(1), one simple assertion

    def __str__(self) -> str:
        """ ~ Pretty print ~ """
        return str(self.data)
    # O(n), length n

    def add(self, x: T) -> None:
        """Add x to the set."""
        if x not in self.data:
            self.data.append(x)
    # O(n) for searching + O(1) for appending = O(n)

    def remove(self, x: T) -> None:
        """Remove x from the set."""
        if x in self.data:
            self.data.remove(x)
    # O(n) for searching + O(n) removing = O(n)

    def delete(self) -> None:
        """Deletes ListSet"""
        self.data = []
    # O(1)