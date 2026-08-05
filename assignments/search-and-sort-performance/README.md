# 📘 Assignment: Search and Sort Performance

## 🎯 Objective

Implement and compare search and sorting algorithms in Python to understand correctness, efficiency, and when each approach should be used.

## 📝 Tasks

### 🛠️ Implement Search Algorithms

#### Descrição
Create functions for linear search and binary search to find a target score in a dataset of student records.

#### Requisitos
O programa concluído deve:

- Implement `linear_search(records, target_score)` and return the matching index or `-1`
- Implement `binary_search(sorted_records, target_score)` and return the matching index or `-1`
- Ensure binary search works only on data sorted by score
- Handle edge cases: empty list, first element, last element, and missing value

### 🛠️ Implement Sorting Algorithms

#### Descrição
Implement sorting functions to rank records by score and compare algorithm behavior.

#### Requisitos
O programa concluído deve:

- Implement `bubble_sort(records)` to return a new list sorted by score (ascending)
- Implement `insertion_sort(records)` to return a new list sorted by score (ascending)
- Keep the original input list unchanged
- Validate correctness by comparing output against Python's `sorted(..., key=...)`

### 🛠️ Benchmark and Analyze Complexity

#### Descrição
Measure execution time for each algorithm using datasets with different sizes and describe observed complexity trends.

#### Requisitos
O programa concluído deve:

- Generate datasets with at least 100, 1_000, and 5_000 records
- Time each algorithm with `time.perf_counter()`
- Print a comparison table with algorithm name, input size, and elapsed time
- Write a short analysis in comments explaining expected complexity (`O(n)`, `O(log n)`, `O(n²)`) and whether results match expectations
