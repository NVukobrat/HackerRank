from collections import Counter


def reverse_shuffle_merge(s):
    left = Counter(s)
    need = {char: int(count / 2) for char, count in left.items()}
    shuffle = {char: int(count / 2) for char, count in left.items()}

    string = []
    for char in reversed(s):
        if need[char] > 0:
            while string and string[-1] > char and shuffle[string[-1]] > 0:
                removed = string.pop()
                need[removed] += 1
                shuffle[removed] -= 1
            string.append(char)
            need[char] -= 1
        else:
            shuffle[char] -= 1

    print(''.join(string))


if __name__ == '__main__':
    s = input()
    reverse_shuffle_merge(s)
