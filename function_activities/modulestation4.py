def min_max(numbers):
    if not numbers:
        return None, None
    return min(numbers), max(numbers)

def min_max_sorted(numbers):
    if not numbers:
        return None, None
    sorted_numbers = sorted(numbers)
    return sorted_numbers[0], sorted_numbers[-1]

def swap_first_last(tpl):
    if not tpl:
        return tpl
    lst = list(tpl)
    lst[0], lst[-1] = lst[-1], lst[0]
    return tuple(lst)

def tuple_to_sorted_list(tpl):
    return sorted(list(tpl))