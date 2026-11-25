# Cu-MOF modified PEO-LiTFSI simulation data

Dataset for *Atomistic description of competitive interfacial effects in Cu-MOF modified PEO-LiTFSI composites*.

[Download the dataset](md_simu4data.xlsx)

## Organization

The workbook contains numerical data organized by system and calculation method. Each worksheet starts with a single header row containing quantity names and units. Tables for different quantities are placed side by side, separated by a blank column. Read each table using its own coordinate and replica columns. Replica labels identify independent simulation runs.

| Worksheets | Data |
|---|---|
| MD01_PL to MD29_r0.10, MD_Salt_r0.02 | Ligand, temperature, PEO chain-length, Cu-BTC loading and LiTFSI concentration series. Sheet names identify the systems. |
| MD_Size143, MD_Size480 | Fragment-size models, with density, energy, MSD, RDF and coordination data. The 82-atom fragment is represented by MD02_PL-CuBTC. |
| MD_Composition | System composition, temperature, mass and charge. |
| MD_Density_Energy, MD_Interaction_Energy | Density and energy time series, component energies and intercomponent interaction energies. |
| MD_Spatial_Profiles, MD_Radius_of_Gyration | Spatial distributions and molecular/PEO-chain radii of gyration. |
| MD_Mechanics | Hill elastic moduli, stiffness, compliance and strain-fit errors. |
| MD_Collective_Transport, MD_Fit_Intervals_Duration, MD_COM_Drift | Collective MSD, NE/EH/Onsager results, fit-interval and trajectory-duration comparisons, and center-of-mass data. |
| MD_Contact_0p5ps | Contact-persistence data sampled at 0.5 ps. |
| DMol3_COMPASS | Interaction-energy scans from DMol3 and COMPASS. |
| VASP_Adsorption, VASP_PDOS | Host, TFSI and complex energies, adsorption energies, geometry and projected density of states. |
| GCMC_Adsorption | Adsorption results and framework composition. |

## Quantities and units

- Time and lag time: ps. Distance: angstrom. MSD: angstrom squared. Density: g cm^-3.
- Diffusion coefficients: m^2 s^-1. Conductivity: mS cm^-1. Elastic moduli: GPa. Energy units are specified in each column.
- MSD denotes mean-square displacement. In three dimensions, D = (1/6) d(MSD)/dt. Atomic and molecular center-of-mass (COM) quantities are identified in the column labels.
- NE denotes Nernst-Einstein conductivity. Li and TFSI contributions are distinct from total NE conductivity. EH denotes the collective Einstein-Helfand estimate. Onsager and transference-number columns retain their indicated definitions and reference frames.
- The Haven convention is H^-1 = sigma_EH/sigma_NE and H = sigma_NE/sigma_EH.
- RDF denotes the radial distribution function g(r). CN denotes the coordination number. Cutoff radii and analysis intervals are retained in the data.
- Contact probabilities and event counts use the cutoffs and sampling intervals recorded in the tables. Continuous and intermittent contact quantities are identified separately.
- Adsorption energy is E_ads = E_complex - E_host - E_TFSI. Host, isolated-ion and complex total energies are provided alongside the adsorption results.
- Blank cells indicate unavailable or inapplicable entries. Numerical zero remains zero. Source precision is retained.

## Citation and license

Please cite the manuscript above when using these data. The data are available under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

Contact: lmf844922127@gmail.com
