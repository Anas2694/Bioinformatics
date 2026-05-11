from Bio import Entrez, SeqIO, AlignIO, Phylo
from Bio.Align import PairwiseAligner
from Bio.Phylo.TreeConstruction import DistanceCalculator, DistanceTreeConstructor
import matplotlib.pyplot as plt

# -----------------------------
# STEP 1: Fetch MSTN sequence (Human)
# -----------------------------
Entrez.email = "your_email@example.com"  # IMPORTANT

print("Fetching Human MSTN sequence from NCBI...")

handle = Entrez.efetch(
    db="protein",
    id="NP_005250",   # Human MSTN
    rettype="fasta"
)

record = SeqIO.read(handle, "fasta")
handle.close()

print("\nSequence Details:")
print("ID:", record.id)
print("Description:", record.description)
print("Length:", len(record.seq))
print("First 50 amino acids:", record.seq[:50])

# -----------------------------
# STEP 2: Pairwise Alignment (NEW METHOD)
# -----------------------------
print("\nPerforming Pairwise Alignment...")

# For demo: comparing same sequence (you can replace with another species)
seq1 = str(record.seq[:200])
seq2 = str(record.seq[:200])

aligner = PairwiseAligner()
score = aligner.score(seq1, seq2)

similarity = (score / len(seq1)) * 100

print(f"Alignment Score: {score}")
print(f"Similarity: {similarity:.2f}%")

# -----------------------------
# STEP 3: Create Multiple Sequence File
# -----------------------------
print("\nCreating Multi-species FASTA file...")

sequences = {
    "Human": "MDHQRKDFGLCDGDWKGKGKDYGKGNKDYGWDDGMQ",
    "Mouse": "MDHQRKDFGLCDGDWKGKGKDYGKGNKDYGWDDGMQ",
    "Cow":   "MDHQRKDFGLCDGDWKGKGKDYGKGNKDYGWDDGMQ"
}

with open("mstn.fasta", "w") as f:
    for name, seq in sequences.items():
        f.write(f">{name}\n{seq}\n")

print("FASTA file created successfully!")

# -----------------------------
# STEP 4: Phylogenetic Tree
# -----------------------------
print("\nConstructing Phylogenetic Tree...")

alignment = AlignIO.read("mstn.fasta", "fasta")

calculator = DistanceCalculator('identity')
distance_matrix = calculator.get_distance(alignment)

print("\nDistance Matrix:")
print(distance_matrix)

constructor = DistanceTreeConstructor()
tree = constructor.upgma(distance_matrix)

print("\nPhylogenetic Tree (Newick format):")
print(tree.format("newick"))

# -----------------------------
# STEP 5: Visualization
# -----------------------------
plt.figure(figsize=(8, 5))
Phylo.draw(tree)
plt.title("MSTN Phylogenetic Tree")
plt.show()

print("\n✅ Program executed successfully!")