sort_used = False


def quicksort_string(string):
    global sort_used
    sort_used = True
    quicksort_string_helper(string, 0, len(string) - 1)


def quicksort_string_helper(string, first, last):
    if first < last:
        splitpoint = partition_string(string, first, last)
        quicksort_string_helper(string, first, splitpoint - 1)
        quicksort_string_helper(string, splitpoint + 1, last)


def partition_string(string, first, last):
    pivot_value = string[first]
    left_mark = first + 1
    right_mark = last
    done = False
    while not done:
        while (left_mark <= right_mark) and (string[left_mark] <= pivot_value):
            left_mark += 1
        while (string[right_mark] >= pivot_value) and (right_mark >= left_mark):
            right_mark -= 1
        if right_mark < left_mark:
            done = True
        else:
            string[left_mark], string[right_mark] = \
                string[right_mark], string[left_mark]
    string[first], string[right_mark] = string[right_mark], string[first]
    return right_mark


def is_anagram(first_string, second_string, ignore_case=True):
    """Verifica se duas strings são anagramas."""
    global sort_used
    if sort_used:
        raise Exception("Não utilize o método padrão de ordenação.")
    if not first_string and not second_string:
        return ("", "", False)
    first_string = [
        char.lower() if ignore_case else char for char in first_string
    ]
    second_string = [
        char.lower() if ignore_case else char for char in second_string
    ]
    quicksort_string(first_string)
    quicksort_string(second_string)
    sort_used = False
    return (
        "".join(first_string),
        "".join(second_string),
        first_string == second_string
        )
