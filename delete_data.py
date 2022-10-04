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
def revr():
    input1 = open('data.csv', 'w')
    output1 = open('s.csv', 'r')
    writer1 = csv.writer(input1)
    for row1 in csv.reader(output1):
         writer1.writerow(row1)
