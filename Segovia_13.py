#NAME : KENNETH SEGOVIA
#DATE : 4/25/2021
#Assignment 13

#global vars
name = 'Kenneth Segovia '
data = '4/25/2021'
cla = 'CIS1400-NET '
asn = 'Assignment 13 '
smr = 'Menu Driven, Input Output, Loop, Modules'
emg = 'END OF FILE MESSAGE '
cm = ','
nl = '\n \n '
x=1#counter

#start of code

def RECC(testln):
    global x#allows use of global variable
    if(testln > 0):
        print('________________________________________')
        print('| ', x , ' | ', name, ' |')
        x=x+1#incrementer
        RECC(testln-1)#recursive
    x = 1 #resets counter for future loops
    if(x==testln):
        print(nl)
        XCC()


def XCC():
    print('MOD NAME FOR MENU XC')
    #options for menu
    print('Select from the following options')
    print('1. Print the data as many times as the input data collects.')
    print('2. exit')
    
    #validation
    choice = input("Choose menu option (1-2): ")
    while choice not in ['1', '2',]:
	    choice = input("Invalid choice.  Choose menu option (1-2): ")
    pas = int(choice)
    #selection
    if(pas==1):
        #number validation
        while True:
            ln = input('Enter number of times you would like to loop: ')
            try:
               testln = int(ln)
               break
            except ValueError:
               print('Not a number try again')
        #first line of output
        print('_______________________________')
        print('| Number | Name |')      
        RECC(testln) 
    
def hdr():#header function
    print(name,cm,data,cm,cla,cm,asn,nl)
    
def ftr():#footer function
    print(smr)
    
def eof():#end of file function
    print(emg,cm,name,data,asn,nl)

def main():#main function
    hdr()
    XCC()
    ftr()
    eof()
#calls main
main()
#end of code
