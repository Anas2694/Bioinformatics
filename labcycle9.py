from Bio import AlignIO
from Bio import Phylo
from Bio.Phylo.TreeConstruction import DistanceCalculator, DistanceTreeConstructor

try:
    alignment = AlignIO.read("aligned_sequences.fasta", "fasta")

    calculator = DistanceCalculator('identity')
    distance_matrix = calculator.get_distance(alignment)

    constructor = DistanceTreeConstructor()
    tree = constructor.upgma(distance_matrix)

    print("Phylogenetic Tree Structure:")
    print(tree)

    Phylo.draw(tree)

except FileNotFoundError:
    print("Error: 'aligned_sequences.fasta' not found. Run the MUSCLE alignment script first.")
except Exception as e:
    print(f"An error occurred: {e}")