from collections import defaultdict

def find_pairs(numbers, target_sum):
    pairs = []
    complements = defaultdict(int)
    
    for num in numbers:
        complement = target_sum - num
        if complements[complement] > 0:
            pairs.append((num, complement))
        complements[num] += 1
    
    return pairs
numbers = [1, 9, 5, 0, 20, -4, 12, 16, 7]
target_sum = 12

pairs = find_pairs(numbers, target_sum)

if pairs:
    print("Pairs that sum to", target_sum, ":")
    for pair in pairs:
        print(pair[0], "+", pair[1], "=", target_sum)
else:
    print("No pairs found that sum to", target_sum)
