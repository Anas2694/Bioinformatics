from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO

dna_sequence = Seq("ATGCGTACGTAGCTAGCTAG")

record = SeqRecord(
    dna_sequence,
    id = "seq1",
    name="Example_Gene",
    description="Example gene sequence",
    annotations={
        "molecule_type": "DNA",
        "gene": "ExmpleGene",
        "function": "Hypothetical protein"
    }
)

output_file_path = "genbank.gb"

with open(output_file_path, "w") as output_file:
    SeqIO.write(record, output_file, "genbank")
print("Genbank file written succesfully.")

with open(output_file_path, "r") as input_file:
    record_read = SeqIO.read(input_file, "genbank")
    print("\nContents of genabank file")
    print(record_read)

