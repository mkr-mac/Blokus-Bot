
from ai import AI, BigFirstAI, SoftBigFirstAI, RecursiveAI, SelfOnlyRecursiveAI
from board import Board


def blokus():

    main_board = Board(size=20)
    players = []
    players.append(BigFirstAI())
    players.append(AI())
    players.append(BigFirstAI())
    players.append(BigFirstAI())

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

    print("Final Scores:")
    for player in players:
        print(f"Player {player.id}: {player.score}")

    print("Final Board:")
    for l in main_board:
        print(l)

    main_board.output_state()




if (__name__ == "__main__"):
    blokus()
