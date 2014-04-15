def get_gene_by_orf(fasta):

    index=0
    start_codon=0
    stop_codon=0
    gene=0
    ORF=''
    for i in range(0, len(fasta),3):
    
        if fasta[i:i+3]=="ATG":
            start_codon+=i
            print "start codon index is: ", start_codon

        if fasta[i:i+3]=="TAA" or fasta[i:i+3]=="TAG" or fasta[i:i    +3]=="TGA":
            stop_codon+=i
            print "stop codon index is: ",stop_codon
          

    ORF=fasta[start_codon:stop_codon+3]

    return ORF
        


   
    index=index+1



get_gene_by_orf(fasta)
match="ATTATGCCCTAGCG"
print get_gene_by_orf(match)


