# DAA Lab Assignments — Sushmeet Kaur Saluja

**Student Name:** Sushmeet Kaur Saluja  
**Roll Number / Student ID:** IC-2K23-90  
**Subject:** Design and Analysis of Algorithms (DAA) Laboratory  
**Repository:** DAA Lab Assignments  

---

## Repository Overview

This repository contains the submitted work for **DAA Lab Tasks 1, 2, and 3**. It includes Python implementations, written answers, dry-run traces, complexity discussions, empirical timing results, and performance graphs.

The work is organized into separate folders for each laboratory task.

## Repository Structure

```text
IC-2K23-90_DAA_Sushmeet_Kaur_Saluja-main/
│
├── README.md                              # Root repository documentation
│
├── DAA-LAB-TASK-1/                        # Lab Task 1: Basic algorithms and data structures
│   ├── README.md                          # Task 1 explanations, dry runs, and complexity
│   ├── part1_trace.py                     # Maximum element and Selection Sort trace
│   ├── part2_stack_queue.py               # Stack (LIFO) and Queue (FIFO) simulation
│   └── part4_complexity.py                # Single-loop and nested-loop step counting
│
├── DAA-LAB-TASK-2/                        # Lab Task 2: Arrays, searching, and sparse matrices
│   ├── section-a,b.md                     # Concept check and logic-tracing answers
│   ├── Section-B -question-1/
│   │   ├── 1D.py                           # 1D array operations
│   │   └── 1D.md                           # Explanation and examples
│   ├── SectionB-Question-2/
│   │   ├── 2D.py                           # 2D array and matrix operations
│   │   └── 2D.md                           # Explanation and examples
│   ├── Section-B-question-3/
│   │   ├── Sparse_matrix.py                # Sparse matrix conversion and reconstruction
│   │   └── sparse_matrix.md                # Sparse matrix documentation
│   ├── Section-B-question-4/
│   │   ├── matrix_cal.py                   # Matrix calculations
│   │   └── matrix_cal.md                  # Matrix calculation documentation
│   └── section-d/
│       └── optimization.md                # Sparse matrix space-optimization analysis
│
└── DAA-LAB-TASK-3/                        # Lab Task 3: Sorting, hashing, and benchmarking
    ├── README.md                          # Complete Task 3 lab report
    ├── program1_basic_sorts.py             # Bubble, Selection, and Insertion Sort
    ├── program2_advanced_sorts.py          # Merge, Quick, and Heap Sort
    ├── program3_radix_sort.py               # LSD Radix Sort
    ├── program4_binary_search.py            # Iterative Binary Search
    ├── program5_timing_analysis.py          # Empirical sorting benchmarks
    ├── program6_graphing.py                 # Matplotlib graph generation
    ├── timing_results.csv                  # Raw benchmark results
    ├── graph_random.png                     # Sorting performance on random input
    ├── graph_sorted.png                     # Sorting performance on sorted input
    ├── program7_student_manager.py          # Student Record Manager
    └── program8_search_engine.py            # Search Engine Simulator
```

---

## Detailed Task Descriptions

### 1. `DAA-LAB-TASK-1` — Basic Algorithms, Stacks, Queues, and Complexity

This task covers introductory algorithmic problem-solving, linear data structures, and basic time-complexity analysis.

- **`part1_trace.py` — Trace It Yourself**
  - Finds the maximum value in the input list `8, 3, 15, 6, 2`.
  - Demonstrates Selection Sort on the same list.
  - The maximum is `15`, found using `4` comparisons.
  - Includes the sorting steps and complexity discussion.
- **`part2_stack_queue.py` — Stack or Queue**
  - Demonstrates Stack operations using **LIFO (Last In, First Out)**.
  - Demonstrates Queue operations using **FIFO (First In, First Out)**.
  - Explains why a printer job-processing system should use a Queue.
- **`part4_complexity.py` — Count the Steps**
  - Counts iterations in a single loop and a nested loop.
  - Demonstrates linear `O(n)` and quadratic `O(n²)` growth.
  - Includes input-growth analysis.
- **`README.md`**
  - Contains the task explanations, dry runs, examples, and instructions for running the Python programs.

**Note:** The supplied Task 1 folder contains Parts 1, 2, and 4; no Part 3 file is included in this repository snapshot.

### 2. `DAA-LAB-TASK-2` — Arrays, Searching, Matrices, and Space Optimization

This task focuses on array manipulation, searching techniques, matrix operations, and sparse matrix representation.

- **`section-a,b.md` — Concept Check and Logic Tracing**
  - Covers Python lists, insertion and deletion, array rotation, linear search, binary search, and sparse matrix triples.
  - Includes dry runs for array operations and search procedures.
  - Represents non-zero matrix values using `(row, column, value)` triples.
- **`Section-B -question-1/` — 1D Array Operations**
  - `1D.py` implements insertion, deletion, and left rotation operations.
  - `1D.md` documents the operations and their examples.
- **`SectionB-Question-2/` — 2D Array Operations**
  - `2D.py` contains 2D array and matrix-processing operations.
  - `2D.md` provides the corresponding explanation and examples.
- **`Section-B-question-3/` — Sparse Matrix Representation**
  - `Sparse_matrix.py` converts matrices into sparse triple form and supports reconstruction.
  - `sparse_matrix.md` explains the representation and implementation.
- **`Section-B-question-4/` — Matrix Calculations**
  - `matrix_cal.py` implements matrix calculations, including addition, multiplication, and transpose.
  - `matrix_cal.md` documents the operations.
- **`section-d/` — Space Optimization Analysis**
  - `optimization.md` compares full matrix storage with sparse triple storage.
  - Includes sparse and dense test cases, storage calculations, the crossover condition, and a real-world sparse-matrix example.

### 3. `DAA-LAB-TASK-3` — Sorting Algorithms, Hashing, Empirical Timing, and Applications

This task implements and compares sorting and searching algorithms, explores hashing, and applies the concepts to small application scenarios.

#### A. Sorting and Searching Programs

- **`program1_basic_sorts.py`**
  - Implements Bubble Sort, Selection Sort, and Insertion Sort.
  - Demonstrates the sorting process and array states.
- **`program2_advanced_sorts.py`**
  - Implements Merge Sort, Quick Sort, and Heap Sort.
  - Quick Sort uses the last element as its pivot.
- **`program3_radix_sort.py`**
  - Implements Least Significant Digit (LSD) Radix Sort for non-negative integers.
  - Uses a stable digit-sorting procedure.
- **`program4_binary_search.py`**
  - Implements iterative Binary Search.
  - Demonstrates searching for present and absent values.

#### B. Empirical Timing and Graphs

- **`program5_timing_analysis.py`**
  - Benchmarks six comparison-based sorting algorithms.
  - Tests random, already-sorted, and reverse-sorted input.
  - Uses input sizes `100`, `500`, `1000`, and `2000`.
  - Saves timing measurements in `timing_results.csv`.
- **`program6_graphing.py`**
  - Reads the timing dataset and generates Matplotlib comparison graphs.
- **`timing_results.csv`**
  - Stores the measured execution times.
- **`graph_random.png`**
  - Visualizes sorting performance on random input.
- **`graph_sorted.png`**
  - Visualizes sorting performance on already-sorted input.

#### C. Application Programs

- **`program7_student_manager.py` — Student Record Manager**
  - Manages student records containing roll numbers, names, and marks.
  - Supports sorting records using the implemented sorting algorithms.
  - Demonstrates Binary Search by roll number.
  - Includes a comparative sorting-performance report.
- **`program8_search_engine.py` — Search Engine Simulator**
  - Simulates keyword searching over a collection of computer-science terms.
  - Compares Binary Search with hash-table lookup.
  - Demonstrates Separate Chaining and Linear Probing collision-handling techniques.
  - Reports search comparisons and probe counts.

The detailed theory, traces, timing tables, sample results, and analysis for Task 3 are documented in the `DAA-LAB-TASK-3/README.md` file.

---

## Technologies and Concepts Used

| Area | Tools / Concepts |
|---|---|
| Programming language | Python |
| Data structures | Lists, stacks, queues, matrices, heaps, hash tables |
| Sorting | Bubble, Selection, Insertion, Merge, Quick, Heap, Radix |
| Searching | Linear Search, Binary Search, Hash-based lookup |
| Matrix processing | 1D arrays, 2D arrays, sparse triple representation |
| Complexity analysis | Big-O notation, time and space complexity |
| Benchmark visualization | Matplotlib |
| Benchmark data | CSV |

---

## How to Run the Programs

Run commands from the repository's root directory. Paths containing spaces should be enclosed in quotation marks.

### Prerequisites

Python 3 is required. Matplotlib is needed for the Task 3 graphing program.

```bash
python --version
python -m pip install matplotlib
```

### Task 1

```bash
python "DAA-LAB-TASK-1/part1_trace.py"
python "DAA-LAB-TASK-1/part2_stack_queue.py"
python "DAA-LAB-TASK-1/part4_complexity.py"
```

### Task 2

```bash
python "DAA-LAB-TASK-2/Section-B-Q1/1D.py"
python "DAA-LAB-TASK-2/Section-B-Q2/2D.py"
python "DAA-LAB-TASK-2/Section-B-Q3/Sparse_matrix.py"
python "DAA-LAB-TASK-2/Section-B-Q4/matrix_cal.py"
```

The Task 2 written answers and explanations are available in the corresponding `.md` files.

### Task 3

```bash
python "DAA-LAB-TASK-3/program1_basic_sorts.py"
python "DAA-LAB-TASK-3/program2_advanced_sorts.py"
python "DAA-LAB-TASK-3/program3_radix_sort.py"
python "DAA-LAB-TASK-3/program4_binary_search.py"
python "DAA-LAB-TASK-3/program5_timing_analysis.py"
python "DAA-LAB-TASK-3/program6_graphing.py"
python "DAA-LAB-TASK-3/program7_student_manager.py"
python "DAA-LAB-TASK-3/program8_search_engine.py"
```

Run the timing-analysis program before graphing if you want to regenerate the benchmark dataset and plots.

---

## Student Information

| Field | Details |
|---|---|
| Student Name | **Sushmeet Kaur Saluja** |
| Roll Number | **IC-2K23-90** |
| Subject | Design and Analysis of Algorithms (DAA) Laboratory |

---

*This repository is maintained as the lab-work submission for the Design and Analysis of Algorithms course.*
