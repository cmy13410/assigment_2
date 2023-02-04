#  Assignment 2 - Camille Young
#  2/4/2023

# Question 1 - Prints Star Pattern
print("\nQuestion 1:")
for i in range(0, 5):  # Prints star pattern in ascending direction
    print('*' * i)

for i in range(5, 0, -1):  # Prints star pattern in descending direction
    print('*' * i)
print()  # Prints for spacing

# Question 2 - Prints at Odd Indexes
print("\nQuestion 2:")
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
for i in range(1, len(my_list), 2):
    print("Index: {} Value: {}".format(i, my_list[i]))
print()  # Prints for spacing

# Question 3 - Print out element types
print("\nQuestion 3:")
x = [23, 'Python', 23.98]  # Example data
type_of_elements = []  # Empty list for types of variables to be appended to
for i in x:  # Loop appends variable types to type_of_elements
    type_of_elements.append(type(i))

# Prints output
print(x)
print(type_of_elements)

print()  # Prints for spacing

# Question 4 - Prints out unique items from a different list
print("\nQuestion 4:")
sample_list = [1, 2, 3, 3, 3, 3, 4, 5]
unique_list = []  # Creates empty list to be appended to

for i in sample_list:  # Iterates through sample list and appends only unqiue values
    if i not in unique_list:
        unique_list.append(i)

print("Sample List: {}".format(sample_list))
print("Unique List: {}".format(unique_list))

print()  # Prints for spacing

# Question 5 - Calculate the number of upper case and lower-case
print("\nQuestion 5:")
input_string = 'The quick Brow Fox'
lower_case_count = 0
upper_case_count = 0
for i in input_string:  # Loops through input_string and has logic to increment counts if upper or lowercase
    if i.isupper():
        upper_case_count += 1
    elif i.islower():
        lower_case_count += 1

# Prints output
print("No. of Upper-case characters: {}".format(upper_case_count))
print("No. of Lower-case Characters: {}".format(lower_case_count))
