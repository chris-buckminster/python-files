"""
Chris Buckminster
CIS245 - Introduction to Programming
Week 9 Assignment

1. Prompt the user for the name of the directory in which they want to save a file. - 15% (done)
2. Prompt the user for the name of the file they want to save to the directory in requirement 1. - 15% (done)
3. If the directory from requirement 1 doesn't exist the program must create the specified directory. - 20% (done)
4. The program will prompt the user for their name, address, and phone number and write that data as a line of comma separated values to the file using the directory and filename from requirements 1 and 2. (example: John Smith,123 Main St,402-555-1212) - 20% (done) 
5. After the data has been written to the file your program must open the file, read the contents, and display the contents to the user as program output. - 20% (done)
6. Create a GitHub Respository for Assignment 9.1 - 5% (done) 

Submit a link to the respository from requirement 6 as your assignment submission. - 5% (done)
"""

import os # imports the OS module

pathofFile = input('Enter the file path where you would like to save the file: ') # prompt user for path of file

nameofFile = input('Enter the name of the file you want to save: ') # prompt user for name of file

if not os.path.exists(pathofFile): # if it doesn't exist, make it 

    os.makedirs(pathofFile)

completeName = os.path.join(pathofFile,nameofFile+".csv") # added a .csv filename because it seemed appropriate

fileObj = open(completeName, "w") # open the file in the specified path

name = input('Enter your name: ') # prompt user for name

address = input('Enter address: ') # prompt user for address

phoneNumber = input('Enter your phone number: ') # prompt user for phone number 

fileObj.write(name+','+address+','+phoneNumber+'\n') # write user input to file

fileObj.close() # close the file 

fileObj = open(completeName, "r") 

print(fileObj.read()) # open the file and show the user