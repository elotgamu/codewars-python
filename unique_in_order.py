# Implement the function unique_in_order which takes as argument a sequence
# and returns a list of items without any elements with the same
# value next to each other and preserving the original order of elements.

# For example:

# unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
# unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
# unique_in_order([1,2,2,3,3])       == [1,2,3]


def unique_in_order(iterable):
    print("Parameters has " + str(len(iterable)) + " elements")
    iterable_list = list(iterable)
    print(iterable_list)
    new_list = list()
    # unique = set()
    # unique_add = unique.add
    # new_list = [x for x in iterable_list if not (x in unique or unique_add(x))] # noqa
    # print(new_list)
    # return new_list
    for element in range(len(iterable_list)):
        if element == 0:
            new_list.append(iterable_list[element])
        else:
            if (element + 1) > len(iterable_list):
                break

            if (iterable_list[element] != iterable_list[element - 1]):
                new_list.append(iterable_list[element])

    print(new_list)
    return new_list


def unique_order_better(iterable):
    result = []
    prev = None
    for char in iterable[0:]:
        if char != prev:
            result.append(char)
            prev = char
    return result


unique_in_order('AAAABBBCCDAABBB')
unique_in_order('ABBCcAD')
unique_in_order([1, 2, 2, 3, 3])
unique_in_order('ADD')
unique_in_order('AAD')
