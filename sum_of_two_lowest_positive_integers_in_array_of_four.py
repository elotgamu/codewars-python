# def sum_two_smallest_numbers(numbers):
#     # your code here
#     if numbers is not None:
#         lowest = numbers[0]
#         lowest_index = 0
#         second_lower = lowest
#         second_array = []

#         for index, number in enumerate(numbers):
#             if lowest >= number:
#                 lowest = number
#                 lowest_index = index

#         for index, number in enumerate(numbers):
#             if lowest_index != index:
#                 second_array.append(number)

#         second_lower = second_array[0]

#         for element in second_array:
#             if second_lower >= element:
#                 second_lower = element

#         return lowest + second_lower


def sum_two_smallest_numbers(numbers):
    # The efficient way using sort (asc) and the sum the first two values
    print('The sum of the two smallest numbers is ', sum(sorted(numbers)[:2]))
    return sum(sorted(numbers)[:2])


sum_two_smallest_numbers([5, 8, 12, 18, 22])
sum_two_smallest_numbers([7, 15, 12, 18, 22])
sum_two_smallest_numbers([25, 42, 12, 18, 22])
