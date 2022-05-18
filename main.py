from time import sleep 
import requests
import utils


def main():

    NAME = "Mauricio"
    print("\n------- Starting tic-tac-toe bot -------\n")

    # Register phase begins
    registry_open = utils.is_registry_open()

    while not registry_open:
        print("Waiting for registry to open...\n")
        sleep(5)
        registry_open = utils.is_registry_open()

    # Register is open now, let's register as player
    PLAYER_ID = utils.register_user(NAME)
    print("Registered successfully as {}, player ID is: {}\n".format(NAME, PLAYER_ID))
    sleep(2)

    # Game-continues flag, set to True until there's a winner
    game_continues = utils.does_game_continue()

    while game_continues:

        my_turn = utils.is_my_turn(PLAYER_ID)
        
        # Flag to waiti for our turn
        while not my_turn:
            print("Waiting for turn...")
            sleep(5)
            my_turn = utils.is_my_turn(PLAYER_ID)

        # It's our turn, start by reading the latest version of the board
        board = utils.read_board()
        utils.print_board(board)

        # Entering cycle of deciding-validating our next move
        valid_move = False

        while not valid_move:

            print("Deciding move...\n")
            sleep(1)
            next_move = utils.decide_move(board, PLAYER_ID)
            valid_move = utils.validate_move(board, next_move) # Validates next move

        print("Move to send, row: {}, col: {}\n".format(next_move[0], next_move[1]))

        # Send move to API and check if game continues
        utils.send_move(PLAYER_ID, next_move)

        # Wait and update game_continues flag
        sleep(5)
        game_continues = utils.does_game_continue()

    # Game ends, check API for winner
    print("GAME OVER\nCheck API for winner.")

if __name__ == '__main__':
    main()
