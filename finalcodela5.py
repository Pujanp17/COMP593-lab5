import re
from collections import Counter
import csv
#Importing.


#Read and print the log file.
def reader(filename):
    with open(filename) as f:
        log = f.read()
        print(log)

#Using regex to sort out the ip addresses and there count.
        regexp = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
        ips_list = re.findall(regexp, log)
        return(ips_list)

#Using regex to sort out other information from log file.
def count(ips_list):
    return Counter(ips_list)


#Creating a new csv file of the output1.
def write_csv(counter):
    with open('output_1.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)

#Creating header.
        header = ['IP Address', 'Frequency']
        writer.writerow(header)
        for item in counter:
            writer.writerow((item, counter[item]))

#Creating a new csv file of the output2.
output_2 = open("output_2.csv", "w")

#Creating header for output 2 csv file.
writer_2 = csv.writer(output_2)
writer_2.writerow(["Date", "Time", "Username", "Ip Address"])


#defining variable for source file.
source_file = open("C:\Demofolder\os2lab\log")
#Creating a another output for CSV file.
for i in source_file.readlines():
    log_file = i.split(":")[len(i.split(":"))-1].lower()
#using regex re.search function to search the regex.
    search = re.search(r'SRC=\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', log_file)
    if(search != None):
        F = log_file[search.span()[0]+4:search.span()[1]]
        if  F in {}:
            dictionary =  {}[F] = dictionary + 1
        else :
            dictionary = 1
#searching for invalid user  in log file.
    search2 = re.search(r'invalid',log_file)
    if(search2 != None):
#writing change to the output file.
        Csvfile = ",".join([" ".join(i.split(" ")[0:2]) , i.split(" ")[2], log_file.split(" ")[3],
                            log_file.split(" ")[len(log_file.split(" "))-1]])
        output_2.write(Csvfile)


if __name__ == '__main__':
        write_csv(count(reader('log')))
