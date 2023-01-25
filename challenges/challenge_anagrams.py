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
    if (len(first_list) != len(second_list)):
        return (first_string.lower(), second_string.lower(), False)
    if (len(first_list) == 0 or len(second_list) == 0):
        return (first_string.lower(), second_string.lower(), False)
    merge_sort(first_list)
    merge_sort(second_list)
    if ("".join(first_list) != "".join(second_list)):
        print(first_list, second_list)
        return (first_string.lower(), second_string.lower(), False)
    if ("".join(first_list) == "".join(second_list)):
        return (first_string.lower(), second_string.lower(), True)
