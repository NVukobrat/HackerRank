def child_len(first, second):
    first_map = {}
    second_map = {}

    # Create maps
    for i, j in zip(first, second):
        if i not in first_map:
            first_map[i] = 0
        first_map[i] += 1

        if j not in second_map:
            second_map[j] = 0
        second_map[j] += 1

    # Pick relevant keys and values
    first_keys = list(first_map.keys())
    second_keys = list(second_map.keys())

    first_values = list(first_map.values())
    second_values = list(second_map.values())

    first_relevant_values = []
    second_relevant_values = []
    for i in range(len(first_keys)):
        for j in range(len(second_keys)):
            if first_keys[i] == second_keys[j]:
                first_relevant_values.append(first_values[i])
                second_relevant_values.append(second_values[j])
                break

    # Determine max child len
    max_child_len = 0
    for i, j in zip(first_relevant_values, second_relevant_values):
        max_child_len += min(i, j)

    print(max_child_len)


if __name__ == '__main__':
    first = input()
    second = input()

    child_len(first, second)
