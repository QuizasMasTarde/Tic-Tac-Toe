global player, game_grid


def winner_check(grid):
    global player
    lines = [
            [i[2] for i in grid],
            [i[1] for i in grid],
            [i[0] for i in grid],
            [grid[i][i] for i in range(3)]
            ]

    lines += grid + [[lines[i][i] for i in range(3)]]
    win = ""
    for line in lines:
        if line.count(player) == 3:
            win = f"{player} wins"
    turn_counter = 0
    for i in grid:
        turn_counter += i.count("X") + i.count("O")
    if win == "" and turn_counter == 9:
        win = "Draw"

    return win


def turn():
    global player, game_grid

    while True:
        row, column = input().split()
        try:
            row = int(row)
            column = int(column)
        except ValueError:
            print("You should enter numbers!")
            continue
        if row not in [1, 2, 3] or column not in [1, 2, 3]:
            print("Coordinates should be from 1 to 3!")
            continue
        if game_grid[row - 1][column - 1] in ["X", "O"]:
            print("This cell is occupied! Choose another one!")
            continue
        else:
            game_grid[row - 1][column - 1] = player
            break


def print_state(grid):
    border = "---------"
    print(f"{border}\n"
          f"| {' '.join(grid[0])} |\n"
          f"| {' '.join(grid[1])} |\n"
          f"| {' '.join(grid[2])} |\n"
          f"{border}")


def player_switch():
    global player
    player = "O" if player == "X" else "X"


def main():
    global player, game_grid

    game_grid = [[" " for _ in range(3)] for _ in range(3)]
    player = "X"
    winner = ""
    print_state(game_grid)
    while not winner:
        turn()
        print_state(game_grid)
        winner = winner_check(game_grid)
        player_switch()
    print(winner)


if __name__ == "__main__":
    main()
