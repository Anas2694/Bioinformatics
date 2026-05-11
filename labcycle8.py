import subprocess
from Bio import AlignIO

seqs = """>seq1
ATGCGTACGTA
>seq2
ATGCGTACGTC
>seq3
ATGCGTACGAG
"""

input_file = "input_sequences.fasta"
output_file = "output_sequences.fasta"

with open(input_file, "w") as f:
    f.write(seqs)
muslce_path="muslce.exe"
try:
    subprocess.run(["muscle", "-in", input_file, "-out", output_file], 
                   check=True, 
                   stdout=subprocess.PIPE, 
                   stderr=subprocess.PIPE)

    alignment = AlignIO.read(output_file, "fasta")
    print(alignment)

except subprocess.CalledProcessError as e:
    print(e.stderr.decode())
except FileNotFoundError:
    print("MUSCLE executable not found.")