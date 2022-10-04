import csv
def word():
    request = input('Введите Id')
    return request
def delete_data():
    request = word()
    input = open('data.csv', 'r')
    output = open('s.csv', 'w')
    writer = csv.writer(output)
    for row in csv.reader(input):
        if row[0] != request:         
            writer.writerow(row)
            break
    input = open('data.csv', 'w')
    output = open('s.csv', 'r')
    writer = csv.writer(input)
    for row in csv.reader(output):
         writer.writerow(row)
