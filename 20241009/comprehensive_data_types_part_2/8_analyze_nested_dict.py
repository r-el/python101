def analyze_nested_dict(nested_dict):
    max_keys = []
    min_keys = []
    overall_max_key = None
    overall_min_key = None
    overall_max_value = float('-inf')
    overall_min_value = float('inf')
    total_sum = 0

    for sub_dict_key, sub_dict in nested_dict.items():
        max_key = max(sub_dict, key=sub_dict.get)
        min_key = min(sub_dict, key=sub_dict.get)
        max_value = sub_dict[max_key]
        min_value = sub_dict[min_key]

        max_keys.append(max_key)
        min_keys.append(min_key)

        if max_value > overall_max_value:
            overall_max_value = max_value
            overall_max_key = max_key

        if min_value < overall_min_value:
            overall_min_value = min_value
            overall_min_key = min_key

        total_sum += sum(sub_dict.values())

    print(f"Keys of max values: {', '.join(max_keys)}")
    print(f"Keys of min values: {', '.join(min_keys)}")
    print(f"Key of overall max value: {overall_max_key}")
    print(f"Key of overall min value: {overall_min_key}")
    print(f"Sum of all values: {total_sum}")

# Example usage
nested_dict = {
    "first_dict": {"a": 1, "b": 10},
    "second_dict": {"c": 1000, "d": -500, "e": 0},
    "third_dict": {"f": 200}
}

analyze_nested_dict(nested_dict)