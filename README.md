# Self-Balancing AVL Tree with Fraction Sorting

An implementation of an AVL (Adelson-Velsky and Landis) tree with automatic balancing, featuring fraction arithmetic and comparison capabilities for precise rational number sorting.

## Overview

This project implements a self-balancing binary search tree that maintains O(log n) performance for insertion, deletion, and search operations. The AVL tree automatically rebalances through rotations whenever the balance factor of any node exceeds ±1. Additionally, it includes a comprehensive Fraction class demonstrating custom object sorting with exact arithmetic.

## Key Features

### AVL Tree Implementation
- **Automatic Balancing**: Maintains height-balanced tree through four rotation types
- **Recursive Design**: All operations implemented recursively for clarity and correctness
- **Height Tracking**: Each node maintains its height for efficient balance factor calculation
- **Multiple Traversals**: In-order, pre-order, and post-order tree traversal methods

### Fraction Class
- **Exact Arithmetic**: Integer-based operations avoid floating-point precision errors
- **Automatic Reduction**: Fractions stored in lowest terms using GCD algorithm
- **Comparison Operators**: Cross-multiplication-based comparisons for exact ordering
- **BST Integration**: Demonstrates custom object sorting capabilities

## Performance Characteristics

| Operation | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Insert | O(log n) | O(log n) recursion |
| Remove | O(log n) | O(log n) recursion |
| Search | O(log n) | O(log n) recursion |
| Traversal | O(n) | O(log n) recursion |
| Sort n items | O(n log n) | O(n) storage |

## Usage Examples

### Basic Tree Operations
```python
from Binary_Search_Tree import Binary_Search_Tree

bst = Binary_Search_Tree()

# Insert elements (automatic balancing)
for value in [10, 5, 15, 2, 7, 12, 20]:
    bst.insert_element(value)

print(bst.in_order())    # [ 2, 5, 7, 10, 12, 15, 20 ]
print(bst.pre_order())   # [ 10, 5, 2, 7, 15, 12, 20 ]
print(bst.post_order())  # [ 2, 7, 5, 12, 20, 15, 10 ]

# Remove elements (maintains balance)
bst.remove_element(5)
print(bst.in_order())    # [ 2, 7, 10, 12, 15, 20 ]

# Get sorted list
sorted_list = bst.to_list()  # [2, 7, 10, 12, 15, 20]
```

### Fraction Sorting
```python
from Binary_Search_Tree import Binary_Search_Tree
from Fraction import Fraction

bst = Binary_Search_Tree()
fractions = [
    Fraction(1, 2),   # 0.5
    Fraction(1, 3),   # 0.333...
    Fraction(2, 3),   # 0.666...
    Fraction(3, 4),   # 0.75
    Fraction(1, 4)    # 0.25
]

# Insert fractions
for frac in fractions:
    bst.insert_element(frac)

print("Original:", fractions)
print("Sorted:  ", bst.to_list())
# Sorted: [1/4, 1/3, 1/2, 2/3, 3/4]
```

## Implementation Details

### AVL Balancing Algorithm
The tree maintains balance through four rotation types:

**Single Rotations:**
- **Left Rotation**: Corrects right-heavy trees
- **Right Rotation**: Corrects left-heavy trees

**Double Rotations:**
- **Left-Right**: Left rotation on left child, then right rotation on root
- **Right-Left**: Right rotation on right child, then left rotation on root

### Balance Factor Calculation
```python
balance_factor = height(right_subtree) - height(left_subtree)
```
- **Balanced**: -1 ≤ balance_factor ≤ 1
- **Rebalancing required**: balance_factor = ±2

### Fraction Precision Strategy
Avoids floating-point errors through cross-multiplication:
```python
# Instead of: self.to_float() < other.to_float()
# Use: self.__n * other.__d < other.__n * self.__d
```

## Testing Strategy

### Comprehensive Test Coverage
- **Structural Testing**: Trees built to 4+ levels with systematic patterns
- **Rotation Verification**: All four rotation types triggered and validated
- **Edge Cases**: Empty trees, single nodes, duplicate handling
- **Integration Testing**: Fraction objects with tree operations

### Validation Methodology
- Hand-calculated expected tree structures for comparison
- Traversal sequence verification against known results
- Balance factor validation after each operation
- Comprehensive exception handling testing

## Technical Insights

This implementation demonstrates several important computer science concepts:

1. **Self-Balancing Trees**: How automatic rebalancing maintains optimal performance
2. **Recursive Algorithm Design**: Clean, readable implementations of complex tree operations
3. **Custom Object Comparison**: Enabling user-defined types to work with generic data structures
4. **Precision in Computation**: Avoiding floating-point errors through algorithmic design choices

The AVL tree provides guaranteed O(log n) performance for basic operations, making it ideal for applications requiring predictable performance with dynamic data sets.
