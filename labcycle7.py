from Bio.Align import PairwiseAligner
seq1 = "AGTACACTGGT"
seq2 = "AGTACGCTGGT"
aligner = PairwiseAligner()
alignment = aligner.align(seq1, seq2)
print("Aligned Sequences:")
print(alignment[0])
print(f"Alignment Score: {alignment[0].score}")