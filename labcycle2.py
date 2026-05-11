from Bio import SeqIO

def read_fasta(fasta_file):
    for record in SeqIO.parse(fasta_file,"fasta"):
        print(f"Description :{record.description}")
        print(f"Sequence :{record.seq}")
        print("-----------------------")

fasta_file="fasta_1.fasta"
read_fasta(fasta_file)