import utils

CARDS_FILE = 'data/cards.csv'
CARD_FIELDS = ['id', 'title', 'description', 'list_id']

def create_card(title, description, list_id):
    cards = utils.read_csv(CARDS_FILE)
    new_id = str(len(cards) + 1)
    cards.append({'id': new_id, 'title': title, 'description': description, 'list_id': list_id})
    utils.write_csv(CARDS_FILE, cards, CARD_FIELDS)

def list_cards(list_id):
    cards = utils.read_csv(CARDS_FILE)
    for card in cards:
        if card['list_id'] == list_id:
            print(f"{card['id']}: {card['title']} - {card['description']}")

def delete_card(card_id):
    cards = utils.read_csv(CARDS_FILE)
    cards = [card for card in cards if card['id'] != card_id]
    utils.write_csv(CARDS_FILE, cards, CARD_FIELDS)
