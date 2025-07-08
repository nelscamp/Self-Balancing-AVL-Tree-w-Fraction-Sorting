# AVL Tree Performance Analysis

## Method Time Complexity

### O(log n) Operations
**`insert_element()` and `remove_element()`**: 
- Tree traversal to find insertion/removal position: O(log n)
- Node creation, height updates, balance factor calculations: O(1)
- Rotation operations (left/right rotations): O(1)
- **Overall**: O(log n) due to guaranteed balanced tree structure

The AVL property ensures the tree height never exceeds log₂(n), making all search-based operations logarithmic.

### O(n) Operations
**`to_list()`, `in_order()`, `pre_order()`, `post_order()`**:
- Must visit every node exactly once
- Each recursive call performs O(1) work
- **Overall**: O(n) for complete tree traversal

### O(1) Operations
**`get_height()`**: Returns stored height value from root node

## Sorting Performance Analysis

**Time Complexity**: O(n log n)

**Analysis**: 
- Insert n elements: n × O(log n) = O(n log n)
- Extract sorted sequence via `to_list()`: O(n)
- **Total**: O(n log n) + O(n) = O(n log n)

**Applicability**: Works with any comparable data type that implements `<`, `>`, and `==` operators. Successfully tested with:
- Integers and floating-point numbers
- Custom Fraction objects with cross-multiplication comparisons
- Any object with properly defined comparison operators

## Fraction Class Integration

### Comparison Strategy
Uses **cross-multiplication** to avoid floating-point precision errors:
```python
def __lt__(self, other):
    return self.__n * other.__d < other.__n * self.__d
```

This approach maintains integer arithmetic throughout comparison operations, ensuring exact results.

### Automatic Reduction
Fractions are automatically reduced to lowest terms using the Euclidean algorithm for GCD calculation, ensuring consistent comparisons and canonical representation.

## Testing Methodology

### Comprehensive Tree Testing
**Structure Testing**: Built trees up to 4 levels with systematic insertion/removal patterns
**Rotation Testing**: Verified all rotation cases (LL, LR, RL, RR) through strategic element sequences
**Balance Verification**: Confirmed AVL property maintenance after each operation via traversal validation

### Edge Case Coverage
- Empty tree operations
- Single-element scenarios  
- Duplicate insertion handling (ValueError verification)
- Non-existent element removal (ValueError verification)
- Complete tree emptying through systematic removal

### Fraction Testing
**Comparison Validation**: Tested all comparison operators (`<`, `>`, `==`) with various fraction combinations
**Sorting Verification**: Confirmed unsorted fraction arrays become properly ordered after BST insertion and extraction
**Edge Cases**: Verified proper handling of equivalent fractions with different representations

### Validation Approach
Hand-calculated expected tree structures and traversal sequences for comparison with actual output. Multi-level testing with different insertion/removal orders ensured robustness across various tree configurations.