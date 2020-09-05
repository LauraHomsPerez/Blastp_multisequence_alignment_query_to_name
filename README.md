# Blastp_multisequence_alignment_query_to_name

## remove_repetitions

1. This python scirpt reads a fasta file named `fasta_input.txt` in the same directory as the Python file `Remove_repetitions.py`.
2. The Fasta file should have a sequence name, followed by the sequence in the text like in the following example
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
3. The script will read line by line, writing in the file `output_file_no_rep`. It will write only one of the each sequence's names.

    >A0A3N4A6A9.1/58-241 Glycoside hydrolase family 68 protein {ECO:0000313|EMBL:ROZ64321.1}    
    >***A0A3N4A6A9.1***/58-241 Glycoside hydrolase family 68 protein {ECO:0000313|EMBL:ROZ64321.1}
    
4.  ***How to use***
- Copy the Fasta format file in the same directory as the 'Remove_repetitions.py' script.
- Run the script
- A file called `output_file_no_Rep.txt` should appear in the same directory.


 ## query_remover
 
 1. This python script reads a stockholm format text file, generated by BlastP.
 2. The scripts reads each line, replacing `Query` with the actual sequence name.
 
 It changes this:
 ```
Query_18927  1    MAHVRRKVATLNMALAGSLLMVLGAQSALAQGN-FSRQEAARMAHRPGVMPRGGPL--FP  57
Query_18917  1    MVNIRQKKPVFRMVVAGSLIAALASQTAFAQSTPDARREALRVGPHPGMMPHAGRM--FP  58
Query_18795  2              LNLLLAGSMVATFTSQAAFAQLNPDALREAFRVAPRPGMMPHGAKL--YP  49
 ```
 
 to this:
 ```
Gluconacetobacter diazotrophicus (strain ATCC 49037 / DSM 5601 / PAl5)            1    MAHVRRKVATLNMALAGSLLMVLGAQSALAQGN-FSRQEAARMAHRPGVMPRGGPL--FP  57
Gluconacetobacter liquefaciens                                                    1    MVNIRQKKPVFRMVVAGSLIAALASQTAFAQSTPDARREALRVGPHPGMMPHAGRM--FP  58
Asaia platycodi SF2.                                                              2              LNLLLAGSMVATFTSQAAFAQLNPDALREAFRVAPRPGMMPHGAKL--YP  49
 ```
 
discarding all other lines in the file


3.  ***How to use***
- Copy the Stockholm format file in the same directory as the 'query_remover.py' script.
- Run the script
- A file called `output_file.txt` should appear in the same directory.




## Remove all sequences, that are not Levansucrase from the FASTA file

1. Open file with notepad++
2. Find and Replace (Ctrl-H)
3. Enable **Regex** with a tickbox.
4. Search for the following: ```^>(?!.*Levansucrase ).*$\r\n.*\r\n```

Explanation:
```
Levansucrase                       Literary matches Levansucrase
(.*Levansucrase)                   Matches anything before Levansucrase, including Levansucrase
(.*Levansucrase )                  Matches anything before Levansucrase, including Levansucrase and a space at the end
(?!.*Levansucrase )                Inverses the previous match (matches anything, but somethig-something-Levansucrase)
(?!.*Levansucrase ).*$             Matches any whole line that does not contain Levansucrase with a space at the end
^>(?!.*Levansucrase ).*$           Matches any whole line that starts with > and does not contain Levansucrase with a space at the end.
^>(?!.*Levansucrase ).*$\r\n.*     Matches anz whole line that starts with > ans does not contain Levansucrase with a space at the end, and a whole line after it.
^>(?!.*Levansucrase ).*$\r\n.*\r\n Matches anz whole line that starts with > ans does not contain Levansucrase with a space at the end, and a whole line after it and a line break after that.

```
