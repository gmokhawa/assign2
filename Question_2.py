#Python Assignment 2 From Gaone Gee Mokhawa Student Number 14M8501
#2this function displays the reverse compliment of a DNA sequence (Eg.if user inputs "ATTATGCCCTTGCG" the program prints "CGCAAGGGCATAAT")

def reverse_copliment(x):
#DNA_sequence=raw_input("enter seq: ")
    reverse_sequence=DNA_sequence[::-1]
    reverse_compliment_Atot=reverse_sequence.replace("A","t")
    reverse_compliment_TtoA=reverse_compliment_Atot.replace("T","A")
    reverse_compliment_Gtoc=reverse_compliment_TtoA.replace("G","c")
    reverse_compliment_CtoG=reverse_compliment_Gtoc.replace("C","G")
    reverse_compliment_ttoT=reverse_compliment_CtoG.replace("t","T")
    reverse_compliment_ctoC=reverse_compliment_ttoT.replace("c","C")
    reverse_compliment=reverse_compliment_ctoC



    return reverse_compliment
