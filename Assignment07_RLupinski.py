# ---------------------------------------------------------------------------- #
# Title: Assignment 07
# Description: Task: Create a new script that demonstrates
#              how Pickling and Structured error handling work.
# ChangeLog (Who,When,What):
# RLupinski,02.23.2022
#    - initialize script
#    - processor and IO functionss
#    - try-except functionality
# RLupinski,02.24.2022
#    - custom exception handling fix
# --------------------------------------------------------------------------- #

# Import Modules ------------------------------------------------------------ #
import pickle  # import pickle module for binary handling
from datetime import datetime  # import datetime module

# Data ---------------------------------------------------------------------- #
# Declare variables and constants
strFileName = "WorkLog.dat"  # work log binary file
intID = ""  # initialize ID string
strWork = ""  # initialize work log string
lstWorkLog = []  # initialize list of work logs


# Processing  --------------------------------------------------------------- #
class Processor:
    @staticmethod
    def save_data_to_file(file_name, list_of_data):
        """
        saves data to the binary file
        :param file_name: name of file to save data
        :param list_of_data: list of work logs
        :return:
        """
        objFile = open(file_name, "ab")  # open dat file in append mode binary
        pickle.dump(list_of_data, objFile)  # write work log to file
        objFile.close()  # close connection to file


# Presentation (Input/Output)  ---------------------------------------------- #
class IO:
    @staticmethod
    def read_data_from_file(file_name):
        """
        reads data from the binary file
        :param file_name: name of file to read data
        :return:
        """
        print("*************************************************")
        print(f"Current logs in {file_name}:")  # prints current data from WorkLog.dat
        objFile = open(file_name, "rb")  # open connection to file in read mode binary
        while True:  # loop through all objects until end of file error occurs
            try:
                data = pickle.load(objFile)  # load data from file to data var
                print(data)  # print all the data to the console
            except EOFError:  # when end of file error occurs, break the loop
                break
        objFile.close()  # close connection to file
        print("*************************************************")
        print("\n")
        return


# Custom Exception Class  --------------------------------------------------- #
class WorkLogNameError(Exception):
    """Can not have numeric entry for name"""

    @staticmethod
    def __int__(self):  # custom error handling example for when a non-alphanumeric name is tried
        return 'Can not have numeric entry for name'


# Main Body of Script  ------------------------------------------------------ #

while True:  # loop through option to user
    IO.read_data_from_file(strFileName)  # display current work log
    choice = input("Type 1 to log work, or hit any key to exit: ")  # option to add log or exit
    if choice == "1":  # if choice == 1 add a new log
        try:  # trying code for errors
            strName = input("Enter your name: ")  # prompt user for name
            if strName.isnumeric():  # if numeric entry is found
                raise WorkLogNameError()  # raise custom error
            intID = int(input("Enter an ID: "))  # get worker's ID
            strWork = str(input("Log work: "))  # get string of work logged
            ts = str(datetime.now())  # get timestamp, convert to string
            lstWorkLog = [strName, intID, strWork, ts]  # list of name,ID,work logged, and timestamp
            Processor.save_data_to_file(strFileName, lstWorkLog)  # pass file and work log list to function
        except ValueError as e:  # raise exception for ID non-numeric
            print("ID must be a number")
            print("Built-In Python error info: ")
            print(e, e.__doc__, type(e), sep='\n')  # return python error docs
        except Exception as e:  # generic catch-all error exception
            print("There was a non-specific error!")
            print("Built-In Python error info: ")
            print(e, e.__doc__, type(e), sep='\n')  # return python error docs
    else:  # else break the loop and end the program
        break
