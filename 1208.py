t = 10
for test_case in range(1, t + 1):
    n = int(input())

    box = list(map(int, input().split()))

    for i in range(n):
        if max(box) - min(box) == 1 or max(box) - min(box) == 0:
            break
        else:
            box[box.index(min(box))] += 1
            box[box.index(max(box))] -= 1

    print("#%d %d" % (test_case, max(box) - min(box)))