##########################################################################################
# Author: Jared L. Ostmeyer
# Date Started: 2020-04-18
# Purpose: Build list of mutations
# Source: https://www.ncbi.nlm.nih.gov/labs/virus/vssi
##########################################################################################

##########################################################################################
# Library
##########################################################################################

import csv
from datetime import datetime
from Bio import SeqIO
from Bio import pairwise2

##########################################################################################
# Setting
##########################################################################################

accession_ref = 'NC_045512'

##########################################################################################
# Load data
##########################################################################################

dates = {}
with open('sequences.csv', 'r') as stream:
  reader = csv.DictReader(stream, delimiter=',')
  for row in reader:
    accession = row['Accession']
    release_date = row['Release_Date']
    collection_date = row['Collection_Date']
    dates[accession] = collection_date

sequences = {}
with open('sequences.fasta', 'r') as stream:
  for record in SeqIO.parse(stream, 'fasta'):
    accession = record.name.split('.')[0]
    if accession in sequences:
      print('WARNING: Duplicate key for primary accession')
    sequences[accession] = str(record.seq)
sequence_ref = sequences[accession_ref]
del sequences[accession_ref]

##########################################################################################
# Format datetimes
##########################################################################################

datetimes = {}
for accession, date in dates.items():
  if date.count('-') > 0:
    datetimes[accession] = \
      datetime.strptime(date, '%Y-%m-%d' if date.count('-') > 1 else '%Y-%m')

##########################################################################################
# Align and find mutations
##########################################################################################

mutations = {}
for accession, sequence in sequences.items():
  if accession in dates:  # Sequence alignment is expensive, so only align sequences with dates
    pair = pairwise2.align.globalxs(
      sequence_ref, sequence,
      -2, -1, one_alignment_only=True
    )[0]
    alignment_ref = pair[0]
    alignment = pair[1]
    for i in range(len(sequence_ref)):
      symbol_ref = alignment_ref[i]
      symbol = alignment[i]
      if 'N' not in symbol_ref and 'N' not in symbol and '-' not in symbol_ref and '-' not in symbol:  # Ignore nucleotides that cannot be confidently called and gaps
        if symbol_ref != symbol:
          if accession not in mutations:
            mutations[accession] = []
          mutation = symbol_ref+str(i)+symbol
          mutations[accession].append(mutation)

##########################################################################################
# Sort mutations by date
##########################################################################################

mutations_accession = {}
mutations_date = {}
mutations_datetime = {}
for accession in sorted(datetimes, key=datetimes.get, reverse=True):
  if accession in mutations:
    for mutation in mutations[accession]:
      mutations_accession[mutation] = accession
      mutations_date[mutation] = dates[accession]
      mutations_datetime[mutation] = datetimes[accession]

##########################################################################################
# Save results
##########################################################################################

with open('mutations.csv', 'w') as stream:
  print('Mutation', 'Collection Date', 'Accession', file=stream, sep=',')
  for mutation in sorted(mutations_datetime, key=mutations_datetime.get):
    date = mutations_date[mutation]
    accession = mutations_accession[mutation]
    print(mutation, date, accession, file=stream, sep=',')
