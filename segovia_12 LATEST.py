
#NAME : KENNETH SEGOVIA
#DATE : 4/02/2021
#Assignment 10

#global vars
name = 'Kenneth Segovia '
data = '4/10/2021'
cla = 'CIS1400-NET '
asn = 'Assignment 11 '
smr = 'Menu Driven, Array, Input Output, Sort, Loop'
emg = 'END OF FILE MESSAGE '
cm = ','
nl = '\n \n '



#start of code

    
def ISN():
    print('Tests if input is Alphanumeric')
    data = input('PUT IN WHAT YOU WANT TO TEST: ')
    if data.isalnum():
        print('TRUE')
    else:
        print('FALSE')
    XCC()

def ISP():
    print('isalpha')
    data = input('PUT IN WHAT YOU WANT TO TEST: ')
    if data.isalpha():
        print('TRUE')
    else:
        print('FALSE')
    XCC()

def ISD():
    print('isdigit')
    data = input('PUT IN WHAT YOU WANT TO TEST: ')
    if data.isdigit():
        print('TRUE')
    else:
        print('FALSE')

    XCC()

def ISL():
    print('islower')
    data = input('PUT IN WHAT YOU WANT TO TEST')
    if data.islower():
        print('TRUE')
    else:
        print('FALSE')

    XCC()

def ISS():
    print('isspace')
    data = input('PUT IN WHAT YOU WANT TO TEST')
    if data.isspace():
        print('TRUE')
    else:
        print('FALSE')

    XCC()

def ISU():
    print('ispuper')
    data = input('PUT IN WHAT YOU WANT TO TEST')
    if data.isupper():
        print('TRUE')
    else:
        print('FALSE')
    XCC()





def XCC():
    print('MOD NAME FOR MENU XC')
    #options for menu
    print('Select from the following options')
    print('1. ISALNUM')
    print('2. ISALPHA')
    print('3. ISDIGIT')
    print('4. ISLOWER')
    print('5. ISSPACE')
    print('6. ISUPPER')
    print('7. EXIT')

    
    #first input recieved
    sel = int(input('Enter Selection 1, 2, 3, 4, 5, 6, 7 : '))

    #validation
    if(sel > 7 or sel < 1):
        print('That is not a valid option')
        sel = int(input('Enter 1, 2, 3, 4, 5, 6, 7'))

    #options
    if(sel == 1):
        ISN()
    elif(sel == 2):
        ISP()
    elif(sel == 3):
        ISD()
    elif(sel == 4):
        ISL()
    elif(sel == 5):
        ISS()
    elif(sel == 6):
        ISU()

    
    

def hdr():#header function
    print(name,cm,data,cm,cla,cm,asn,nl)
    
def ftr():#footer function
    print(smr)
    
def eof():#end of file function
    print(emg,cm,name,data,asn,nl)

def main():
    hdr()
    XCC()
    ftr()
    eof()

main()
    
