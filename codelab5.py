import re
import csv
#Importing regex and CSV.

#Reading the log file.
source_file = open("C:\gitsem2\COMP593-lab5\log")

#Creating output file for two CSV file Output_1 and output_2.
output_1 = open("output_1.csv", "w")
output_2 = open("output_2.csv", "w")

#Creating header and applying it to the destination files.
writer_1 = csv.writer(output_1)
writer_1.writerow(["IP Address","Frequency"])

writer_2 = csv.writer(output_2)
writer_2.writerow(["Date", "Time", "Username", "Ip Address"])

dict = {}


#Using for loop with if else statements.
for i in source_file.readlines():
        source_file = i.split(":")[len(i.split(":"))-1].lower()
#using regex search function to search the regex.
        search = re.search(r'SRC=(\d+).(\d+).(\d+).(\d+).(\d+)', source_file)
        if(search != None):
            if source_file[search.span()[0]+4:search.span()[1]] in dict:
                dict[source_file[search.span()[0]+4:search.span()[1]]] = dict[source_file[search.span()[0]+4:search.span()[1]]] + 1
        else :
            dict[source_file[search.span()[0]+4:search.span()[1]]] = 1
#searching for invalid user  in log file.
        search2 = re.search(r'invalid',source_file)
        if(search2 != None):
#Joining the 
                Csvfile = ",".join([" ".join(i.split(" ")[0:2]) , i.split(" ")[2], source_file.split(" ")[3],
                            source_file.split(" ")[len(source_file.split(" "))-1]])
        output_2.write(Csvfile)

for file_data in dict.items():
    writer_1.writerow(file_data)