
from ai import AI
from board import Board


def blokus():

    main_board = Board()
    players = [AI(p+1) for p in range(4)]

    moves_left = True

    while moves_left:
        moves_left = False
        for p in players:
            if p.has_valid_moves:
                p.decide_action(main_board)
                moves_left = True

    for l in main_board:
        print(l)




if (__name__ == "__main__"):
    blokus()
