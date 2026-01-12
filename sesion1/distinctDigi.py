'''
Consider a number composed of 10 distinct digits, different from 9876543210. Determine the
number that follows it in the increasing sequence of all natural numbers containing 10 distinct
digits.
'''

def next_permutation(a: list) -> bool:
	# Modify list `a` in-place to the next lexicographic permutation.
	# Return True if next permutation exists, False if `a` is the last permutation.
	n = len(a)
	i = n - 2
	while i >= 0 and a[i] >= a[i + 1]:
		i -= 1
	if i == -1:
		return False
	j = n - 1
	while a[j] <= a[i]:
		j -= 1
	a[i], a[j] = a[j], a[i]
	# reverse suffix
	a[i+1:] = reversed(a[i+1:])
	return True


def find_next_number(s: str) -> str:
	s = s.strip()
	a = list(s)
	# iterate to next permutations until leading digit != '0'
	while next_permutation(a):
		if a[0] != '0':
			return ''.join(a)

	return 'error'


s = '8745091236'
print(s)
print(find_next_number(s))
