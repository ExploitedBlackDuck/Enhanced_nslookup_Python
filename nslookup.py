#!/usr/bin/python3

import socket 


#this module is core networking module in Python, 
#can be used to resolve IP address.

sourcefile = 'sourcefile.txt' #file with IP address
outfile = 'results.txt' #file to write the IP addresses

with open(sourcefile, 'r') as inputf: 
    #This opens the sourcefile in read mode to see what are the domains


    with open(outfile, 'a') as outputf: 
        #This opens the outfile in append mode to write the results


        addresses = inputf.readlines() 
        #This reads all the IP addresses in sourcefile line by line


        for address in addresses: 
            #This for loop will go one by one on addresses.


            address = address.strip("\n") 
                #as the every address in the file are in newline,
                #the socket function will have trouble, so strip off the newline char


            try:
                resolution = (socket.gethostbyaddr(address))
                print(address, resolution[0])
                outputf.write(address + "," + resolution[0] + "\n")
            except:
                outputf.write(address + ",Unknown\n")
                print('Could not resolve ' + address)
                 