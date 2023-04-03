def sum_of_squares(numbers):
    sum = 0
    for num in numbers:
        sum += num**2
    return sum

# Example usage
my_list = [1, 2, 3, 4, 5]
result = sum_of_squares(my_list)
print("Sum of squares:", result)
