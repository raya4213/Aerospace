#!/usr/local/bin/python
import os
import sys
#os.path.realpath(os.path.dirname(sys.argv[0]))
#import os.path

if os.name == "nt":
   os_type = 1
else:
   os_type = 0
   
print " "
print " "
print "           *************************************************************************"
print "           ** Make sure to include the follwing files into your current directory **"
print "           **                      1. AmungoFx3Dumper.exe                         **"
print "           **                      2. AmungoItsFx3Firmware.img                    **"
print "           **                      3. nt1065.hex                                  **"
print "           *************************************************************************"

# check for the files to be present in the current dir
if os_type == 1:
   check = os.path.isfile("AmungoFx3Dumper.exe")
else:
   check = os.path.isfile("AmungoFx3Dumper")
if check == False:
   print "FileError: AmungoFx3Dumper not found"
   exit()

check = os.path.isfile("AmungoItsFx3Firmware.img")
if check == False:
   print "FileError: AmungoItsFx3Firmware.img not found"
   exit()

check = os.path.isfile("nt1065.hex")
if check == False:
   print "FileError: nt1065.hex not found"
   exit()

# user inout of seconds
print " "
input_sec= raw_input('Enter time in sec to log data:')

## error check to ensure input is an number (integer)
while True:
   try:
      val = int(input_sec)
      break
   except ValueError:
      print("That's not an int!")
      input_sec= raw_input('Enter your input:')
      
print type(input_sec)

# user can select the drivers to be either cypress or libusb

input_driver = raw_input("Enter 'c' for CYUSB/'l' for LIBUSB: ")
print input_driver
if input_driver == 'c' or 'C':
   input_driver = "cypress"
elif input_driver == 'l' or 'L':
   input_driver = "libusb"
else:
    print "Using the default drivers as CYUSB"
    input_driver = "cypress"

# constructing the string for running AmungoFx3Dumper.exe

if os_type == 1:
   # windows platform
   amungodumper_str = "AmungoFx3Dumper.exe"
else:
   #linux platform
   amungodumper_str = "AmungoFx3Dumper"
str_for_Amungo = amungodumper_str + " AmungoItsFx3Firmware.img nt1065.hex dump.bin" + " " + input_sec + " " + input_driver
os.system("@echo off")
#os.system("AmungoFx3Dumper.exe AmungoItsFx3Firmware.img nt1065.hex dump.bin 3600 cypress")
os.system(str_for_Amungo)
os.system("pause")
print "checking for continuity"
#os.system("a.exe")


