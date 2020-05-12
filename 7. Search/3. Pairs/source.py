count = 0


def number_of_pairs(arr, n, k):
    arr = sorted(arr, reverse=True)
    left = 0
    right = n
    for ref_elem in arr:
        split_count(ref_elem, arr, k, left, right)
        left += 1


def split_count(ref_elem, arr, k, left, right):
    if right <= left:
        return

    middle_index = (left + right) // 2
    score = ref_elem - arr[middle_index]
    if score == k:
        global count
        count += 1
    elif score > k:
        split_count(ref_elem, arr, k, left, middle_index)
    elif score < k:
        split_count(ref_elem, arr, k, middle_index, right)

    split_count(ref_elem, arr, k, left, middle_index)
    split_count(ref_elem, arr, k, middle_index, right)


if __name__ == '__main__':
    n, k = input().split(" ")[0:2]
    arr = input()
    arr = list(map(int, arr.split(" ")[:-2]))

    number_of_pairs(arr, int(n), int(k))

    print()
