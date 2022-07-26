import re
import csv 
#Importing regex and CSV.

#Reading the log file.
source_file = open("C:\gitsem2\COMP593-lab5\log")

#Creating output file for two CSV file Output_1 and output_2.
output_1 = open("output_1.csv", "w")
output_2 = open("output_2.csv", "w")
