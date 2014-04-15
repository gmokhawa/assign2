#6.this fuction receives a sequence(string) and an ID(string) and creates a string in fasta format where the ID is the content of the first line and the sequence is split into line of maximum 60 characters.

def get_fasta():

    lines=[]
    for i in seq:
        print i
        for i in range(0,len(seq),60):
            #lines=(i.seq[i:i+60]#, '\n'
            lines.append(seq[i:i+60])

        return '\n'.join(lines)
       
    







get_fasta()
seq =raw_input("enter file ")
print get_fasta()
