import csv
import os

#READ_CSV: You read the content, also, if the file does not exist, it creates it.
def read_csv(file_path):
    if not os.path.exists(file_path):
        with open(file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            if 'boards.csv' in file_path:
                writer.writerow(['id', 'name'])
            elif 'lists.csv' in file_path:
                writer.writerow(['id', 'name', 'board_id'])
            elif 'cards.csv' in file_path:
                writer.writerow(['id', 'title', 'description', 'list_id'])

    with open(file_path, newline='', mode='r') as file:
        reader = csv.DictReader(file)
        return list(reader)


def write_csv(file_path, data, fieldnames):
    with open(file_path, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
