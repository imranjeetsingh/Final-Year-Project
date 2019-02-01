import csv
file_open = open("TRAJECTOR.tsv","r")
# for file in file_open:
file = csv.reader(file_open,delimiter='\t')
ans = open("trajector_data.txt","w")
for file in file:
    # print(file[4])
    ans.write(file[4])
    ans.write("\n")
