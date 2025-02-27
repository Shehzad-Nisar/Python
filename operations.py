set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

union_result = set_a.union(set_b)
print("Union:", union_result)

intersection_result = set_a.intersection(set_b)
print("Intersection:", intersection_result)

difference_a_b = set_a.difference(set_b)
print("Difference (A - B):", difference_a_b)

difference_b_a = set_b.difference(set_a)
print("Difference (B - A):", difference_b_a)

symmetric_difference_result = set_a.symmetric_difference(set_b)
print("Symmetric Difference:", symmetric_difference_result)
