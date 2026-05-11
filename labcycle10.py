from Bio import PDB
import os

pdb_id = "1TUP"

pdbl = PDB.PDBList()
pdbl.retrieve_pdb_file(pdb_id, pdir=".", file_format="pdb")

filename = f"pdb{pdb_id.lower()}.ent"

parser = PDB.PDBParser(QUIET=True)
structure = parser.get_structure(pdb_id, filename)

model = structure[0]
chain = model['A']

print(f"Chain {chain.id}:")
for residue in chain:
    print(residue)

io = PDB.PDBIO()
io.set_structure(structure)
io.save("output.pdb")