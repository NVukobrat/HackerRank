def child_len(first, second):
    """
    Dynamic Programming approach.
    """
    size = len(first)
    matrix = [[0] * (size + 1) for i in range(size + 1)]
    for i in range(1, size + 1):
        for j in range(1, size + 1):
            if first[i - 1] is not second[j - 1]:
                matrix[i][j] = max(matrix[i - 1][j], matrix[i][j - 1])
            else:
                matrix[i][j] = (matrix[i - 1][j - 1]) + 1

    print(matrix[i][j])

if __name__ == '__main__':
    first = input()
    second = input()

    child_len(first, second)



def child_len_2_attempt(first, second):
    first_clear = ""
    second_cpy = (second + '.')[:-1]
    second_i = []
    for i in range(len(first)):
        for j in range(len(second_cpy)):
            if first[i] is second_cpy[j]:
                first_clear += first[i]
                second_i.append(j)
                second_cpy = second_cpy[:j] + "-" + second_cpy[(j + 1):]
                break

    second_clear = ""
    second_i.sort()
    for i in second_i:
        second_clear += second[i]

    first_len = determine_child_len(first_clear, second_clear)
    second_len = determine_child_len(second_clear, first_clear)

    print(max(first_len, second_len))


def determine_child_len(first, second):
    offset = 0
    child_len = 0
    for i in range(len(first)):
        for j in range(offset, len(second)):
            if first[i] is second[j]:
                child_len += 1
                offset = j + 1

    return child_len


def child_len_1_attempt(first, second):
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
