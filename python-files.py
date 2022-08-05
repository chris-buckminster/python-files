"""
Chris Buckminster 
CIS245 - Introduction to Programming
Week 9 Assignment

- Create a program that performs file processing activities. 
- The program this week will use the OS library in order to validate that a directory exists before creating a file in that directory. 
- The program will prompt the user for the directory they would like to save the file in as well as the name of the file.
- The program should then prompt the user for their name, address, and phone number. 
- The program will write this data to a comma separated line in a file and store the file in the directory specified by the user.
- Once the data has been written the program should read the file you just wrote to the file system and display the file contents to the user for validation purposes. 
"""


import os

folder = input('Enter folder name: ')
# check for valid folder name
if os.path.isdir(folder):
    filename = input('Enter file name: ') # read file name
    file = folder + "\\" + filename # create the fully qualified file name
    name = input('Enter user name: ') # read name
    address = input('Enter address: ') # read address
    phone = input('Enter phone number: ') # read phone
    # code to write the data to the file
    outfile = open(file, 'w')
    print(f'{name},{address},{phone}', file=outfile)
    outfile.close()
    # code to read the data to the file
    infile = open(file, 'r')
    data = infile.readline().strip().split(',')
    # display the file contents to the user for validation purposes.
    print(f'Your name: {data[0]}')
    print(f'Your address: {data[1]}')
    print(f'Your phone: {data[2]}')
    infile.close()

else:
    print(f'Error: {folder} do not exist.')