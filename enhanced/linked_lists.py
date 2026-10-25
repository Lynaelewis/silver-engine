"""Polished, independently runnable version of the original linked-list exercise.

Original coursework files in the repository root remain unchanged.
"""
from typing import Any, Iterable, Optional


class Node:
    def __init__(self, item: Any, link: Optional["Node"] = None) -> None:
        self.item = item
        self.link = link

    def __repr__(self) -> str:
        return f"Node({self.item!r})"


class LinkedList:
    def __init__(self, items: Optional[Iterable[Any]] = None) -> None:
        self._head: Optional[Node] = None
        self._tail: Optional[Node] = None
        self._size = 0
        if items is not None:
            for item in items:
                self.add_last(item)

    def __len__(self) -> int:
        return self._size

    def get_head(self) -> Any:
        return self._head.item if self._head else None

    def get_tail(self) -> Any:
        return self._tail.item if self._tail else None

    def add_first(self, item: Any) -> None:
        self._head = Node(item, self._head)
        if self._tail is None:
            self._tail = self._head
        self._size += 1

    def add_last(self, item: Any) -> None:
        node = Node(item)
        if self._tail is None:
            self._head = node
        else:
            self._tail.link = node
        self._tail = node
        self._size += 1

    def remove_first(self) -> Any:
        if self._head is None:
            raise RuntimeError("LinkedList is empty")
        item = self._head.item
        self._head = self._head.link
        if self._head is None:
            self._tail = None
        self._size -= 1
        return item

    def remove_last(self) -> Any:
        if self._head is None:
            raise RuntimeError("LinkedList is empty")
        if self._head is self._tail:
            return self.remove_first()
        current = self._head
        while current.link is not self._tail:
            current = current.link
        item = self._tail.item
        current.link = None
        self._tail = current
        self._size -= 1
        return item

    def to_list(self) -> list:
        result = []
        current = self._head
        while current is not None:
            result.append(current.item)
            current = current.link
        return result


class ReversibleLinkedList(LinkedList):
    def reverse(self) -> None:
        previous, current = None, self._head
        self._tail = self._head
        while current is not None:
            following = current.link
            current.link = previous
            previous, current = current, following
        self._head = previous


class SortedLinkedList(LinkedList):
    def __init__(self, items: Optional[Iterable[Any]] = None) -> None:
        super().__init__()
        if items is not None:
            for item in items:
                self.add_sorted(item)

    def add_first(self, item: Any) -> None:
        raise NotImplementedError("Use add_sorted() instead")

    def add_last(self, item: Any) -> None:
        raise NotImplementedError("Use add_sorted() instead")

    def add_sorted(self, item: Any) -> None:
        node = Node(item)
        if self._head is None or item <= self._head.item:
            node.link = self._head
            self._head = node
            if self._tail is None:
                self._tail = node
        else:
            previous = self._head
            while previous.link is not None and previous.link.item < item:
                previous = previous.link
            node.link = previous.link
            previous.link = node
            if node.link is None:
                self._tail = node
        self._size += 1


class UniqueLinkedList(LinkedList):
    def remove_dups(self) -> dict:
        """Remove repeated hashable values; return duplicates removed per value."""
        seen = set()
        counts = {}
        previous = None
        current = self._head
        while current is not None:
            if current.item in seen:
                counts[current.item] = counts.get(current.item, 0) + 1
                previous.link = current.link
                if current is self._tail:
                    self._tail = previous
                self._size -= 1
            else:
                seen.add(current.item)
                counts.setdefault(current.item, 0)
                previous = current
            current = current.link
        return counts
