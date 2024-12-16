# Python program to demonstrate List, Tuple, Set, and Dictionary


# List: Ordered, mutable, allows duplicates
print("1. List:")
my_list = [1, 2, 3, 4, 2]
print("   - List elements:", my_list)
my_list.append(5)  # Adding an element
print("   - After appending 5:", my_list)

# Tuple: Ordered, immutable, allows duplicates
print("\n2. Tuple:")
my_tuple = (1, 2, 3, 4, 2)
print("   - Tuple elements:", my_tuple)
print("   - Accessing element at index 1:", my_tuple[1])

# Set: Unordered, mutable, no duplicates
print("\n3. Set:")
my_set = {1, 2, 3, 4, 2}
print("   - Set elements (no duplicates):", my_set)
my_set.add(5)  # Adding an element
print("   - After adding 5:", my_set)

# Dictionary: Key-value pairs, mutable, no duplicate keys
print("\n4. Dictionary:")
my_dict = {"a": 1, "b": 2, "c": 3}
print("   - Dictionary elements:", my_dict)
my_dict["d"] = 4  # Adding a new key-value pair
print("   - After adding key 'd' with value 4:", my_dict)
print("   - Accessing value for key 'b':", my_dict["b"])

