t = int(input())

for test_case in range(1, t + 1):

    n, m, k = map(int, input().split())

    people = sorted(list(map(int, input().split())))

    can = True

    for i in range(n):
        made = people[i] // m * k - i - 1

        if made < 0:
            can = False
            break

    if can:
        print("#%d Possible" % test_case)

    else:
        print("#%d Impossible" % test_case)