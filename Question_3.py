#get_ORF function-this function receives a DNA sequence as a string and returns the first open reading frame (0,1 or 2)where both start and stop codons are present; or -1 if it can't be forund, making sure that the start codon appears fir

def
    fasta="ATTATGCCCTTGCG"
    index=0

    while index!=-1:
        for i in range(0,len(fasta),3):

            if fasta[i:i+3]=="ATG":
                start_codon=i
                print "start codon index: ", start_codon

        if fasta[i:i+3]=="TAA" or fasta[i:i+3]=="TAG" or fasta[i:i+3]=="TGA":
                stop_codon=i
                print "stop codon index: ", stop_codon


    index=index+1

