import utils


BOARDS_FILE = 'data/boards.csv'
BOARD_FIELDS = ['id', 'name']


#CREATE_BOARD: You create a board and you asign an ID to this board.
def create_board(name):
    boards = utils.read_csv(BOARDS_FILE)
    new_id = str(len(boards) + 1)
    boards.append({'id': new_id, 'name': name})
    utils.write_csv(BOARDS_FILE, boards, BOARD_FIELDS)

#You make a loop to list all boards.
def list_boards():
    boards = utils.read_csv(BOARDS_FILE)
    for board in boards:
        print(f"{board['id']}: {board['name']}")


#You delete a board when you say an ID     "primary key"
def delete_board(board_id):
    boards = utils.read_csv(BOARDS_FILE)
    boards = [board for board in boards if board['id'] != board_id]
    utils.write_csv(BOARDS_FILE, boards, BOARD_FIELDS)
