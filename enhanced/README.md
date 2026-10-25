# Linked List Portfolio Improvements

This folder contains an **enhanced, separately documented adaptation** of the Python linked-list coursework in the repository root. The original files (`linkedlist`, `extendedlinkedlist`, `exam3`, and the root `README.md`) have **not been edited or deleted**.

## What it demonstrates

- Object-oriented programming through inheritance and encapsulation
- Singly linked lists with head, tail, and size tracking
- In-place reversal in O(n) time
- Sorted insertion in O(n) time
- Duplicate removal with a hash set (expected O(n) time for hashable elements)
- Standard-library unit testing, including empty-list and boundary cases

## Files

- `linked_lists.py` — Enhanced standalone implementation
- `test_linked_lists.py` — Six unit tests

## Run the tests

From the repository root:

```bash
cd enhanced
python -m unittest -v test_linked_lists.py
```

Or run an interactive example:

```python
from linked_lists import ReversibleLinkedList
values = ReversibleLinkedList([1, 2, 3])
values.reverse()
print(values.to_list())  # [3, 2, 1]
```

## Notes on authorship

The root-level files are the original coursework. The files in this folder are a later portfolio-focused refinement, with clearer naming, corrected syntax, additional boundary handling, and tests. They should not be represented as unchanged coursework submissions.

## Limitations

- Sorted values must be mutually comparable.
- Duplicate detection requires hashable values.
- This is a data-structures learning project, not a cybersecurity tool.
