"""
Program to take csv file as a input and provide formatted text file as output
Author: Utkarsh Reuben Khanna
CNo: C0750077
"""

from datetime import datetime
NEW_RATE_VALUE = 1.0385
with open("employee.txt",'w') as file:                  #Open employee.txt file in write mode 
    file.write("Employee Salary Estimate \n")           #Writing title as first line of file 
    file.write("-------------------------\n")           #Adding seperator 
    file.write("\n")                                    #Add an empty line 
    file.write("\n")                                    #Add an empty line                
    file.write("Employee name \t Hire Date \t Old Rate \t New Rate \n") #Adding headers to the file seperating each header with tab space
    file.write("--------------\t -------- \t -------- \t----------\n ") #Adding seperator to each header 
    with open('assets\Employees.csv') as emp:           #Open CSV file to read 
        next(emp)                                       #Skip the first line since its a header 
        for data in emp:                                #For each line in employees.csv    
            temp = data.strip().split(',')              #Remove all empty spaces and split for every comma and store in a temp
            fullName = temp[1].strip()+temp[2]          #Make full name by adding first name and last name
            dateHired =  datetime.strptime(temp[3],' %Y-%m-%d').date().strftime('%m-%d-%Y') #First create a date time object form the csv file then format it to mm-dd-yyyy
            oldRate = temp[4];                              #old rate which employees used to make
            newRate = str(round(float(oldRate)*NEW_RATE_VALUE,2))   # Multiply the old rate value with new rate constant and round it to 2 decimal places 
            file.write(fullName+"\t"+dateHired+"\t"+oldRate+"\t\t  "+newRate +"\n ") #Write it to the file with tab spaces 

   