# TO-DO List in Terminal

## Description

This project is a terminal-based task management application. It allows you to create, list, and delete boards, lists, and cards. Data is stored in CSV files for easy persistence and manipulation. This project is written in Python and does not require a graphical user interface.

## Features

- **Create Board**: Add a new board with a specified name.
- **List Boards**: Display all existing boards.
- **Delete Board**: Remove a board by specifying its ID.
- **Create List**: Add a new list to a specific board.
- **List Lists**: Display all lists associated with a specific board.
- **Delete List**: Remove a list by specifying its ID.
- **Create Card**: Add a new card to a specific list.
- **List Cards**: Display all cards associated with a specific list.
- **Delete Card**: Remove a card by specifying its ID.

## Project Structure:

.
├── main.py
├── todo.py
├── boards.py
├── lists.py
├── cards.py
├── utils.py
└── data
├── boards.csv
├── lists.csv
└── cards.csv


- **`main.py`**: The main file that runs the program.
- **`todo.py`**: Contains the main menu and navigation logic.
- **`boards.py`**: Handles operations related to boards.
- **`lists.py`**: Handles operations related to lists.
- **`cards.py`**: Handles operations related to cards.
- **`utils.py`**: Contains auxiliary functions for reading and writing CSV files.
- **`data/`**: Directory where CSV files are stored (`boards.csv`, `lists.csv`, `cards.csv`).

## Requirements

- Python 3.x

## Installation

1. **Clone the repository**:

   ```sh
   git clone <https://github.com/DANCHUSKY/To-Do-List.git>
   cd <To-Do-List>

TO-DO List
![image](https://github.com/user-attachments/assets/3bc74832-fa5b-4a1e-8bcc-267395425a4d)

