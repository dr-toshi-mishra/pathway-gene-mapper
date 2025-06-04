# Pathway Gene Mapper

## Overview

**Pathway Gene Mapper** is a Python tool designed to analyze genomic loci of pathway-related genes using *NCBI feature tables* as input. It helps researchers identify the presence, arrangement, and proximity of genes involved in specific metabolic pathways such as the **Rhamnose biosynthesis (Rml) pathway**. This tool facilitates understanding gene clustering and operon organization within prokaryotic genomes, thereby supporting studies in functional annotation, metabolic pathway completeness, and gene regulation.

---

## Features

- Parses NCBI Feature Table files (`.tbl`) for gene annotations.
- Identifies and verifies presence of pathway-specific genes.
- Determines genomic proximity of pathway genes (contiguous, neighboring, dispersed).
- Generates summary reports highlighting gene presence and clustering.
- Command-line interface for easy batch processing of multiple genomes.
- Modular Python code allowing integration with custom bioinformatics workflows.

---

## Installation

### Prerequisites

- Python 3.6 or higher
- Required Python packages: listed in `requirements.txt`

### Steps

Clone the repository:

```bash
git clone https://github.com/dr-toshi-mishra/pathway-gene-mapper.git
cd pathway-gene-mapper
````

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

### Input

Provide the path to an NCBI Feature Table file (`.tbl`) corresponding to a genome. These files can be downloaded from NCBI for various prokaryotic genomes and contain detailed gene annotation data.

### Running the tool

Use the command-line script to analyze gene presence and proximity for a specific pathway. For example, to analyze the Rml pathway genes:

```bash
python pathway_gene_mapper.py --input path/to/genome.tbl --pathway rml
```

### Output

The tool outputs:

* A summary report listing detected pathway genes and their coordinates.
* Classification of gene proximity (e.g., contiguous, neighboring, dispersed).
* Warnings if expected pathway genes are missing or fragmented.

Example console output snippet:

```
Gene rmlA found at location 1500-2300 (contiguous)
Gene rmlB found at location 2400-2800 (neighboring)
Gene rmlC not found - possible pathway incompleteness
```

---

## Python Module Usage

You can also use the functionality programmatically by importing the module:

```python
from pathway_gene_mapper import analyze_pathway

results = analyze_pathway('genome.tbl', pathway='rml')

for gene, info in results.items():
    print(f"{gene}: {info['status']} at {info['location']} ({info['proximity']})")
```

---

## Input and Output Details

### Input Format

* NCBI Feature Table file (`.tbl`), containing gene features with their coordinates and annotations.
* The tool parses CDS and gene features relevant to the specified metabolic pathway.

### Output Format

* Console printed report summarizing gene detection and proximity.
* Optional CSV/JSON summary files (feature planned for future versions).

---

## Contributing

Contributions, bug reports, and feature requests are welcome!
Please open issues or submit pull requests with descriptive messages.

---

## Contact

Developed by Dr. Toshi Mishra
GitHub: [@dr-toshi-mishra](https://github.com/dr-toshi-mishra)
---

## Acknowledgments

Thanks to the NCBI for providing accessible genome annotation data and to the open-source Python community for libraries used in this project.
