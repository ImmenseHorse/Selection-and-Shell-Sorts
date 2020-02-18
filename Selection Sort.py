#This program was written by Duc Nguyen on Dec 12, 2019.
#This program will create a file called "sorted.txt" containing the numbers from
#the "unsorted.txt" sorted from lowest to highest using Selection Sort.

import time

#The constants for 2 file names
UNSORTED = "unsorted.txt" 
SORTED = "sorted.txt"

def CreateNumericList(filename):
    """This function accepts a filename and then creates a numeric list from the
    data in this file"""

    #in_file - the file object associated with the unsorted text file
    #entire_list - the list of integers existed in the unsorted text file
    
    in_file = open(filename, "r")
    entire_list = in_file.readlines()
    in_file.close()
    for x in range(len(entire_list)):
        entire_list[x] = int(entire_list[x].strip())
    return entire_list
    
def SelectionSort(entire_list):
    """This function accepts a numeric list and then sorts the integers in this
    list from lowest to highest"""
    
    #passnum - the number of passes required to sort the file
    #switchnum - the number of switches required to sort the file
    #entire_list - the list of integers existed in the unsorted text file
    #temp - the temporary variable storing the intergers
    #requirednums - the list consists of switchnum and passnum
    #min_index - the position of the smallest number 
    
    passnum = 0
    switchnum = 0
    for x in range(len(entire_list)-1):
        min_index = x
        passnum = passnum + 1
        for y in range(x+1,len(entire_list)):
            if entire_list[min_index] > entire_list[y]:
                min_index = y
        switchnum = switchnum + 1
        temp = entire_list[x]
        entire_list[x] = entire_list[min_index]
        entire_list[min_index] = temp
    
    requirednums =[switchnum,passnum]
    return requirednums

def DisplayList(entire_list):
    """This function accepts a numeric list and then displays this list
    across the screen"""
    
    #entire_list - the list of integers existed in the unsorted text file
    
    for x in range(len(entire_list)):
        print(entire_list[x], end = "\t")
    print()

def CreateFile(entire_list,filename):
    """This function accepts a numeric list and a filename, then creates a
    new file with sorted numbers from the numeric list"""
    
    #entire_list - the list of integers existed in the unsorted text file
    #out_file - the file object associated with the sorted text file
    
    out_file = open(filename,"w")
    for x in range(len(entire_list)):
        out_file.write(str(entire_list[x])+"\n")
    out_file.close()
    
def main():
    """This is the mainline for the program"""
    
    #starttime - the time for the program to assemble the data
    #entire_list - the list of integers existed in the unsorted text file
    #requirednums - the list consists of switchnum and passnum
    #endtime - the total time for the program to assemble the data and analyze
    #          them
    
    entire_list = CreateNumericList(UNSORTED)
    starttime = time.time() 
    requirednums = SelectionSort(entire_list)
    endtime = time.time()
    DisplayList(entire_list)
    CreateFile(entire_list,SORTED)
    print()
    print("The number of switches required to sort the file is",requirednums[0])
    print("The number of passes required to sort the file is",requirednums[1])
    print("The actual time taken to sort the file is",endtime-starttime)
main()
    
    


            
    
    
