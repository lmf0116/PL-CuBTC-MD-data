# MD and GCMC simulation data for Cu-MOF modified PEO–LiTFSI composites

Raw simulation records for the manuscript

> **Atomistic description of competitive interfacial effects in Cu-MOF modified
> PEO-LiTFSI composites**


This repository collects the molecular-dynamics (MD) and grand canonical Monte
Carlo (GCMC) results used to build the tables and figures in the manuscript and
its Supporting Information, so that the calculations can be traced and, where
practical, reproduced.

## What is in here

```
data/
  md_simu4data.xlsx          original workbook (authoritative, human-readable layout)
  csv/                       one CSV per worksheet, flat cell-by-cell dump
    sheet01_raw-summary.csv
    sheet02_partial-atomic-charges.csv
    sheet03_gcmc-adsorption.csv
    sheet04_md-composition-linkers.csv
    sheet05_temperature-series.csv
    sheet06_chain-length-series.csv
    sheet07_salt-concentration-series.csv
    sheet08_loading-series.csv
    sheet09_mechanical-properties.csv
scripts/
  export_csv.py              regenerates data/csv/ from the .xlsx
```

The `.xlsx` workbook is the canonical record. Several worksheets hold multiple
logical sub-tables (MSD time series, RDF curves, interaction energies, system
composition) side by side, so they use stacked multi-row headers. The CSV files
are a faithful cell-by-cell dump (empty cells left empty) for anyone who wants
to load the numbers programmatically or diff them; they are **not** tidied
long-form tables.

## Worksheet map

| Worksheet (original name) | CSV file | Contents |
|---|---|---|
| Sheet1 | `sheet01_raw-summary.csv` | Scratch/summary values used to build the metal-substituted (Cu, Ni, Al, Co, Fe, Mg) and linker-functionalized (F, Cl, Br, NH₂, SH, CHO) frameworks |
| 电荷 | `sheet02_partial-atomic-charges.csv` | DFT-derived partial atomic charges for TFSI⁻ and Cu-BTC |
| PL-Cu-x吸附量 | `sheet03_gcmc-adsorption.csv` | GCMC results: average loading *N*, isosteric heat, total energy, and absolute uptake (mg/g) for pristine and modified Cu-BTC |
| PL-Cu-x系统物理组成 | `sheet04_md-composition-linkers.csv` | MD system composition, energies, MSD/diffusion, Nernst–Einstein conductivity, and RDF data for the BTC/BBC/TTCA/TATB linker comparison |
| PL-CuBTC不同温度 | `sheet05_temperature-series.csv` | Temperature series (298–410 K): MSD, density, RDF, interaction energy, mass-density profiles |
| 不同聚合度 298k 1atm | `sheet06_chain-length-series.csv` | PEO chain-length series (L = 30–200 EO units): composition, density, radius of gyration, MSD, RDF, interaction energies |
| PL-Cu-BTC不同阴离子浓度 | `sheet07_salt-concentration-series.csv` | Salt-ratio series (r = 0.02–0.10): composition, MSD, interaction energies, RDF, concentration profiles |
| PL-Cu-BTC不同CuBTC | `sheet08_loading-series.csv` | Cu-BTC loading series (1–5 clusters): composition, MSD, RDF, interaction energies, radius of gyration |
| 力学性能 | `sheet09_mechanical-properties.csv` | Mechanical properties: shear modulus, bulk modulus, and Lamé constant for the chain-length and loading series |

## Methods (summary)

- **Software.** Materials Studio 8.0; COMPASS force field for the polymer, salt,
  and MOF atoms.
- **Charges.** LiTFSI partial charges from electrostatic-potential fitting;
  framework charges from the DFT-derived parameters of Zhao et al.,
  *J. Mol. Model.* 2011, 17, 227.
- **MD.** PEO chains generated with Polymer Builder, packed with Amorphous Cell
  (periodic). Energy minimization (conjugate gradient, 2×10⁻⁵ kcal/mol), then
  NPT equilibration (Berendsen thermostat / Andersen barostat, 0.01 GPa,
  298–410 K) followed by NVT production; 1 fs time step; particle-mesh Ewald
  (1×10⁻⁴ kcal/mol); atom-based van der Waals cutoff 15.5 Å.
- **GCMC.** Fixed-pressure runs at 298 K and 1 atm; 10⁶ equilibration + 10⁷
  production cycles; atom-based vdW cutoff 12.5 Å; Ewald summation
  (1×10⁻⁴ kcal/mol).

Full details, definitions of the derived quantities (interaction energy,
Nernst–Einstein contribution, adsorption energy, absolute uptake), and the
equilibrium model parameters are in the manuscript and Supporting Information
(Tables S1–S3, Figures S1–S7).

## Citation

If you use these data, please cite the manuscript

## License

Raw simulation data are released under the
[Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/)
license — see `LICENSE`. The export script in `scripts/` is MIT-licensed.

## Contact

lmf844922127@gmail.com
