import utils

LISTS_FILE = 'data/lists.csv'
LIST_FIELDS = ['id', 'name', 'board_id']


#CREATE_LIST: You create a board and you asign an ID to this board.
def create_list(name, board_id):
    lists = utils.read_csv(LISTS_FILE)
    new_id = str(len(lists) + 1)
    lists.append({'id': new_id, 'name': name, 'board_id': board_id})
    utils.write_csv(LISTS_FILE, lists, LIST_FIELDS)


def list_lists(board_id):
    lists = utils.read_csv(LISTS_FILE)
    for lst in lists:
        if lst['board_id'] == board_id:
            print(f"{lst['id']}: {lst['name']}")

#DELETE_LIST: You delete a list using an ID
def delete_list(list_id):
    lists = utils.read_csv(LISTS_FILE)
    lists = [lst for lst in lists if lst['id'] != list_id]
    utils.write_csv(LISTS_FILE, lists, LIST_FIELDS)
