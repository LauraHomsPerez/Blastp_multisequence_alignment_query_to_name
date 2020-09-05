import requests

# This function opens the pfam website and find the source organism for an accession number and returns it.
def pool_pfam_website(var_accnum):                      
    url = 'https://pfam.xfam.org/protein/' + var_accnum     # What website to download (where var_accnum is the accession number)
    r = requests.get(url)                                   # Dowloads the website to a string, only one line. 
    var_loct1 = r.text.find("organism")                     # Searches for the location of the the word "organism"                
    var_loc2 = r.text.find(" " * 16,var_loct1)              # Searches for the location of 16 spaces after the word organism (this is where the source organism starts)
    var_loc3 = r.text.find("</a>",var_loc2)                 # Searches for the locaition of "</a>" after those 16 spaces (this is where the name ends).
    return r.text[var_loc2+16:var_loc3]                     # Gets the source organism name and returns it. 


#print (pool_pfam_website("V6KQL7.1"))


input_file = open("output_file_no_rep.txt","r")             # Open the file and read it
line_in_file = input_file.readlines()   
output_file_source_organism_names = open("output_file_source_organism_names.txt", "w")

for line in line_in_file: 
    if line.startswith('>'):
        var_accession_number=line[line.find(">")+1:line.find(".")+2]
        var_source_organism= pool_pfam_website(var_accession_number)      
        var_output_line=">" + var_source_organism + "_" + line[1:]
        output_file_source_organism_names.write(var_output_line)
        print(var_output_line)
        
    else:
        output_file_source_organism_names.write(line) 
        print(line)
    
input_file.close()
output_file_source_organism_names.close() 