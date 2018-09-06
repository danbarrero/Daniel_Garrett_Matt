# Import a FASTQ file, calculate the hamming distances for each sequence,
# and plot these distances in a way you think is useful.

# Script must ultimately be contained in one fluid .py file merged via GitHub

import matplotlib.pyplot as plt

f = open('CTGATC.fastq', 'r')

def getSeqs(fastq_file):
	#Parse a FASTQ for sequence identities and corresponding sequences
	seqences = {}
	return sequences
### sequences is standing in for whatever Garrett saves his sequences into
sequences = seq1, seq2, seq3
print(sequences)
### calculating Hamming distance by comparing each nucleotide in two strings
def hamDist(str1, str2):
	diffs = 0

	for i in range(0, len(str1)):
		if not str1[i] == str2[i]:
			diffs += 1

	return diffs

# Running hamDist over sets of 2 lists and appending those values to a list which can be graphed
dist = []
for i in range(len(sequences)):
	for j in range(i):
		value = hamDist(sequences[i], sequences[j])

		dist.append(value)
print(dist)

### plots the hamming distances as a histogram

plt.hist(dist)
plt.show()
