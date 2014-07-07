# File: reshape.py
# By  : Reed S
# Date: 22 May 2014
# Rev : N/A
# Desc: 
'''
	This is the reshaping code for the Sinclair Data following Tuan's code. 
	
	It requires and input file and will output two files.
	
		full_conversion.csv:
			This file has all the reshaped data with every 
			serial number available.

		filtered_conversion.csv:
			This file has all the reshaped data after deleting
			the serial numbers listed in: 
				in_delete_serial_name(name)

	In order to change the serial names outputed,
		goto the "serial_names" list, and add serial names or change
		serial names. You can also add more serial numbers.
		The syntax is (follow the pattern):
			<"serial_number":"serial_name",>
		Note: that if there is no serial_name defined, the 
		serial_number will be used.

	In order to delete the serial names outputed,
		goto "in_delete_serial_name(name)", and add or change
		the serial numbers.  
		The syntax is (follow the pattern):
			<"serial_number",>
			
'''



# import libraries
import datetime as dt
import csv
import sys
import os


# open the input and output files
try:
    input_filename = sys.argv[1]
except:
    print "Please use appropriate syntax."
    print '>>>"python reshape.py <file_name>"'
    quit()
output_filename = "full_conversion.csv"

# setup the reader
try:
    input_file = open(input_filename, "r")
    reader = csv.reader(input_file, delimiter = ",")
except:
    print "File not found."
    quit()
    
#os.system("cls")

# This will store the names for the serial numbers
# adding serial numbers that are not in data will not
# cause errors
serial_names = {}
# define functions
# this determines the serial numbers that are not needed
# adding serial numbers that are not in data will not 
# cause errors
def in_delete_serial_name(name):
    delete_serial_name = ()
        
    for i in range(0, len(delete_serial_name)):
        if(name == delete_serial_name[i]):
            return True
    return False


# notice to begin code    
print "Processing... Please Wait"
    
# setup the writer
output_file = open(output_filename, "wb")
writer = csv.writer(output_file,delimiter = ",")

# find the row for the header
input_row = reader.next()
input_row = reader.next()

sensors = []

# find the sensor names
sensors = input_row[2:]
for i in range(0, len(sensors)):
    try:
        sensors[i] = serial_names[sensors[i].split(",")[2].split(" ")[-1].replace(")","")]
    except:
        sensors[i] = sensors[i].split(",")[2].split(" ")[-1].replace(")","")

# find the row with data
output_row = []

for input_row in reader:
    for i in range(2, len(input_row)):
        output_row = []        
	datetime_ = dt.datetime.strptime(input_row[1],'%m/%d/%y %H:%M:%S %p')
        output_row.append(datetime_)
        output_row.append(sensors[i-2])
        output_row.append(input_row[i])
        writer.writerow(output_row)
        del output_row[:]

input_file.close()
output_file.close()

# notice for complete full conversion
print "Finished full conversion."


print "Processing... Please wait"
# setup the writer
input_file = open("full_conversion.csv", "r")
reader = csv.reader(input_file, delimiter = ",")
output_file = open("filtered_conversion.csv", "wb")
writer = csv.writer(output_file, delimiter = ",")

# write to the file
for input_row in reader:
    if in_delete_serial_name(input_row[1]) == False:
        writer.writerow(input_row)
                

input_file.close()
output_file.close()

print "Finished filtered conversion"
quit()