
from ai import AI, BigFirstAI, SoftBigFirstAI, RecursiveAI, SelfOnlyRecursiveAI
from board import Board


def blokus():

    main_board = Board()
    players = []
    players.append(BigFirstAI(1))
    players.append(SoftBigFirstAI(2))
    players.append(SoftBigFirstAI(3))
    players.append(BigFirstAI(4))

    moves_left = True

    turn_counter = 1

    while moves_left:
        moves_left = False
        
        print(f"Turn {turn_counter}!")
        turn_counter+=1

        for p in players:
            if p.has_valid_moves:
                phands = []
                for h in players:
                    phands.append(h.hand)
                p.decide_action(main_board, playerhands=phands)
                moves_left = True

    print("Final Board:")
    for l in main_board:
        print(l)




if (__name__ == "__main__"):
    blokus()
