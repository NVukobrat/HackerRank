# Enter your code here. Read input from STDIN. Print output to STDOUT
def alternate(arr):
    if arr[0] == 'A':
        flag = True
    else:
        flag = False
    del_num = 0
    for c in arr[1:]:
        if flag and c == 'A':
            del_num += 1
            flag = True
        elif flag and c == 'B':
            flag = False
        elif not flag and c == 'A':
            flag = True
        elif not flag and c == 'B':
            del_num += 1
            flag = False
    print(del_num)


if __name__ == '__main__':
    line_num = int(input())

    for i in range(line_num):
        line = input()
        alternate(line)
