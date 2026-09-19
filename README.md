# LeetCode Solutions

<p align="center">
  <strong>48 problems solved. One repository for deliberate problem solving.</strong><br/>
  Algorithms, data structures, SQL, complexity analysis, and interview-focused practice.
</p>

<p align="center">
  <a href="https://leetcode.com/"><img src="https://img.shields.io/badge/LeetCode-Practice-FFA116?style=for-the-badge&logo=leetcode&logoColor=black" alt="LeetCode"/></a>
  <img src="https://img.shields.io/badge/Problems-48-111827?style=for-the-badge" alt="48 problems solved"/>
  <img src="https://img.shields.io/badge/Python-Solutions-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/SQL-Solutions-336791?style=for-the-badge&logo=postgresql&logoColor=white" alt="SQL"/>
  <img src="https://img.shields.io/github/last-commit/RITESH2127/LEETCODE?style=for-the-badge" alt="Last commit"/>
</p>

<p align="center">
  <a href="#overview">Overview</a> ·
  <a href="#progress">Progress</a> ·
  <a href="#patterns-covered">Patterns</a> ·
  <a href="#repository-structure">Structure</a> ·
  <a href="#how-to-use">How to Use</a> ·
  <a href="#roadmap">Roadmap</a>
</p>

---

## Overview

This repository is a continuously evolving collection of **LeetCode problem solutions** built around a simple principle:

> **Understand the pattern, solve it cleanly, analyze the trade-offs, then move on to the next problem.**

The repository combines **algorithmic problem solving** with **SQL/database interview practice**, with solutions organized by LeetCode problem ID so every exercise is easy to locate, study, and revisit.

The current collection contains **48 solved problems**, including **27 Easy, 20 Medium, and 1 Hard** according to the repository's tracked statistics.

---

# Progress

| Difficulty | Solved |
|:---|---:|
| Easy | 27 |
| Medium | 20 |
| Hard | 1 |
| **Total** | **48** |

### Problem Mix

~~~text
48 solved problems
│
├── Algorithmic problem solving
│   ├── Arrays
│   ├── Strings
│   ├── Hashing
│   ├── Two Pointers
│   ├── Linked Lists
│   ├── Recursion
│   ├── Backtracking
│   ├── Dynamic Programming
│   ├── Greedy techniques
│   └── Mathematical problems
│
└── SQL / Database problem solving
    ├── Filtering
    ├── JOINs
    ├── Aggregation
    ├── GROUP BY / HAVING
    ├── Subqueries
    ├── Window-function patterns
    └── Conditional logic
~~~

> Counts are based on the repository's current `stats.json` and can change as new solutions are added.

---

# Patterns Covered

## Arrays and Searching

The collection uses common techniques for reducing brute-force solutions into efficient search and traversal strategies.

- Hash maps
- Sorting
- Two pointers
- In-place modification
- Multi-pointer traversal
- Target-oriented search

Representative problems:

| Problem | Core pattern |
|---|---|
| [Two Sum](0001-two-sum) | Hash map lookup |
| [Remove Element](0027-remove-element) | In-place array manipulation |
| [Container With Most Water](0011-container-with-most-water) | Two pointers |
| [3Sum](0015-3sum) | Sorting + two pointers |
| [3Sum Closest](0016-3sum-closest) | Target search |
| [4Sum](0018-4sum) | Multi-pointer reduction |

## Strings and Parsing

String problems cover traversal, comparison, mapping, pattern recognition, and parsing.

| Problem | Core pattern |
|---|---|
| [Zigzag Conversion](0006-zigzag-conversion) | Structured traversal |
| [Integer to Roman](0012-integer-to-roman) | Greedy mapping |
| [Roman to Integer](0013-roman-to-integer) | Parsing |
| [Longest Common Prefix](0014-longest-common-prefix) | Prefix comparison |
| [Regular Expression Matching](0010-regular-expression-matching) | Dynamic programming |

## Linked Lists

The collection includes linked-list manipulation through [Add Two Numbers](0002-add-two-numbers), focusing on pointer movement, carry propagation, node construction, and traversal.

## Recursion and Backtracking

These problems reinforce recursive decomposition, state-space exploration, and search-tree reasoning.

Examples include [Letter Combinations of a Phone Number](0017-letter-combinations-of-a-phone-number) and [Regular Expression Matching](0010-regular-expression-matching).

## Dynamic Programming and Greedy Thinking

The repository includes problems where recognizing state transitions, reusable subproblems, or locally optimal decisions is central to the solution.

---

# SQL / Database Practice

The SQL track focuses on common data-interview patterns and on translating business requirements into relational logic.

| Pattern | Typical techniques |
|---|---|
| Filtering | `WHERE`, comparisons, `IN` |
| NULL handling | `IS NULL`, `IS NOT NULL` |
| Aggregation | `COUNT`, `SUM`, `AVG`, `MIN`, `MAX` |
| Grouping | `GROUP BY`, `HAVING` |
| JOINs | `INNER JOIN`, `LEFT JOIN` |
| Subqueries | Scalar and correlated patterns |
| Conditional logic | `CASE` expressions |
| Analytic reasoning | Ranking, ordering, time-based comparisons |

Representative problems:

- [Rising Temperature](0197-rising-temperature)
- [Managers With at Least 5 Direct Reports](0570-managers-with-at-least-5-direct-reports)
- [Employee Bonus](0577-employee-bonus)
- [Find Customer Referee](0584-find-customer-referee)
- [Big Countries](0595-big-countries)
- [Triangle Judgement](0610-triangle-judgement)
- [Consecutive Numbers](0180-consecutive-numbers)
- [Confirmation Rate](1934-confirmation-rate)
- [Count Salary Categories](1907-count-salary-categories)

---

# Repository Structure

Every solved problem is kept in its own directory.

~~~text
LEETCODE/
│
├── 0001-two-sum/
│   ├── 0001-two-sum.py
│   └── README.md
│
├── 0002-add-two-numbers/
├── 0006-zigzag-conversion/
├── 0007-reverse-integer/
├── ...
├── 0180-consecutive-numbers/
├── 0197-rising-temperature/
├── 0570-managers-with-at-least-5-direct-reports/
├── ...
├── 1934-confirmation-rate/
├── 2356-number-of-unique-subjects-taught-by-each-teacher/
│
├── stats.json
└── README.md
~~~

A typical problem folder contains:

~~~text
problem-id-problem-name/
├── problem-id-problem-name.py
│   or
├── problem-id-problem-name.sql
└── README.md
~~~

---

# Solution Philosophy

This repository is intended to be a **problem-solving record**, not a dump of accepted code.

~~~text
Problem
  ↓
Understand constraints
  ↓
Identify the pattern
  ↓
Write the simplest correct approach
  ↓
Analyze time and space
  ↓
Look for optimization
  ↓
Implement cleanly
  ↓
Test edge cases
  ↓
Record the solution
~~~

Every solution should be considered through three lenses:

### Correctness
Handle the full problem specification and edge cases.

### Complexity
Evaluate time complexity, space complexity, constraints, and practical trade-offs.

### Pattern recognition
The goal is to recognize reusable structures rather than memorize isolated answers.

---

# How to Use

## Study Mode

Choose a pattern and solve related problems together.

~~~text
Two Pointers
    ↓
Container With Most Water
    ↓
3Sum
    ↓
3Sum Closest
    ↓
4Sum
~~~

## Interview Mode

1. Read the problem.
2. Hide the solution.
3. Derive the approach independently.
4. Implement it.
5. Compare with the repository solution.
6. Check complexity and edge cases.
7. Re-solve later without looking.

## SQL Mode

~~~text
Requirement
    ↓
Identify tables
    ↓
Identify relationships
    ↓
Choose JOIN / subquery
    ↓
Filter
    ↓
Aggregate
    ↓
Order / window / condition
    ↓
Final result
~~~

---

# Running Python Solutions

Python is used for the algorithmic solutions.

~~~bash
cd 0001-two-sum
python 0001-two-sum.py
~~~

On systems where Python 3 is invoked explicitly:

~~~bash
python3 0001-two-sum.py
~~~

Some solutions follow LeetCode's function-signature format and may require a small local test harness for standalone execution.

---

# Running SQL Solutions

SQL solutions are written for LeetCode's database environment.

~~~text
1. Open the corresponding LeetCode problem.
2. Review the provided schema.
3. Paste the query.
4. Execute against the online judge.
5. Compare the result with the expected output.
~~~

The queries can also be adapted for local database engines where syntax is compatible.

---

# Complexity Guide

| Complexity | Typical use |
|---|---|
| O(1) | Constant-time lookup or work |
| O(log n) | Binary-search-style reduction |
| O(n) | Single-pass traversal |
| O(n log n) | Comparison sorting |
| O(n²) | Pairwise search under suitable constraints |
| O(2ⁿ) / O(n!) | Exhaustive state-space exploration |

The objective is not to minimize Big-O notation at any cost. A strong interview solution balances **correctness, constraints, clarity, maintainability, and performance**.

---

# Learning Roadmap

~~~mermaid
flowchart LR
    A["Arrays"] --> B["Hashing"]
    B --> C["Two Pointers"]
    C --> D["Strings"]
    D --> E["Linked Lists"]
    E --> F["Recursion"]
    F --> G["Backtracking"]
    G --> H["Greedy"]
    H --> I["Dynamic Programming"]
    I --> J["Advanced Patterns"]
    C --> K["SQL Fundamentals"]
    K --> L["JOINs"]
    L --> M["Aggregation"]
    M --> N["Subqueries"]
    N --> O["Advanced SQL"]
~~~

### Suggested progression

**Foundation**

Arrays → Hashing → Strings → Basic SQL

**Core interview patterns**

Two Pointers → Sorting → Linked Lists → JOINs → Aggregation

**Advanced reasoning**

Recursion → Backtracking → Dynamic Programming → Advanced SQL

---

# Roadmap

This repository is intended to grow from a collection of solutions into a structured interview-preparation knowledge base.

- Expand coverage across major DSA patterns.
- Increase the Medium and Hard problem set.
- Add more SQL problems covering advanced analytics.
- Standardize per-problem README structure.
- Improve edge-case and trade-off explanations.
- Add language variants where useful.
- Track progress automatically through repository statistics.
- Introduce lightweight automated validation for solution files.

---

# Design Principles

| Principle | Meaning |
|---|---|
| **Clarity** | Understandable code before clever code |
| **Efficiency** | Respect constraints and avoid unnecessary work |
| **Consistency** | Similar patterns documented in similar ways |
| **Depth** | Understand why an approach works |
| **Repetition** | Revisit patterns until recognition becomes natural |
| **Incremental growth** | Improve one problem at a time |

---

# Useful Resources

- [LeetCode](https://leetcode.com/) — Problem platform and judge
- [NeetCode](https://neetcode.io/) — Pattern-based interview preparation
- [GeeksforGeeks](https://www.geeksforgeeks.org/) — Algorithms and data structures reference
- [Visualgo](https://visualgo.net/) — Algorithm visualizations
- [Big-O Cheat Sheet](https://www.bigocheatsheet.com/) — Complexity reference

---

# Contribution

Useful contributions include:

- Correctness fixes
- Complexity improvements
- Cleaner explanations
- Additional language implementations
- Stronger edge-case coverage
- Documentation improvements

For substantial changes, open an issue or pull request with a clear explanation of the proposed improvement.

---

# License

This repository is licensed under the MIT License.

---

# Author

<p align="center">
  <strong>Ritesh Kumar</strong><br/>
  Computer Science Engineering
</p>

<p align="center">
  <a href="https://github.com/RITESH2127">GitHub</a>
  ·
  <a href="https://leetcode.com/RITESH2127/">LeetCode</a>
  ·
  <a href="https://github.com/RITESH2127/LEETCODE">Repository</a>
</p>

---

<p align="center">
  <sub>One problem at a time. One pattern at a time. Better problem solving over time.</sub>
</p>
