#Importing data from a file
#You must import the CSV library in order for files to be accessed
#CSV: Comma Separated Calues
#Records: rows of the file, different types of data all belonging together
#Fields: columns of the fie, sets of data (all data in a column is the same "type" ie names, ages, salaries, emails, etc

#BASE CODE----------------------------------------------------

import csv #import CSV library so we can read the file

total_records = 0 #you should always have a total records var for your first few attempts at file reading
total_salary = 0 #holds all salaries in file for total print at end

#right click the text/csv file in folder view then properties to find file location
#these file locations are case sensitive & space/special chatacter sensitive so doube check them
#flip all '\' to '/'

with open("G:/SE126.22/Lab_DataFromFile/example.csv") as csvfile:
    file = csv.reader(csvfile)
    #now the file we have connected is known in the program as 'file'
    #file has several records, each record has several fields
    #below is a FOR loop
    #for loops are loops --- they continually repeat a sequence of code
    #they continue based on a RANGE not a CONDITION
    #range 0-10 or a-f
    for rec in file:

        #RANGE: for each record in the file, do the following
        #rec is a variable that is initialized the for loop range

        total_records += 1 #total_recrds = total_records + 1
        #print(rec)
        #print only the names in the file -- specify position of data in list
        #print("RECORD #{0}: \t {1}".format(total_records, rec[0]))
        #print("RECORD #{0}: \t {1} \t${2}".format(total_records, rec[0], rec[2]))
        #add all salaries to total_salary
        total_salary += float(rec[2])
        print("{0} \t {1} \t ${2:.2f}".format(rec[0], rec[1], float(rec[2])))


print("TOTAL RECORDS",total_records)
print("TOTAL SALARY: ${0}".format(total_salary))