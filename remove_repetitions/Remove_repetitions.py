input("Press Enter to continue or Ctrl-z to stop")

input_file = open("fasta_input.txt","r")                                   # Open the file and read it
line_in_file = input_file.readlines()                                 # To read each the whole file line by line
var_flag=0                                                            # Set the var_flag to 0
                                            
output_file_no_rep = open("output_file_no_rep.txt", "w")              # Creating an empty file
list_a_num = []                                                       # Creating an empty dictionary

for line in line_in_file: 
    
    if var_flag==1:                                                  # This section prints the protein sequences that are below the line that starts with <. How does it do it? In the first loop, since we have set var_flag to 0, the "if var_flag==1" will not print or write anything. Then, the next "if line startswith ">" and it is not duplicated, will print the line and it will set the var_flag to 1, which indicates that the next line should be printed in the next cycle of the for loop. After this second line is printed, we set the var_flag to 0 again, restarting the whole process. 
        print(line)
        output_file_no_rep.write(line) 
        var_flag=0
    
    if line.startswith('>'):                                          # Reading only lines that start with ">""
        var_accession_number=line[line.find(">")+1:line.find(".")+2]  # Creating a variable that contains only the Accession Number
        if var_accession_number not in list_a_num:                    # If the Accession Number is not in the list, put it  
            list_a_num.append(var_accession_number)
            output_file_no_rep.write(line) 
            print (line)
            var_flag=1    

input_file.close()
output_file_no_rep.close()
input("Press Enter to exit")            