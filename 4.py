if __name__ == '__main__':
    with open("4.in") as f:
        lines = f.readlines()
        random_order = lines[0].split(',')
        boards = [tuple(tuple(lines[i + j].split()) for j in range(5)) for i in range(2, len(lines), 6)]

    drawn = set()
    for random in random_order:
        drawn.add(random)
        for board in boards:
            if any(all(board[i][j] in drawn for j in range(5)) for i in range(5)) or any(
                    all(board[j][i] in drawn for j in range(5)) for i in range(5)):
                break
        else:
            continue

        print(int(random) * sum(int(elem) for line in board for elem in line if elem not in drawn))
        break

    good_boards = set(boards)
    drawn = set()
    for random in random_order:
        drawn.add(random)
        for board in boards:
            if (any(all(board[i][j] in drawn for j in range(5)) for i in range(5)) or any(
                    all(board[j][i] in drawn for j in range(5)) for i in range(5))) and board in good_boards:
                good_boards.remove(board)
                if not good_boards:
                    print(int(random) * sum(int(elem) for line in board for elem in line if elem not in drawn))
        else:
            continue
