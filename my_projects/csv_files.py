import csv

with open('test.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['user_id', 'user_name', 'comments_qty'])
    writer.writerow([5235, 'bogdan', 1234])
    writer.writerow([8631, 'mike', 246])
    writer.writerow([7100, 'elise', 33])

with open('test.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)
    for line in reader:
        print(line)


    print(reader.line_num)
