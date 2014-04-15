#1.this fuction receives a path to a file as a string, reads a fasta file witht a single DNA sequence and returns a tuple with the id and the sequence.
def readfasta(fp):
#two output are expected, being name and sequence
    name = ""
    sequence = ""
    tmp = []
    for line in fp:
        line=line.rstrip()
        if line.startswith(">"):
             #temporary file
            tmp.append(name)# appent values in tmp and concatenate   them wiht variable name
            tmp.append(sequence)#append and concatenate value in variable sequence
            name,sequence = line, []
            
        
    else:
        sequence = sequence.append(line)
           
        return tmp



#fp=open("dna.fasta","r")

#readfasta(fp)
