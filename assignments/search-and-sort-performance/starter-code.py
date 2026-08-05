"""Starter code for Search and Sort Performance assignment."""

from __future__ import annotations

from random import randint
from time import perf_counter


def linear_search(records: list[dict[str, int]], target_score: int) -> int:
    """Return index of first record with target_score, or -1 if not found."""
    # TODO: Implement linear search.
    raise NotImplementedError


def binary_search(sorted_records: list[dict[str, int]], target_score: int) -> int:
    """Return index of a record with target_score in a sorted list, or -1."""
    # TODO: Implement binary search.
    raise NotImplementedError


def bubble_sort(records: list[dict[str, int]]) -> list[dict[str, int]]:
    """Return a new list sorted by score using bubble sort."""
    # TODO: Implement bubble sort without mutating input.
    raise NotImplementedError


def insertion_sort(records: list[dict[str, int]]) -> list[dict[str, int]]:
    """Return a new list sorted by score using insertion sort."""
    # TODO: Implement insertion sort without mutating input.
    raise NotImplementedError


def generate_records(size: int) -> list[dict[str, int]]:
    """Generate synthetic student records with random scores."""
    return [{"id": i, "score": randint(0, 100)} for i in range(size)]


def benchmark() -> None:
    """Benchmark algorithms across multiple dataset sizes."""
    sizes = [100, 1_000, 5_000]

    print(f"{'Algorithm':<18} {'Size':>8} {'Time (s)':>12}")
    print("-" * 40)

    for size in sizes:
        records = generate_records(size)
        target = records[size // 2]["score"]

        start = perf_counter()
        linear_search(records, target)
        elapsed = perf_counter() - start
        print(f"{'linear_search':<18} {size:>8} {elapsed:>12.6f}")

        start = perf_counter()
        bubble_sort(records)
        elapsed = perf_counter() - start
        print(f"{'bubble_sort':<18} {size:>8} {elapsed:>12.6f}")

        start = perf_counter()
        insertion_sort(records)
        elapsed = perf_counter() - start
        print(f"{'insertion_sort':<18} {size:>8} {elapsed:>12.6f}")

        sorted_records = sorted(records, key=lambda item: item["score"])
        start = perf_counter()
        binary_search(sorted_records, target)
        elapsed = perf_counter() - start
        print(f"{'binary_search':<18} {size:>8} {elapsed:>12.6f}")


if __name__ == "__main__":
    benchmark()
