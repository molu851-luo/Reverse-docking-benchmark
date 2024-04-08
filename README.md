# AF2 Human Proteome Binding Site Predictions with PointSite

This repository contains binding site predictions for the human proteome as determined by PointSite, utilizing the AlphaFold2 (AF2) structural models. The predictions are part of a reverse docking benchmark test and are valuable for understanding protein-ligand interactions at a proteomic scale.

## Dataset Overview

The initial dataset consisted of 20,504 protein structures, each associated with a unique UniProt ID. To ensure quality, structures with disordered regions or those lacking defined ligand-binding pockets were excluded. The refined dataset comprises 12,195 high-quality protein structures.

- Folder containing predicted binding site information: `HumanProteome-AF2-PointSite-BindPredict`
- List of retained UniProt IDs: `Protein_Uniprot_ID.txt`

## Reverse Docking Pipeline

For reverse docking analyses involving Glide, the `XDock` tool was employed. The `XDock` script facilitates the setup and execution of Glide docking runs and can be found within this repository:

- [XDock Tool](https://github.com/Wang-Lin-boop/Schrodinger-Script/blob/main/XDock)

## Reference and Additional Information

For comprehensive details regarding the methodology, results, and implications of this project, please consult our preprint:

- [Benchmarking Reverse Docking through AlphaFold2 Human Proteome](https://www.biorxiv.org/content/10.1101/2023.12.16.572027v1.full)

## Contact

For inquiries or assistance regarding this dataset, please reach out to:

- Email: jguo@mpu.edu.mo 
- Institution: Centre in Artificial Intelligence Driven Drug Discovery, Faculty of Applied Sciences, Macao Polytechnic University, Macao

