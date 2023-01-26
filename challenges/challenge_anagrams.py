def merge_sort(list, start=0, end=None):
    if end is None:
        end = len(list)
    if (end - start) > 1:
        mid = (end + start) // 2
        merge_sort(list, start, mid)
        merge_sort(list, mid, end)
        merge(list, start, mid, end)


def merge(list, start, mid, end):
    left = list[start:mid]
    right = list[mid:end]

    left_index, right_index = 0, 0

    for general_index in range(start, end):
        if left_index >= len(left):
            list[general_index] = right[right_index]
            right_index = right_index + 1
        elif right_index >= len(right):
            list[general_index] = left[left_index]
            left_index = left_index + 1
        elif left[left_index] < right[right_index]:
            list[general_index] = left[left_index]
            left_index = left_index + 1
        else:
            list[general_index] = right[right_index]
            right_index = right_index + 1


def is_anagram(first_string, second_string):
    first_list = [letter for letter in first_string.lower()]
    second_list = [letter for letter in second_string.lower()]

    merge_sort(first_list)
    merge_sort(second_list)

    first_string = "".join(first_list)
    second_string = "".join(second_list)

    if (len(first_string) != len(second_string)):
        return (first_string, second_string, False)

    if (len(first_string) == 0 or len(first_string) == 0):
        return (first_string, second_string, False)

    if (first_string != second_string):
        return (first_string, second_string, False)

    if (first_string == second_string):
        return (first_string, second_string, True)
