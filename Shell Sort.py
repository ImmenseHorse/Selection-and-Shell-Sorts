#This program was written by Duc Nguyen on Dec 20, 2019.
#This program will create a file called "sorted.txt" containing the numbers from
#the "unsorted.txt" sorted from lowest to highest using Shell Sort.

import time

UNSORTED = "unsorted.txt"       #The unsorted text file
SORTED = "sorted.txt"           #The sorted text file        
INCREMENTS = "increment.txt"    #The increment text file

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
    
def ShellSort(numerics,increments):
    """This function accepts a numeric list and then sorts the integers in this
    list from lowest to highest"""
        
    #passnum - the number of passes required to sort the file
    #switchnum - the number of switches required to sort the file
    #numerics - the list of integers existed in the unsorted text file
    #increments - the list of integers existed in the increment text file
    #temp - the temporary variable storing the intergers
    #requirednums - the list consists of switchnum and passnum 
    #keepgoing - the flag for the while loop
    
    passnum = 0
    switchnum = 0
    
    for x in range(len(increments)):
        if increments[x] < len(numerics):
            keepgoing = True
            while keepgoing:
                keepgoing = False
                for y in range(len(numerics)-increments[x]):
                    if numerics[y] > numerics[y+increments[x]]: 
                        temp = numerics[y]
                        numerics[y] = numerics[y+increments[x]]
                        numerics[y+increments[x]] = temp
                        switchnum = switchnum + 1
                        keepgoing = True
                passnum = passnum + 1
            requirednums =[switchnum,passnum]
    return requirednums


def DisplayList(numerics):
    """This function accepts a numeric list and then displays this list
    across the screen"""
    
    #numerics - the list of integers existed in the unsorted text file
    
    for x in range(len(numerics)):
        print(numerics[x], end = "\t")
    print()

def CreateFile(numerics,filename):
    """This function accepts a numeric list and a filename, then creates a
    new file with sorted numbers from the numeric list"""
    
    #numerics - the list of integers existed in the unsorted text file
    #out_file - the file object associated with the sorted text file
    
    out_file = open(filename,"w")
    for x in range(len(numerics)):
        out_file.write(str(numerics[x])+"\n")
    out_file.close()
    
def main():
    """This is the mainline for the program"""
    
    #starttime - the time for the program to assemble the data
    #numerics - the list of integers existed in the unsorted text file
    #increments - the list of integers existed in the increment text file
    #requirednums - the list consists of switchnum and passnum
    #endtime - the total time for the program to assemble the data and analyze
    #          them
    
    numerics = CreateNumericList(UNSORTED)
    increments = CreateNumericList(INCREMENTS)
    starttime = time.time() 
    requirednums = ShellSort(numerics,increments)
    endtime = time.time()
    DisplayList(numerics)
    CreateFile(numerics,SORTED)
    print()
    print("The number of switches required to sort the file is",requirednums[0])
    print("The number of passes required to sort the file is",requirednums[1])
    print("The actual time taken to sort the file is",endtime-starttime)
main()

    
    


            
    
    
