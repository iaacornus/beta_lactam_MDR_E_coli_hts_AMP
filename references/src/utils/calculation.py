import numpy as np
import pandas as pd
from rdkit import Chem
from rdkit.Chem import Descriptors, Lipinski, Mol


def elemental_composition(smiles) -> list[Mol]:
    elemental_comp__: list[Mol] = []

    for elem in smiles:
        mol_: Mol = Chem.MolFromSmiles(elem)
        elemental_comp__.append(mol_)

    return elemental_comp__


def calc_lipinski(smiles) -> pd.DataFrame:
    """ calculates the lipinski descriptor of molecules
    given its smiles.

    """

    descriptors__ = np.arange(1, 1)

    for index, mol__ in enumerate(
            elemental_composition(smiles)
        ):
        desc_mol_wt = Descriptors.MolWt(mol__)
        desc_mol_log_p = Descriptors.MolLogP(mol__)
        desc_num_h_don = Lipinski.NumHDonors(mol__)
        desc_num_h_acc = Lipinski.NumHAcceptors(mol__)

        calc_desc = np.array(
                [
                    desc_mol_wt,
                    desc_mol_log_p,
                    desc_num_h_don,
                    desc_num_h_acc
                ]
            )

        if index == 0:
            descriptors__ = calc_desc
        else:
            descriptors__ = np.vstack(
                    [
                        descriptors__,
                        calc_desc
                    ]
                )

    descriptors = pd.DataFrame(
            columns=["MW", "logP", "nhd", "nha"],
            data=descriptors__
        )

    return descriptors
