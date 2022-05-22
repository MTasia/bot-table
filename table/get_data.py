import csv


def get_table(date, file_name):
    file_name = 'D:/Documents/Наглая морда без капли совести/pythonProject/data/' + file_name + '.csv'
    table = []
    with open(file_name, newline='\n', encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file, delimiter=";")
        data = {row["title"]: row["date"] for row in reader}
        for title in data:
            if date == data[title].split(',')[0]:
                table.append([title, data[title].split(',')[1]])
    return table
