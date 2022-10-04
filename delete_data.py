import csv
def wort():
    request = input('Введите Фамилию')
    return request
def delete_data():
    request = wort()
    input = open('data.csv', 'r')
    output = open('s.csv', 'w')
    writer = csv.writer(output)
    for row in csv.reader(input):
        if row[0] != request:         
            writer.writerow(row)
    input1 = open('data.csv', 'w')
    output = open('s.csv', 'r')
    writer = csv.writer(input1)
    for row in csv.reader(output):
         writer.writerow(row)
    input.close()
    output.close()
