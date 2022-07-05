
from ai import AI
from board import Board


def blokus():

    main_board = Board()
    players = [AI(p) for p in range(4)]

    moves_left = True

    while moves_left:
        moves_left = False
        for p in players:
            if p.has_valid_moves:
                p.decide_action(main_board)
                moves_left = True

    print(main_board)    




if (__name__ == "__main__"):
    blokus()
