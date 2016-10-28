import csv

# function to load the files
def get_row(filename):
    with open(filename, "rb") as csvfile:
        datareader = csv.reader(csvfile)
        for row in datareader:
            yield row

file = 'updated_data.csv'


# find the row index of the last row for a student id.
last_rows = []
count = -1
last_words = ''

for row in get_row(file):
    count += 1
    if count == 0:
        continue
    if count == 1:
        last_words = row[0]
    elif row[0] != last_words:
        last_rows.append(count-1)
        last_words = row[0]
last_rows.append(count)
print count, last_rows[:10],last_rows[-1]


# split the data into training and testing set
count = -1
col = 0
for row in get_row(file):
    count += 1
    if count == 0:
        with open('train_data.csv', 'wb') as myfile:
            wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
            wr.writerow(row)
        with open('test_data.csv', 'wb') as myfile:
            wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
            wr.writerow(row)
    else:
        if col < len(last_rows) and count == last_rows[col]:
            with open('test_data.csv', 'ab') as myfile:
                wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
                wr.writerow(row)
                col += 1
        else:
            with open('train_data.csv', 'ab') as myfile:
                wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
                wr.writerow(row)

print 'Splitting is done!'





