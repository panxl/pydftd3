from pathlib import Path
from ctypes import POINTER, c_int, c_double

import numpy as np


class DFTD3Library(object):
    def __init__(self):
        self.library = np.ctypeslib.load_library('libdftd3', Path(__file__).parent)

        self.library.dftd3_dispersion.argtypes = [
            POINTER(c_int),
            np.ctypeslib.ndpointer(np.float64, ndim=2, flags="F"),
            np.ctypeslib.ndpointer(np.int32, ndim=1),
            np.ctypeslib.ndpointer(np.float64, ndim=1, shape=5),
            POINTER(c_int),
            POINTER(c_double),
            np.ctypeslib.ndpointer(np.float64, ndim=2, flags="F"),
        ]
 
        self.library.dftd3_dispersion.restypes = None

    def DFTD3Calculation(self, natoms, positions, numbers, parameters):

        _parameters = {
            "s6": 1.,
            "rs6": 0.,
            "s18": 0.,
            "rs18": 0.,
            "alp": 14.,
            "version": 4,
        }
 
        _parameters.update(parameters)
        version = _parameters.pop("version")

        position = np.asarray(positions, order="F")
        _parameters = np.fromiter(_parameters.values(), dtype=float)
        energy = c_double(0.)
        gradient = np.zeros((3, natoms), order="F")

        args = [
            c_int(natoms),
            positions,
            numbers,
            _parameters,
            c_int(version),
            energy,
            gradient,
        ]

        self.library.dftd3_dispersion(*args)

        return energy.value, gradient
