def printer(n):
    print("START")

    for i in n:
        print(i)

    print("END")


def printer2(n):
    maxx = 0
    for i in range(9):
        for j in range(9):
            k = len(n[i][j])
            if k > maxx:
                maxx = k
    print(maxx, "is max")
    for i in range(9):
        for j in range(9):
            k = len(n[i][j])
            if k < maxx:
                for l in range(maxx - k):
                    n[i][j].append(0)
    print("START")

    for i in n:
        print(i)

    print("END")


def printer3(n):
    for i in range(9):
        for j in range(9):
            if len(n[i][j]) == 1:
                n[i][j] = n[i][j][0]
            else:
                n[i][j] = 0
    print("START")

    for i in n:
        print(i)

    print("END")


#sample = {1, 2, 3, 4, 5, 6, 7, 8, 9}

# sample[0] = 0
# print(sample)
# help(sample)

gen = [
    [[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9],
     [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9],
     [1, 2, 3, 4, 5, 6, 7, 8, 9]],
    [[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9],
     [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9],
     [1, 2, 3, 4, 5, 6, 7, 8, 9]],
    [[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9],
     [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9],
     [1, 2, 3, 4, 5, 6, 7, 8, 9]],
    [[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9],
     [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9],
     [1, 2, 3, 4, 5, 6, 7, 8, 9]],
    [[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9],
     [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9],
     [1, 2, 3, 4, 5, 6, 7, 8, 9]],
    [[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9],
     [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9],
     [1, 2, 3, 4, 5, 6, 7, 8, 9]],
    [[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9],
     [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9],
     [1, 2, 3, 4, 5, 6, 7, 8, 9]],
    [[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9],
     [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9],
     [1, 2, 3, 4, 5, 6, 7, 8, 9]],
    [[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9],
     [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9],
     [1, 2, 3, 4, 5, 6, 7, 8, 9]]]

puzzle = [
    4, 0, 0, 0, 0, 9, 6, 0, 0,
    0, 0, 0, 4, 6, 0, 0, 3, 0,
    0, 6, 7, 3, 0, 0, 0, 1, 0,
    3, 0, 9, 0, 7, 0, 0, 0, 0,
    0, 4, 8, 0, 0, 0, 7, 5, 0,
    0, 0, 0, 0, 4, 0, 9, 0, 3,
    0, 2, 0, 0, 0, 7, 1, 6, 0,
    0, 7, 0, 0, 1, 4, 0, 0, 0,
    0, 0, 4, 6, 0, 0, 0, 0, 8
]

puzzle = [
    2, 0, 0, 6, 0, 0, 0, 0, 0,
    0, 0, 0, 9, 4, 0, 0, 0, 6,
    0, 0, 0, 0, 2, 0, 0, 4, 0,
    5, 0, 0, 3, 0, 9, 1, 0, 0,
    0, 1, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 2, 8, 0, 5, 0, 0, 9,
    0, 0, 0, 0, 5, 0, 0, 2, 0,
    7, 0, 0, 0, 9, 8, 0, 6, 0,
    0, 0, 0, 0, 0, 4, 0, 0, 7]

puzzle = [
    2, 0, 0, 6, 0, 3, 7, 0, 0,
    3, 0, 0, 9, 4, 1, 0, 0, 6,
    1, 0, 0, 0, 2, 7, 9, 4, 0,
    5, 0, 0, 3, 0, 9, 1, 0, 0,
    0, 1, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 2, 8, 0, 5, 0, 0, 9,
    0, 0, 0, 0, 5, 0, 0, 2, 0,
    7, 0, 0, 2, 9, 8, 0, 6, 0,
    0, 0, 0, 1, 0, 4, 0, 0, 7
]


def block_wise(matrix):
    block = [[], [], [], [], [], [], [], [], []]
    for i in range(9):
        for j in range(9):
            k = j // 3 + 3 * (i // 3)

            block[k].append(matrix[i][j])
    return block


def transpose(matrix):
    h = []
    t = []

    for i in range(9):
        for j in range(9):
            h.append(matrix[j][i])
        t.append(h)
        h = []
    return t


def nines(list1):
    nines_h = []
    nine = []
    n = 0
    for i in list1:
        n += 1
        nine.append(i)

        if n % 9 == 0:
            nines_h.append(nine)
            nine = []

    return nines_h


def line_remover(n, l, gen):
    for i in range(9):
        if len(gen[i]) > 1:
            try:
                gen[i].remove(n)
            except:
                pass
                # print(gen[l][i], "remove.(", n, ")")
    return gen


def all_h_check(puzzle, gen):
    for l in range(9):
        for j in range(9):
            n = puzzle[l][j]
            if n != 0:
                gen[l] = line_remover(n, l, gen[l])

    return gen


def new_puzzle(puzzle, gen):
    newpuzzle = []
    for i in range(9):
        row = []
        for j in range(9):
            if puzzle[i][j] == 0 and len(gen[i][j]) == 1:
                row.append(gen1[i][j][0])
            else:
                row.append(0)
        newpuzzle.append(row)
    return newpuzzle


def unique_in_list(check):
    agregator = []
    for i in check:
        for j in i:
            agregator.append(j)
    # print("un ", agregator)
    n = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    m = 0
    unique = []
    for i in n:
        rep = agregator.count(i)
        if rep == 1:
            m += 1
            position = agregator.index(i)
            unique.append([i, position])
    # print(unique)
    # print(m, "block uniques")
    return [m, unique]


def unique_in_block(gen):
    gen = block_wise(gen)

    for i in range(9):
        check = []
        widths = []
        pos = 0
        for j in range(9):
            pos += len(gen[i][j])
            widths.append(pos)
            check.append(gen[i][j])
        # print(widths)
        locations = unique_in_list(check)

        if locations[0] != 0:
            # print(len(locations[1]))
            for k in locations[1]:
                # k[0] is number
                # k[1] is its position

                for x in range(9):
                    if widths[x] >= k[1] + 1:
                        # print(x, end=" ")
                        break

                gen[i][x] = [k[0]]
            # print()
    # print()

    return block_wise(gen)


def check(matrix):
    ans = 0
    for i in range(9):
        for j in range(9):
            for k in matrix[i][j]:
                ans += 1
    ans = ans - 81

    return ans


def new_puzzle(puzzle, gen):
    for i in range(9):
        for j in range(9):
            if puzzle[i][j] == 0 and len(gen[i][j]) == 1:
                puzzle[i][j] = gen[i][j][0]
            else:
                puzzle[i][j] = 0
    return puzzle


def new_puzzle2(puzzle, gen):
    for i in range(9):
        for j in range(9):
            if puzzle[i][j] == 0 and len(gen[i][j]) == 1:
                puzzle[i][j] = gen[i][j][0]
            else:
                pass
    return puzzle


def answer_checker(n):
    for i in range(9):
        row = []
        for j in range(9):
            row.append(n[i][0])
            for k in range(9):
                if row.count(k+1) != 1:
                    print("H-line", i+1, "value", k+1)
    n = transpose(n)
    for i in range(9):
        row = []
        for j in range(9):
            row.append(n[i][0])
            for k in range(9):
                if row.count(k + 1) != 1:
                    print("V-line", i + 1, "value", k + 1)


if __name__ == "__main__":

    puzzle = nines(puzzle)
    for i in range(9):
        for j in range(9):
            if puzzle[i][j] != 0:
                gen[i][j] = [puzzle[i][j]]
    gen1 = gen

    for i in range(100):

        guesses = check(gen1)
        gen1 = all_h_check(puzzle, gen1)
        gen1 = transpose(all_h_check(transpose(puzzle), transpose(gen1)))
        gen1 = block_wise(all_h_check(block_wise(puzzle), block_wise(gen1)))
        gen1 = unique_in_block(gen1)
        puzzle = new_puzzle(puzzle, gen1)
        if guesses == check(gen1):
            print(guesses, "guesses remaining")
            print(i + 1, "iterations done")
            break

    # printer2(block_wise(gen1))
    printer3(gen1)
    #answer_checker(gen1)
    # printer(puzzle)
