from Bio.Seq import Seq
#Create DNA Sequence
dna_sequence=Seq("ATGCTAGCTAGCTAGCTG")
#DNA Slicing 
sliced_sequence=dna_sequence[3:11]
print("Sliced Seq",sliced_sequence)
another_sequence=Seq("GGCTAG")
#DNA Sequence Concatenation
concatenated_sequence=sliced_sequence+another_sequence
print("Concatenzted_seq",concatenated_sequence)
#Trancribe the concatenated sequence into RNA
rna_sequence = concatenated_sequence.transcribe()
print("RNA Sequence: ", rna_sequence)
#Trancslate the rna sequence into protein
protein_sequence=rna_sequence.translate()
print("Protein Sequence: ",protein_sequence)