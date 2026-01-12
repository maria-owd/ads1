"""Partition negatives before positives with minimal swaps.

Given a sequence of non-zero values (positive and negative), transform the sequence in such a
way that all negative values precede the positive ones, minimizing the number of swap
operations. The implementation below performs an in-place two-pointer partition which
achieves this with at most one swap per misplaced negative-positive pair.
"""


def partition_negatives(arr) -> int:
	left = 0
	right = len(arr) - 1
	swaps = 0

	while left < right:
		if arr[left] < 0:
			left += 1
			continue
		if arr[right] >= 0:
			right -= 1
			continue
		arr[left], arr[right] = arr[right], arr[left]
		swaps += 1
		left += 1
		right -= 1

	return swaps



arr = [2, -1, 4, -2, -5, 6]
a = arr.copy()
swaps = partition_negatives(a)
print(f"input:  {arr}\noutput: {a} (swaps={swaps})")

