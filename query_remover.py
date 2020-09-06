
input("Press Enter to continue or Ctrl-z to stop")




input_file = open("input.txt","r")                             # Open the file and read it
line_in_file = input_file.readlines()                          # To read each the whole file line by line
dictionary_names={}                                            # Creating an empty dictionary
output_file = open("output_file.txt", "w")

for line in line_in_file: 
    if line.startswith('Subject'):                             # Reading only lines that start with "Subject"
        
        #print(line.find(":")+1)                               # Find the location of ":" on the current line. Because o for loop, we'll get all of them.
        #print(line.find("_"))                                 # Find the location of "_"
        #print( line[line.find(":")+1:line.find("_")] )        # Cuts the line between characters ":" and "_". The name of the bacteria
        #print(line[line.find("Query"):line.find("Length")-1]) # Cuts the Query name
        dictionary_names[line[line.find("Query"):line.find("Length")-1]] = line[line.find(":")+1:line.find("_")]  # Adding Query num and bacteria names to dictionary
        
for line in line_in_file: 
    if line.startswith('Query_'):
       # print(line[0:line.find(" ")])
       # print (dictionary_names[line[0:line.find(" ")]] , end =" ") 
       # print (line[line.find(" "):])

        var_current_name=dictionary_names[line[0:line.find(" ")]]
        var_len_name=len(var_current_name)
  
        
        output_file.write(var_current_name) 
        output_file.write(" " * (120 - var_len_name))
        output_file.write(line[line.find(" ")+2:])
        #output_file.write("\n")
        
        
        
        
input_file.close()
output_file.close()

input("Press Enter to exit")
