import numpy as np

from pydftd3 import DFTD3Library


Elements = ["None", 'H', 'He',
            'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne',
            'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar',
            'K', 'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr',
            'Rb', 'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I', 'Xe',
            'Cs', 'Ba', 'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb',
            'Lu', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi']


# DFTB3 D3(BJ) parameters
parameters = {
    "s6": 1.0,
    "rs6": 0.5719,
    "s18": 0.5883,
    "rs18": 3.6017,
    "alp": 14.0,
}

version = 4


def test_dftd3_calculation(xyz, out):
    natoms = np.loadtxt(xyz, dtype=int, max_rows=1)
    positions = np.loadtxt(xyz, usecols=(1, 2, 3), skiprows=2, max_rows=natoms).T / 0.52917726

    elements = np.loadtxt(xyz, dtype="U2", usecols=0, skiprows=2, max_rows=natoms)
    numbers = np.zeros(natoms, dtype=np.int32)
    for i, e in enumerate(elements):
        numbers[i] = Elements.index(e)

    lib = DFTD3Library()

    ene, grad = lib.DFTD3Calculation(natoms, positions, numbers, parameters, version)

    ene_ref = np.loadtxt(out, max_rows=1)
    grad_ref = np.loadtxt(out, skiprows=1, max_rows=natoms).T

    np.testing.assert_allclose(ene, ene_ref, atol=1e-8)
    np.testing.assert_allclose(grad, grad_ref, atol=1e-8)


if __name__ == "__main__":
    test_dftd3_calculation("dna.xyz", "dna.out")
