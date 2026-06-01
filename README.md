# racah

**The Racah algebra, compiled.**

This package is the spectroscopy-specialised layer of [spectrafold](https://github.com/roguetrainer/spectrafold).

```bash
pip install spectrafold   # the full library
pip install racah         # this stub (re-exports spectrafold)
```

```python
import racah

racah.flop(0, 1, 1, 1, 1, 1)    # 6j symbol {0 1 1; 1 1 1} = -1/3
racah.pandya_transform(...)       # Pandya transform as FLIP;FLOP
racah.g2_casimir(1, 0)            # G2 Casimir for the fundamental 7-dim irrep
```

All results are exact sympy expressions — no floats, no rounding.

## Papers

| Paper | DOI |
|-------|-----|
| 347 Spiders for Spectra  | [10.5281/zenodo.20458996](https://doi.org/10.5281/zenodo.20458996) |
| 348 Spiders for Nuclei   | [10.5281/zenodo.20490046](https://doi.org/10.5281/zenodo.20490046) |
| 349 The Origami Calculus | [10.5281/zenodo.20474914](https://doi.org/10.5281/zenodo.20474914) |
| 350 Spiders for Quarkonium | [10.5281/zenodo.20490294](https://doi.org/10.5281/zenodo.20490294) |

## License

MIT. Author: Ian R. C. Buckley.
