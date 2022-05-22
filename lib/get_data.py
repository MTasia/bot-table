import csv


def get_books(type_book, file_name):
    file_name = 'D:/Documents/Наглая морда без капли совести/pythonProject/data/' + file_name + '.csv'
    books = []
    with open(file_name, newline='\n', encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file, delimiter=";")
        data = {row["title"]: row["type"] for row in reader}
        for item in data:
            type_item = data[item].split(",")[0]
            if type_book == type_item:
                link = data[item].split(",")[1]
                books.append([item, link])
    return books
