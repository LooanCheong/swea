t = int(input())

for test_case in range(1, t + 1):
    mem = list(input())

    n_mem = ["0"] * len(mem)

    cnt = 0

    for i in range(len(mem)):
        if mem[i] != n_mem[i]:
            for j in range(i, len(mem)):
                n_mem[j] = mem[i]
            cnt += 1

    print("#%d %d" % (test_case, cnt))