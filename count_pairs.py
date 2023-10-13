# Implementing the count_pairs function

def count_pairs(numbers, target):
	num_set = set()
	pair_count = 0
	
	for num in numbers:
		complement = target - num
		if complement in num_set:
			pair_count += 1
			# Remove the complement from set to ensure single use
			num_set.remove(complement)
		else:
			num_set.add(num)
			
	return pair_count

# Testing the function with a simple example
count_pairs([1, 2, 3, 4, 5], 6) # Should return 2 for pairs (1, 5) and (2, 4)

