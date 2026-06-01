"""
racah
=====
The Racah algebra, compiled.

This package re-exports spectrafold — the Origami ISA for spectroscopy.
Install spectrafold for the full library:

    pip install spectrafold

The racah name is reserved for future use as the spectroscopy-specialised
layer of the spectrafold engine.

    from spectrafold import flop, flip, split, splat, twist

Papers: doi:10.5281/zenodo.20490046 (Paper 348, Spiders for Nuclei)
"""

try:
    from spectrafold import (
        flip, flop, split, splat, twist,
        twist_eigenvalue, wigner3j, verify_pentagon,
    )
    from spectrafold.spectroscopy.pandya import pandya_transform
    from spectrafold.spectroscopy.g2wall import g2_casimir, is_beyond_g2_wall
except ImportError:
    pass  # spectrafold not installed; install with: pip install spectrafold

__version__ = "0.1.0"
