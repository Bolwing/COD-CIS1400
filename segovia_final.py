#NAME : KENNETH SEGOVIA
#DATE : 05/10/2021
#Final Exam

#global vars
name = 'Kenneth Segovia '
data = '05/10/2021'
cla = 'CIS1400-NET '
asn = 'Final Exam '
smr = 'Menu Driven, Input Output, Loop, Modules, Random, If Statements, Random, IS Commands'
emg = 'END OF FILE MESSAGE '
cm = ','
nl = '\n \n '
arr = [0] * 5#the array

import random

def hdr():#header function
    print(name,cm,data,cm,cla,cm,asn,nl)
    
def ftr():#footer function
    print(smr)
    
def eof():#end of file function
    print(emg,cm,name,data,asn,nl)

def Mennu():
    global arr
    #required for menu
    print('*****Final Exam Test Method Menu*****')
    print('1. Build the Array with a Random Number, 5 points.')
    print('2. Print the Array unsorted, to the display, 5 points.')
    print('3. Sort the Array in ascending order, 5 points.')
    print('4. Print the Array to the display and to a file named "PFILEA". [PFILEA.txt]. 10 points.')
    print('5. Sort the Array in descending order, 5 points.')
    print('6. Print the Array in descending order and to a file named "PFILED". [PFILED.txt]. 10 points.')
    print('7. Exit the Menu/Program. 5 points.')
    print(nl)

    #all is tests
    choice = input("Choose menu option (1-7): ")
    print('IS ALPHANUMERIC TEST: ', choice.isalnum())
    print('IS ALPHA TEST: ', choice.isalpha())
    print('IS LOWERCASE: ', choice.islower())
    print('IS UPPERCASE: ', choice.isupper())
    print('IS SPACE: ', choice.isspace())
    print('IS DIGIT: ', choice.isdigit())
    print(nl)

    #input validation
    while choice not in ['1', '2','3','4','5','6','7']:
	    choice = input("Invalid choice.  Choose menu option (1-7): ")
    pas = int(choice)

    #options for menu
    if(pas==1):
        Randy()
    elif(pas==2):
        ShowA()
    elif(pas==3):
        SortA()
    elif(pas==4):
        popA()
    elif(pas==5):
        SortD()
    elif(pas==6):
        popD()
    

def Randy():#builds array with random numbers
    global arr#access array
    for x in range(5):#assigns random variable to locations in array
        arr[x] = random.randint(0,10)
    Mennu()#return to menu
    
def SortA():#sorts array ascending order
    global arr#access array
    arr.sort()#array is placed in ascending order
    Mennu()#return to menu

def SortD():#sorts array descending order
    global arr#access array
    arr.sort(reverse=True)#array is placed in descending order
    Mennu()

def ShowA():#displays array after unsorted/sorted action
    print(arr)
    Mennu()#return to menu

def popA():
    global arr#access array
    arr.sort()#sorts array for required action
    print(arr)#prints array
    PFILEA = open('PFILEA.txt','w')#opens PFILEA
    #assigns index in array to a string for file
    n1=str(arr[0])
    n2=str(arr[1])
    n3=str(arr[2])
    n4=str(arr[3])
    n5=str(arr[4])
    #writes each index to a line in file
    PFILEA.write(n1 + '\n')
    PFILEA.write(n2 + '\n')
    PFILEA.write(n3 + '\n')
    PFILEA.write(n4 + '\n')
    PFILEA.write(n5 + '\n')

    PFILEA.close()#closes PFILEA
    print('action complete')
    Mennu()#return to menu

def popD():
    global arr#access array
    arr.sort(reverse=True)#sorts array for required action
    print(arr)#prints array
    PFILED = open('PFILED.txt','w')#opens PFILED
    #assigns index in array to a string for file
    n1=str(arr[0])
    n2=str(arr[1])
    n3=str(arr[2])
    n4=str(arr[3])
    n5=str(arr[4])
    #writes each index to a line in file
    PFILED.write(n1 + '\n')
    PFILED.write(n2 + '\n')
    PFILED.write(n3 + '\n')
    PFILED.write(n4 + '\n')
    PFILED.write(n5 + '\n')

    PFILED.close()#closes PFILED
    print('action complete')
    Mennu()#return to menu
    
def main():#main function
    hdr()
    Mennu()
    ftr()
    eof()

main()#calls main

#end of code
#have a great summer
