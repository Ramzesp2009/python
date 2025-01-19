def zeichne_spielfeld(lists: list):
    print('_________')
    for list in lists:
        print((' | ').join(list))
        print('_________')


def starte_spiel():
    lists = [[' ' for i in range(3)] for i in range(3)]
    count = 0
    while True:
        zeichne_spielfeld(lists)
        count +=1

        # Stop game when is a draw
        if count > 9:
            print("The game ended in a draw!")
            break

        # Which player is now
        if count % 2 == 0:
            player = "Player 2"
        else:
            player = "Player 1"

        # ask player a move
        zeile = int(input(f"{player} enter one figure please from 0 to 2:\t"))
        spalter = int(input(f"{player} enter one figure please from 0 to 2:\t"))

        # Check correct input
        if zeile > 2:
            count -= 1
            continue
        if spalter > 2:
            count -= 1
            continue
        # Check correct move
        if count % 2 == 0:
            if lists[zeile][spalter] == ' ':
                lists[zeile][spalter] = 'O'
            else:
                print("Please one more time your move")
                count -= 1
        else:
            if lists[zeile][spalter] == ' ':
                lists[zeile][spalter] = 'X'
            else:
                print("Please one more time your move")
                count -= 1

        # Check all the rows == X
        for row in lists:
            if all(element == 'X' for element in row):
                print(f"{player} win")
                break
        # Check all the columns == X
        for i in range(3):
            if all(lists[j][i] == 'X' for j in range(3)):
                print(f"{player} win")
                break
        # Check diagonal from left to right == X
        if all(lists[i][i] == 'X' for i in range(3)):
            print(f"{player} win")
            break
        # Check diagonal from right to left == X
        if all(lists[i][abs(i - 2)] == 'X' for i in range(3)):
            print(f"{player} win")
            break

        # Check all the rows == O
        for row in lists:
            if all(element == 'O' for element in row):
                print(f"{player} win")
                break
        # Check all the columns == O
        for i in range(3):
            if all(lists[j][i] == 'O' for j in range(3)):
                print(f"{player} win")
                break
        # Check diagonal from left to right == O
        if all(lists[i][i] == 'O' for i in range(3)):
            print(f"{player} win")
            break
        # Check diagonal from right to left == O
        if all(lists[i][2 - i] == 'O' for i in range(3)):
            print(f"{player} win")
            break


starte_spiel()

