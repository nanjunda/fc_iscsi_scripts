import csv

with open('x.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    count = 0
    sum4=0.0
    sum8=0.0
    sum11=0.0
    sum27=0.0
    sum35=0.0
    for row in readCSV:
        s = str(row[4])
        if "Avg" not in s:
            count += 1
            print(row[4],row[8],row[11],row[27],row[35])
            sum4 += float(row[4])
            sum8 += float(row[8])
            sum11 += float(row[11])
            sum27 += float(row[27])
            sum35 += float(row[35])
    avg4=sum4/count
    avg8=sum8/count
    avg11=sum11/count
    avg27=sum27/count
    avg35=sum35/count
    print (avg4, avg8, avg11, avg27, avg35)