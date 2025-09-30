```markdown
# Fibonacci Sequence in Python

The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones.

## Python Example

```python
def fibonacci(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

# Print first 10 Fibonacci numbers
print(fibonacci(10))
```