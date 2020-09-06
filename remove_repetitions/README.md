# Retrieve Source organism by Accession number from Pfam


## This function opens the pfam website and find the source organism for an accession number and returns it.
1. This python scirpt reads a fasta file named `output_file_no_rep.txt` in the same directory as the Python file `Rename_acc_num_source_org.py`.
2. This Fasta file contains all protein sequences from GH68 family of bacteria dowloaded from PFAM (https://pfam.xfam.org/family/PF02435#tabview=tab7.
3. Prior to that, the file contained repetitions of sequences that have been removed (SEE remove_repetitions.py).
4. The Fasta file should contain the Accession Name followed by the sequence in the text like in the following example:

```
>A0A3M8AKQ8.1/53-513 Glycoside hydrolase family 68 protein {ECO:0000313|EMBL:RNB51771.1}
    MSTSTRRMRRPLVGGITAAGVLVGTLFTGTAAAVAQPDLQPGAEPTVHTQQAYAPEDDFTAKWTRADAKQLQRLSDPNAASRENSMPA
    >A0A3N4A6A9.1/58-241 Glycoside hydrolase family 68 protein {ECO:0000313|EMBL:ROZ64321.1}
    MPEDSNLADRQISRRSFGRLAAAVTAAATLTSVSYRTDKAWAAEGPQPTPHTQQAYDPISSDFAAKWTRADARQIMTQQNDESVPRGE
    >A0A3S1DAP8.1/37-483 Glycoside hydrolase family 68 protein {ECO:0000313|EMBL:RUT33589.1}
    MNIRKFVRRAAAVTFTTALIAGGGTSAFAKEKDSQDYKESYGFSHITRSDMLKIPGQQLSQQFQAPSFDASTIKNIPSAKGVDQWGNPI
    >A0A437SU42.1/117-568 Levansucrase {ECO:0000313|EMBL:RVU70410.1}
    MHNSKKHSMLTLVSAGVLLGILNTANCKPVHADTLNSPTTNTNNVQNQNTTDQTQNFSSNDSASVTNADQTSDSTQTSTQASDLQLTDE
    >B0RBJ8.1/47-509 Sugar hydrolase {ECO:0000313|EMBL:CAQ02894.1}
    MTKRIRRGLSASAAATLVVASALLAGGSAQAAGTTPPRPTVHTQEAYAPEDDFTAHWTRADAKQIAKLSDPTAAPRQNSMPEALTMPQV
    >A0A024PB57.1/37-486 Levansucrase {ECO:0000313|EMBL:CDQ25652.1}
    MNLKLLAKKATILTLSTAILAGGSGLVHAEQKAHEDTKEDYGISHITRADMEAMAKQHGNDNFEVPKFDASTIQNIPSATKVTENGEEI

```
5. The function opens PFAM at the ACCESSION NUMBER site of an organism. 

```
import requests

def pool_pfam_website(var_accnum):                      
    url = 'https://pfam.xfam.org/protein/' + var_accnum                                         # What website to download (where var_accnum is the accession number)
    r = requests.get(url)                                                                       # Dowloads the website to a string, only one line. 
    var_loct1 = r.text.find("organism")                                                         # Searches for the location of the the word "organism"                
    var_loc2 = r.text.find(" " * 16,var_loct1)                                                  # Searches for the location of 16 spaces after the word organism (this is where the source organism starts)
    var_loc3 = r.text.find("</a>",var_loc2)                                                     # Searches for the locaition of "</a>" after those 16 spaces (this is where the name ends).
    return r.text[var_loc2+16:var_loc3]                                                         # Gets the source organism name and returns it. 


```
6. It reads the ACCESSION NUMBER from the FASTA file dowloaded from PFAM, searches it on the website, gives the SOURCE ORGANISM corresponding and writes it down in an output file
named `output_file_source_organism_names.txt`.

```
input_file = open("output_file_no_rep.txt","r")                                                 # Open the file and read it
line_in_file = input_file.readlines()                                                           # Reads line in file
output_file_source_organism_names = open("output_file_source_organism_names.txt", "w")          # Name the output file called "output_file_source_organism_names.txt", that will contain the FASTA file from PFAM with all the Source Organism names in it.

for line in line_in_file:                                                                       # Read only lines containing ">".
    if line.startswith('>'):
        var_accession_number=line[line.find(">")+1:line.find(".")+2]                            # Define Accession Number variable. Find accession number in PFAM website with function ".find" in line and cut it out or subset it with function [] from line. 
        var_source_organism= pool_pfam_website(var_accession_number)                            # Define Source Organism variable. Use function created before to search for it in PFAM website.  
        var_output_line=">" + var_source_organism + "_" + line[1:]                              # Define output line. Output line contains ">" "source organism" "_" and the rest of the line. 
        output_file_source_organism_names.write(var_output_line)                                # Write it down in the output file names "output_file_source_organism_names".
        print(var_output_line)
        
    else:
        output_file_source_organism_names.write(line)                                           # If line does not start with ">" (line containing protein sequences), write it down in the output file (the program will write it just below of each ">" line. 
        print(line)
    
input_file.close()                                                                               # Close input file.
output_file_source_organism_names.close()                                                        # Close output file.

```
