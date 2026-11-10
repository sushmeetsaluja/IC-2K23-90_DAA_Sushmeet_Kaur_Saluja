# DAA Lab Task 1

This repository contains solutions for Part 1, Part 2, and Part 3 of DAA Lab Task 1.

---

## Part 1. Trace It Yourself

### Input

`8, 3, 15, 6, 2`

### Output

Largest number: `15`

Sorted list: `2, 3, 6, 8, 15`

### Comparisons Made

`4`

### Dry Run

| i | A[i] | max | comparisons |
|---|------|-----|-------------|
| 1 | 3 | 8 | 1 |
| 2 | 15 | 15 | 2 |
| 3 | 6 | 15 | 3 |
| 4 | 2 | 15 | 4 |

The first element `8` is taken as the initial maximum. The remaining elements are checked one by one.

### Sorting Method Used

**Selection Sort**

### Sorting Steps

```text
Initial: 8, 3, 15, 6, 2

Step 1: 2, 3, 15, 6, 8
Step 2: 2, 3, 15, 6, 8
Step 3: 2, 3, 6, 15, 8
Step 4: 2, 3, 6, 8, 15
```

Final sorted list:

`2, 3, 6, 8, 15`

### Explanation

The first number is considered the maximum initially. Every remaining number is compared with the current maximum, and it is updated whenever a larger value is found.

Selection Sort finds the smallest value from the unsorted part of the list and places it in its correct position.

### Data Structure Used

**List**

### Complexity

Finding maximum: **O(n)**

Selection Sort: **O(n²)**

---

## Part 2. Stack or Queue

### Input

`Task1, Task2, Task3, Task4, Task5`

### Stack Order

Stack follows **LIFO (Last In, First Out)**.

```text
Task5 → Task4 → Task3 → Task2 → Task1
```

### Queue Order

Queue follows **FIFO (First In, First Out)**.

```text
Task1 → Task2 → Task3 → Task4 → Task5
```

### Printer Should Use

**Queue**

### Reason

A printer should process jobs in the order in which they arrive. A queue follows FIFO, so the first job received by the printer is the first job processed.

### Dry Run

**Stack (LIFO)**

```text
Push: Task1, Task2, Task3, Task4, Task5

Pop: Task5, Task4, Task3, Task2, Task1
```

**Queue (FIFO)**

```text
Enqueue: Task1, Task2, Task3, Task4, Task5

Dequeue: Task1, Task2, Task3, Task4, Task5
```

### Data Structures Used

**Stack and Queue**

### Complexity

Processing all tasks takes **O(n)** time.

---

## Part 3. Build a Small Tree

### Input

Subjects:

`Math, Science, Algebra, Geometry, Physics, Chemistry`

Math and Science are top-level subjects.

Algebra and Geometry come under Math.

Physics and Chemistry come under Science.

### Tree

```text
          Math                 Science
         /    \               /       \
    Algebra   Geometry    Physics   Chemistry
```

### Dry Run

```text
Level 0: Math, Science

Level 1 under Math:
Algebra, Geometry

Level 1 under Science:
Physics, Chemistry
```

### Level Order Traversal

```text
Math → Science → Algebra → Geometry → Physics → Chemistry
```

### Explanation

Level-order traversal visits all nodes of one level before moving to the next level. A queue can be used to maintain the order in which the nodes need to be visited.

### Data Structures Used

**Tree** for representing the subject hierarchy.

**Queue** for level-order traversal.

### Complexity

Level-order traversal takes **O(n)** time because every node is visited once.

---

## Input Growth Analysis

If the input becomes **100 times larger**:

- An **O(n)** operation will require approximately **100 times** more work.
- An **O(n²)** operation will require approximately **10,000 times** more work.

Therefore, maximum finding, stack/queue processing, and tree traversal grow **proportionally**, while Selection Sort grows much faster as the input size increases.

---

## How to Run

```bash
python part1_trace.py
python part2_stack_queue.py
python part3_tree.py
```



## Language

Python