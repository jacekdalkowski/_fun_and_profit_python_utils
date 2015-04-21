def gen_combinations(n, c):
    combination = []
    for i in range(0, c):
        combination += [i]

    yield list(combination)

    while True:
        #move last one forward
        for i in range(combination[c-1] + 1, n):
            combination[c-1] = i
            yield list(combination)

        moveCandidate = 0
        goBackSeq = range(0,c-1)
        goBackSeq.reverse();
        for i in goBackSeq:
            if combination[i+1] - combination[i] > 1:
                moveCandidate = i
                break

        combination[moveCandidate] = combination[moveCandidate] + 1
        for i in range(moveCandidate+1, c):
            combination[i] = combination[i-1] + 1

        yield list(combination)

        if combination[0] == n-c:
            return

combinations = list(gen_combinations(5, 3))
print combinations