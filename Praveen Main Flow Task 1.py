# Create a list
my_list = [1, 2, 3]
print("Original List:", my_list)

# Add an element to the list
my_list.append(4)
print("List after adding an element:", my_list)

# Remove an element from the list
my_list.remove(2)
print("List after removing an element:", my_list)

# Modify an element in the list
my_list[0] = 10
print("List after modifying an element:", my_list)

# Create a dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}
print("\nOriginal Dictionary:", my_dict)

# Add a key-value pair to the dictionary
my_dict['d'] = 4
print("Dictionary after adding a key-value pair:", my_dict)

# Remove a key-value pair from the dictionary
del(my_dict['b'])
print("Dictionary after removing a key-value pair:", my_dict)

# Modify a value in the dictionary
my_dict['a'] = 10
print("Dictionary after modifying a value:", my_dict)

# Create a set
my_set = {1, 2, 3}
print("\nOriginal Set:", my_set)

# Add an element to the set
my_set.add(4)
print("Set after adding an element:", my_set)

# Remove an element from the set
my_set.remove(2)
print("Set after removing an element:", my_set)

# Try to add a duplicate element to the set
my_set.add(3)
print("Set after trying to add a duplicate element:", my_set)
