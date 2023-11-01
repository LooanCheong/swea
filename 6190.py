t = int(input())

for test_case in range(1, t + 1):
    n = int(input())
    n_list = list(map(int, input().split()))
    mul_list = []

    for i in range(len(n_list)):
        for j in range(i + 1, len(n_list)):
            mul_list.append(n_list[i] * n_list[j])

    mul_list = sorted(mul_list, reverse = True)

    ans = -1

    for i in mul_list:
        check = 0

        if len(str(i)) == 1:
            continue

        for j in range(len(str(i)) - 1):
            if str(i)[j] > str(i)[j + 1]:
                check = 1
                break

        if check == 0:
            ans = i
            break

    print("#%d %d" % (test_case, ans))