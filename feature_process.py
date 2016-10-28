import csv

# function to load the files
def get_row(filename):
    with open(filename, "rb") as csvfile:
        datareader = csv.reader(csvfile)
        for row in datareader:
            yield row

file = 'dataset.csv'


# student id list and KC_list
student_id = []
KC_list = []
count = 0
for row in get_row(file):
    count +=1
    if count != 1:
        if row[1] not in student_id:
            student_id.append(row[1])
        strings = row[17].split("~~")
        for string in strings:
            if string!='' and string not in KC_list:
                KC_list.append(string)

print len(student_id), len(KC_list)


# create features
feature_list = ['ID']+ KC_list + ['CFA']
l = len(feature_list)
print l

feature_dic = {key: {} for key in student_id} # I created a feature dictionary to store all the information for each student
# the structure is like {'student_id':{'knowledge iterm1' :{'corrects':0,'opportunities':0,'incorrects':0}}}
count = 0
with open('updated_data.csv', 'wb') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerow(feature_list)
    for row in get_row(file):
        count += 1
        if count != 1:
            datalist = [0 for n in range(l)]
            datalist[-1] = row[13]
            datalist[0] = row[1]
            strings = row[17].split("~~") # split the knowledge iterm by '~~'
            if type(row[18]) is str:
                opps = row[18].split("~~") # the opptunity is seperated by ~~ for each knowledge item. I need split it and store it in knowledge item dictionary
            else:
                opps = row[18]
            for i, string in enumerate(strings):
                if string != '':
                    if string in feature_dic[row[1]].keys():
                        dic = feature_dic[row[1]][string]
                        dic['Incorrects'] = dic['Incorrects'] + float(row[14]) # I added all the incorrects up.
                        a = opps[i]
                        if a == '':
                            a = 1
                        else:
                            a = float(opps[i])
                        if a > dic['Opp']:
                            dic['Opp'] = a
                        dic['cor_rate'] = 1-dic['Incorrects']/(dic['Opp']+dic['Incorrects']) # calculate the correct rate
                        index = feature_list.index(string)
                        datalist[index] = dic['cor_rate']

                    else:
                        feature_dic[row[1]][string] = {}
                        dic = feature_dic[row[1]][string]
                        dic['Incorrects'] = float(row[14]) # store the incorrects to the dictionary
                        a = opps[i]
                        if a == '':
                            dic['Opp'] = 1
                        else:
                            dic ['Opp'] = float(opps[i])
                        dic['cor_rate'] = 1 - dic['Incorrects']/(dic['Opp']+dic['Incorrects'])
                        index = feature_list.index(string)
                        datalist[index] = dic['cor_rate']
            wr.writerow(datalist)

print 'Data is ready!'








