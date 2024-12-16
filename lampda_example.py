# Example of lambda in map()
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # Output: [1, 4, 9, 16, 25]

# Example in sorted()
points = [(2, 3), (1, 4), (3, 2)]
sorted_points = sorted(points, key=lambda point: point[1])
print(sorted_points)  # Output: [(3, 2), (2, 3), (1, 4)]
