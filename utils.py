"""
[Module] Tic-tac-toe bot utilities.
"""
from random import randint, random
import requests
from urllib.parse import unquote


API_URL = "http://127.0.0.1:8000"


def is_registry_open() -> bool:
    """
    Checks if registry is available via API.
    """
    try:
        url = "{}/registry".format(API_URL)
        res = requests.get(url)

        if res.text == "true":
            return True
        elif res.text == "false":
            return False

    except:
        return False


def register_user(name: str) -> str:
    """
    Registers user in API game.
    """
    url = "{}/register_player/{}".format(API_URL, name)
    res = requests.post(url)
    player_id = res.text[1]
    return player_id


def is_my_turn(player_id: str) -> bool: 
    """
    Checks if it is our turn via API.
    """
    url = "{}/turn/{}".format(API_URL, player_id)
    res = requests.get(url)
    
    if res.text == "true":
        return True
    elif res.text == "false":
        return False


def read_board() -> list:
    """
    Gets game board via API.
    """
    url = "{}/board".format(API_URL)
    res = requests.get(url)
    board_str = res.text
    board = [
        [board_str[1], board_str[2], board_str[3]], 
        [board_str[4], board_str[5], board_str[6]], 
        [board_str[7], board_str[8], board_str[9]]
    ]

    return board


def decide_move(board: list, player_id: str) -> list:
    """
    Decides next move to make.
    """
    #Calcular cual es la variable del enemigo

    enemigo = "X"
    if player_id == "X":
        enemigo == "0"

    #Estrategia para ganar siempre en medio para ganar o empatar

    if board [0][0]== enemigo and board [1][1] == "-":
        return [1,1]
    if board [0][1]== enemigo and board [1][1] == "-":
        return [1,1]
    if board [0][2]== enemigo and board [1][1] == "-":
        return [1,1]
    if board [1][0]== enemigo and board [1][1] == "-":
        return [1,1]
    if board [1][2]== enemigo and board [1][1] == "-":
        return [1,1]
    if board [2][0]== enemigo and board [1][1] == "-":
        return [1,1] 
    if board [2][1]== enemigo and board [1][1] == "-":
        return [1,1]
    if board [2][2]== enemigo and board [1][1] == "-":
        return [1,1]

    #Estrategia para siempre empatar si pierdo enmedio 
    #elegir siempre las esquinas

    if board [1][1] == enemigo and board [0][0] == "-" and board [0][2] == "-" and board [2][0] == "-" and board [2][2] == "-":
        corner = [[0,0],[0,2],[2,0],[2,2]]
        return random.choice(corner)

    #Estrategia para poner de los de enmedio despues de ganar enmedio y si estoy en contra diagonalmente 
    if board [1][1] == player_id and board [0][0] == enemigo and board [2][2] == enemigo and board [1][0] == "-" and board [1][2]  == "-":
        middle = [[1,0],[1,2]]
        return random.choice(middle)
    if board [1][1] == player_id and board [0][2] == enemigo and board [2][0] == enemigo and board [1][0] == "-" and board [1][2] == "-":
        middle_c = [[1,0],[1,2]]
        return random.choice(middle_c)

    

    
    #Posibilidades Gane 

    #Paso 2 Ganes Horizanteles,diagonales,vertical de todo el board 

    #Caso 1 Gane Horizontal de arriba 

    if board [0][0] == player_id and board [0][1] == player_id and board [0][2] == "-":
        return [0,2]
    if board [0][0] == player_id and board [0][1] == player_id and board [0][2] == "-":
        return [0,2]   
    if board [0][0] == player_id and board [0][2] == player_id and board [0][1] == "-":
        return [0,1]     

    #Caso 2 Gane Horizontal de enmedio 

    if board [1][0] == player_id and board [1][1] == player_id and board [1][2] == "-":
        return [1,2]
    if board [1][0] == player_id and board [1][2] == player_id and board [1][1] == "-":
        return [1,1]   
    if board [1][2] == player_id and board [1][1] == player_id and board [1][0] == "-":
        return [1,0]    

    #Caso 3 Gane Horizontal de abajo  

    if board [2][0] == player_id and board [2][1] == player_id and board [2][2] == "-":
        return [2,2]
    if board [2][0] == player_id and board [2][2] == player_id and board [2][1] == "-":
        return [2,1]   
    if board [2][2] == player_id and board [2][1] == player_id and board [2][0] == "-":
        return [2,0]   

    #Caso  1 Gane Vertical de la columna izquierda del board

    if board [0][0] == player_id and board [1][0] == player_id and board [2][0] == "-":
        return [2,0]
    if board [0][0] == player_id and board [2][0] == player_id and board [1][0] == "-":
        return [1,0]   
    if board [2][0] == player_id and board [1][0] == player_id and board [0][0] == "-":
        return [0,0]   
    
    #Caso 2 Bloqueo Vertical de la columna de enmedio del board 

    if board [0][1] == player_id and board [1][1] == player_id and board [2][1] == "-":
        return [2,1]
    if board [0][0] == player_id and board [2][1] == player_id and board [1][1] == "-":
        return [1,1]   
    if board [2][1] == player_id and board [1][1] == player_id and board [0][1] == "-":
        return [0,1] 

    #Caso 3 Bloqueo Vertical de la columna de la columna de la derecha del board 

    if board [0][2] == player_id and board [1][2] == player_id and board [2][2] == "-":
        return [2,2]
    if board [0][2] == player_id and board [2][2] == player_id and board [1][2] == "-":
        return [1,2]   
    if board [2][2] == player_id and board [1][2] == player_id and board [0][2] == "-":
        return [0,2] 

    #Caso 1 Diagonal de la posicion (0,0) a (2,2)

    if board [0][0] == player_id and board [1][1] == player_id and board [2][2] == "-":
        return [2,2]
    if board [0][0] == player_id and board [2][2] == player_id and board [1][1] == "-":
        return [1,1]   
    if board [2][2] == player_id and board [1][1] == player_id and board [0][0] == "-":
        return [0,0] 

    #Caso 2 Diagonal de la poscion (2,0) a (0,2)

    if board [0][2] == player_id and board [1][1] == player_id and board [2][0] == "-":
        return [2,0]
    if board [2][0] == player_id and board [0][2] == player_id and board [1][1] == "-":
        return [1,1]   
    if board [2][0] == player_id and board [1][1] == player_id and board [0][2] == "-":
        return [0,2] 
    


    
    #Paso 1 Bloqueos Horizanteles,diagonales,vertical de todo el board 

      #Caso 1 Bloqueo Horizontal de arriba 
    if board [0][0] == enemigo and board [0][1] == enemigo and board [0][2] == "-":
        return [0,2]
    if board [0][0] == enemigo and board [0][1] == enemigo and board [0][2] == "-":
        return [0,2]   
    if board [0][0] == enemigo and board [0][2] == enemigo and board [0][1] == "-":
        return [0,1]     

    #Caso 2 Bloqueo Horizontal de enmedio 

    if board [1][0] == enemigo and board [1][1] == enemigo and board [1][2] == "-":
        return [1,2]
    if board [1][0] == enemigo and board [1][2] == enemigo and board [1][1] == "-":
        return [1,1]   
    if board [1][2] == enemigo and board [1][1] == enemigo and board [1][0] == "-":
        return [1,0]    

    #Caso 3 Bloqueo Horizontal de abajo  

    if board [2][0] == enemigo and board [2][1] == enemigo and board [2][2] == "-":
        return [2,2]
    if board [2][0] == enemigo and board [2][2] == enemigo and board [2][1] == "-":
        return [2,1]   
    if board [2][2] == enemigo and board [2][1] == enemigo and board [2][0] == "-":
        return [2,0]   

    #Caso  1  Bloqueo Vertical de la columna izquierda del board

    if board [0][0] == enemigo and board [1][0] == enemigo and board [2][0] == "-":
        return [2,0]
    if board [0][0] == enemigo and board [2][0] == enemigo and board [1][0] == "-":
        return [1,0]   
    if board [2][0] == enemigo and board [1][0] == enemigo and board [0][0] == "-":
        return [0,0]   
    
    #Caso 2 Bloqueo Vertical de la columna de enmedio del board 

    if board [0][1] == enemigo and board [1][1] == enemigo and board [2][1] == "-":
        return [2,1]
    if board [0][0] == enemigo and board [2][1] == enemigo and board [1][1] == "-":
        return [1,1]   
    if board [2][1] == enemigo and board [1][1] == enemigo and board [0][1] == "-":
        return [0,1] 

    #Caso 3 Bloqueo Vertical de la columna de la columna de la derecha del board 

    if board [0][2] == enemigo and board [1][2] == enemigo and board [2][2] == "-":
        return [2,2]
    if board [0][2] == enemigo and board [2][2] == enemigo and board [1][2] == "-":
        return [1,2]   
    if board [2][2] == enemigo and board [1][2] == enemigo and board [0][2] == "-":
        return [0,2] 

    #Caso 1 Diagonal de la posicion (0,0) a (2,2)

    if board [0][0] == enemigo and board [1][1] == enemigo and board [2][2] == "-":
        return [2,2]
    if board [0][0] == enemigo and board [2][2] == enemigo and board [1][1] == "-":
        return [1,1]   
    if board [2][2] == enemigo and board [1][1] == enemigo and board [0][0] == "-":
        return [0,0] 

    #Caso 2 Diagonal de la posicion (2,0) a (0,2)

    if board [0][2] == enemigo and board [1][1] == enemigo and board [2][0] == "-":
        return [2,0]
    if board [2][0] == enemigo and board [0][2] == enemigo and board [1][1] == "-":
        return [1,1]   
    if board [2][0] == enemigo and board [1][1] == enemigo and board [0][2] == "-":
        return [0,2] 

   
    row = randint(0, 2)
    column = randint(0, 2)
    return [row, column]


def validate_move(board: list, move: list) -> bool:
    """
    Checks if the desired next move hits an empty position.
    """
    row, col = move[0], move[1]

    if board[row][col] == "-":
        return True

    return False


def send_move(player_id: str, move: list) -> None:
    """
    Sends move to API.
    """
    row, col = move[0], move[1]
    url = "{}/move/{}/{}/{}".format(API_URL, player_id, row, col)
    res = requests.post(url)
    return None


def does_game_continue() -> bool:
    """
    Checks if the current match continues via API.
    """
    url = "{}/continue".format(API_URL)
    res = requests.get(url)

    if res.text == "true":
        return True
    elif res.text == "false":
        return False


def print_board(board: list) -> None:
    '''
    Prints the baord in console to watch the game.
    '''
    print("\nCurrent board: \n")
    print(board[0][0], "|", board[0][1], "|", board[0][2])
    print("----------")
    print(board[1][0], "|", board[1][1], "|", board[1][2])
    print("----------")
    print(board[2][0], "|", board[2][1], "|", board[2][2], "\n")
