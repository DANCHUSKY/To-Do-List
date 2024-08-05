import boards
import lists
import cards


def main_menu():
    while True:
        print("\n--- TO-DO List en Terminal ---")
        print("1. Crear Tablero")
        print("2. Listar Tableros")
        print("3. Eliminar Tablero")
        print("4. Crear Lista")
        print("5. Listar Listas")
        print("6. Eliminar Lista")
        print("7. Crear Tarjeta")
        print("8. Listar Tarjetas")
        print("9. Eliminar Tarjeta")
        print("0. Salir")
        choice = input("Seleccione una opción: ")

        if choice == '1':
            name = input("Nombre del tablero: ")
            boards.create_board(name)
        elif choice == '2':
            boards.list_boards()
        elif choice == '3':
            board_id = input("ID del tablero a eliminar: ")
            boards.delete_board(board_id)
        elif choice == '4':
            board_id = input("ID del tablero: ")
            name = input("Nombre de la lista: ")
            lists.create_list(name, board_id)
        elif choice == '5':
            board_id = input("ID del tablero: ")
            lists.list_lists(board_id)
        elif choice == '6':
            list_id = input("ID de la lista a eliminar: ")
            lists.delete_list(list_id)
        elif choice == '7':
            list_id = input("ID de la lista: ")
            title = input("Título de la tarjeta: ")
            description = input("Descripción de la tarjeta: ")
            cards.create_card(title, description, list_id)
        elif choice == '8':
            list_id = input("ID de la lista: ")
            cards.list_cards(list_id)
        elif choice == '9':
            card_id = input("ID de la tarjeta a eliminar: ")
            cards.delete_card(card_id)
        elif choice == '0':
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")
