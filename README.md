# Repository of code for identifying and modelling mutations in the SARS-Cov-2 genome
###### JARED L OSTMEYER, ASSISTANT PROFESSOR, UT SOUTHWESTERN DEPARTMENT OF POPULATION AND DATA SCIENCES

## Rebuilding the Database

To rebuild the database, we need to first download available versions of the SARS-Cov-2 genome. Visit https://www.ncbi.nlm.nih.gov/labs/virus/vssi and click `Seach by virus`. In the search box type `SARS-Cov-2` and click on `taxid:2697049`. A new page will appepar with the list of genome sequences. On the left panel, locate the tab `Nucleotide Completeness` and check the box for `complete`. The list of genome sequences should automatically update, keeping on those genomes that are complete. On the top-right, click the button `Download`. You will need to download two files. First, under `Sequence data (FASTA Format)` download `Nucleotide`. Then, under `Current table view result` download `CSV format`. These downloads will result in the following two files

```
sequences.csv
sequences.fasta
```

To build the database of mutations, run the following command in the terminal. The script may take approximately an entire day to complete.

```
python3 mutations_parallel.py   # This script does the same computations as mutations.py distributed across multiple CPU cores
```

The script save the results in a file called `mutations.csv`

## Results

The file `mutations.csv` list the point mutations observed in the SARS-Cov-2 genome relative to the reference genome `NC_045512`. Each point mutation is represented as a symbol, a number, and another symbol. The first symbol represents the original nucleotide according to the reference genome. The number represents the position of the mutation in the reference genome. The last symbol represents the nucleotide after the mutation. Each mutation is listed with the earliest date it is observed along with the accession code indicating the genome where the mutation first occurred.

There are two limitations with this analysis. The first limitation is that our analysis excludes insertions and deletions. This is because a preliminary analysis revealed that insertions and deletions occur almost exclusively at the ends of the genome, making it unclear if these insertions and deletions are sequence artifacts or actual mutations. The other limitation is that there is no way to determine if the remaining point mutations are actual mutations or sequencing error. These limitations must be kept in mind going forward.

## Requirements

* [Python3](https://www.python.org/)
* [Biopython version 1.7.1](https://biopython.org/)
