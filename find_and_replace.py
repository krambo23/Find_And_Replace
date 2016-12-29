import sys

file_name = str(sys.argv[1])
new_file = str(sys.argv[2])

# Get string to be replaced
str_search = input("Find : ")
str_replace = input("Replace : ")

# Get file encoding type
encoding_type = input("Input Encoding [Leave blank if UTF-8] : ")
if encoding_type == "" :
	encoding_type = "utf-8"

# Reads file and replaces string
file_read = open(file_name, "r", encoding = encoding_type, errors = "ignore").read() # Opening,reading and closing "file_name" in r mode
# NOTE : '.read()' reads the file and closes it automatically 

if file_read.find(str_search) == -1 :
	print("Not found")
	sys.exit() # Kills program
else :
	file_out = file_read.replace(str_search, str_replace) # Replaces string

# Writes to merged file
file_write = open(new_file, "w", encoding = encoding_type, errors = "ignore") # Opening new_file in w mode
file_write.write(file_out) # Writes into merge_output the contents of "file_out"
file_write.close() # Closes file_write

print("Operation Complete ;-)")