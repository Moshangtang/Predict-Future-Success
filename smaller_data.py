import csv

# function to load the files
def get_row(filename):
    with open(filename, "rb") as csvfile:
        datareader = csv.reader(csvfile)
        for row in datareader:
            yield row

file = 'train_data.csv'

count = -1
for row in get_row(file):
    count += 1
    if count == 0:
        with open('small_train_data.csv', 'wb') as myfile:
            wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
            wr.writerow(row)
    elif count % 4 == 0:
        with open('small_train_data.csv', 'ab') as myfile:
            wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
            wr.writerow(row)
print 'Reducing is done!'
