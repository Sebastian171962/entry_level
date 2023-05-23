def find_pairs(numbers, target_sum):
    pairs = []
    complements = set()
    
    for num in numbers:
        complement = target_sum - num
        if complement in complements:
            pairs.append((num, complement))
        complements.add(num)
    
    return pairs

numbers = [1, 9, 5, 0, 20, -4, 12, 16, 7]
target_sum = 12

pairs = find_pairs(numbers, target_sum)

print("Pairs that sum to", target_sum, ":")
for pair in pairs:
    print(pair[0], "+", pair[1], "=", target_sum)
