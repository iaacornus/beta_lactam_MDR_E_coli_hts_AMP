# draw the molecular structure using the
# canonical smiles fetched and rdkit
from rdkit import Chem
from rdkit.Chem import Draw

def reconstruct_mol(mol_, PATH) -> None:
    # mol_key in chembl_mol.keys():
    mol = Chem.MolFromSmiles(
            mol_["smiles"]
        )
    mol_drawn = Draw.MolDraw2DCairo(400, 400)
    mol_drawn.DrawMolecule(mol)
    mol_drawn.FinishDrawing()
    png_data = mol_drawn.GetDrawingText()
    mol_key = mol_["mol_id"]

    with open(
            f"./{PATH}/{mol_key}.png", "wb"
        ) as mol_png:
        mol_png.write(png_data)
