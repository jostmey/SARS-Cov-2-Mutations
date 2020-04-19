# Repository of code for identifying and modelling mutations in the SARS-Cov-2 genome
###### JARED L OSTMEYER, ASSISTANT PROFESSOR, UT SOUTHWESTERN DEPARTMENT OF POPULATION AND DATA SCIENCES

## Rebuild Database

To rebuild the database, we need to first download available versions of the SARS-Cov-2 genome. Visit https://www.ncbi.nlm.nih.gov/labs/virus/vssi and click `Seach by virus`. In the search box type `SARS-Cov-2` and click on `taxid:2697049`. A new page will appepar with the list of genome sequences. On the left panel, locate the tab `Nucleotide Completeness` and check the box for `complete`. The list of genome sequences should automatically update, keeping on those genomes that are complete. On the top-right, click the button `Download`. You will need to download two files. First, under `Sequence data (FASTA Format)` download `Nucleotide`. Then, under `Current table view result` download `CSV format`. These downloads will result in the following two files

```
sequences.csv
sequences.fasta
```

To build the database of mutations, run the following command in the terminal. The script may take approximately an entire day to complete.

```
python3 mutations_parallel.py
```

The script save the results in a file called `mutations.csv`

## Requirements

* [Python3](https://www.python.org/)
* [Biopython version 1.7.1](https://biopython.org/)
