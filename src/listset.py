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
        self.init = init
    # O(1) time

    def __contains__(self, x: T) -> bool:
        """Test if x is in set."""
        if x in self.init:
            return True
        else:
            return False
    # O(n), n is size of ListSet

    def __bool__(self) -> bool:
        """
        Return truth value of the set.

        A set is True if it is non-empty and False
        otherwise
        """
        if self.init == []:
            return False
        else:
            return True
    # O(1), one simple assertion

    def add(self, x: T) -> None:
        """Add x to the set."""
        if x not in self.init:
            self.init.append(x)
    # O(n) for searching + O(1) for appending = O(n)

    def remove(self, x: T) -> None:
        """Remove x from the set."""
        if x in self.init:
            self.init.remove(x)
    # O(n) for searching + O(n) for searching and removing = O(n)
