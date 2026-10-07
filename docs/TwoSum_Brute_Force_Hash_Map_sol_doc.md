# Intuition

My first instinct was to compare every number with every other number and check whether their sum equals the target.

This works because there is guaranteed to be exactly one valid pair, but it requires checking many combinations. This leads to an **O(n²)** time complexity.

A better way to think about the problem is: for each number, ask **"What number do I need to reach the target?"**

That number is the **complement**:

```python
complement = target - num
```

If I've already seen that complement, I immediately have the answer.

# Approach

## 1st Solution: Brute Force

Loop through every element and compare it with every other element.

```python
for index in range(len(nums)):
    for subindex in range(len(nums)):
        if index != subindex:
            if nums[index] + nums[subindex] == target:
                return [index, subindex]
```

The `index != subindex` check prevents using the same element twice.

This solution is straightforward, but the nested loops mean that the number of comparisons grows quadratically with the size of the input.

## 2nd Solution: Hash Map

Use a dictionary called `seen` to store numbers we've already visited and their indices.

For each number:

1. Calculate the complement needed to reach `target`.
2. Check whether that complement is already in `seen`.
3. If it is, return the stored index and the current index.
4. Otherwise, store the current number and its index.

For example:

```python
nums = [2, 7, 11, 15]
target = 9
```

When we reach `7`:

```python
complement = 9 - 7
# complement = 2
```

We've already seen `2`, so we can immediately return:

```python
[0, 1]
```

This avoids checking every possible pair.

# Complexity

## 1st Solution: Brute Force

* **Time complexity:** \(O(n^2)\)
* **Space complexity:** \(O(1)\)

## 2nd Solution: Hash Map

* **Time complexity:** \(O(n)\)
* **Space complexity:** \(O(n)\)

The dictionary gives us **O(1) average-time lookup**, allowing us to solve the problem with a single pass through the array.

# Code

## 1st Solution: Brute Force

```python
class Solution(object):
    def twoSum(self, nums, target):
        indexes = []

        for index in range(len(nums)):
            for subindex in range(len(nums)):
                if index != subindex:
                    current_element = nums[index]
                    next_element = nums[subindex]
                    result = current_element + next_element

                    if result == target:
                        indexes.append(index)
                        indexes.append(subindex)
                        return indexes
```

## 2nd Solution: Hash Map

```python
class Solution(object):
    def twoSum(self, nums, target):
        seen = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in seen:
                return [seen[complement], i]

            seen[num] = i
```

The **second solution is the preferred solution** because it improves the time complexity from **O(n²)** to **O(n)** by trading some additional memory for faster lookups.

