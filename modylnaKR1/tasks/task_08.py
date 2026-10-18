
def compare_tags(first: list, second: list) -> dict:
    first_set = {str(tag).strip().lower() for tag in first}
    second_set = {str(tag).strip().lower() for tag in second}

    only_first = sorted(first_set - second_set)
    only_second = sorted(second_set - first_set)
    both = sorted(first_set & second_set)

    union = first_set | second_set

    if union:
        similarity = len(both) / len(union)
    else:
        similarity = 0.0

    return {
        "only_first": only_first,
        "only_second": only_second,
        "both": both,
        "similarity": similarity
    }
