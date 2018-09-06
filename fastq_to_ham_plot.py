# Import a FASTQ file, calculate the hamming distances for each sequence,
# and plot these distances in a way you think is useful.

# Script must ultimately be contained in one fluid .py file merged via GitHub

import sys
import matplotlib.pyplot as plt

def getSeqs(fastq_file):
    #Parse a FASTQ for sequence identities and corresponding sequences
    #Output is a list of same-length FASTQ files with only characters
    #ACTGN.
    sequences = []
    seqIdRead = False
    for line in open(fastq_file): 
        # Read in FASTQ lines. Sequence lines (all we need for now) are
        # the lines that follow sequence identifier lines starting with
        # an "@" symbol. Ignore everything else.
        if seqIdRead == True and line[0] != "@":
            # There's one case of two sequence headers in a row...
            seq = line.rstrip()
            sequences.append(line.rstrip())
            seqIdRead = False
        if line[0] == "@":
            seqIdRead = True
    # We're gonna make some promises about this data, so we want to make
    # sure they're true. Specifically: 1) the sequences are all the same
    # length and 2) they contain only sequence characters.
    validatedSeqs = []
    sequenceChars = ["A", "C", "G", "T", "N"]
    lastLen = None
    for seq in sequences:
        for char in seq: assert char in sequenceChars
        if lastLen != None:
            if len(seq) == lastLen: validatedSeqs.append(seq)
        else:
            validatedSeqs.append(seq)
        lastLen = len(seq)
    return validatedSeqs

def hamDist(str1, str2):
	diffs = 0

	for i in range(0, len(str1)):
		if not str1[i] == str2[i]:
			diffs += 1

	return diffs

# Running hamDist over sets of 2 lists and appending those values to a list which can be graphed
sequences = getSeqs("CTGATC.fastq")
dist = []
# comparing all to all is too many comparisons (~half a billion). We'll
# compare all to the first.
#for i in range(len(sequences)):
#    if i % 1000 == 0: print(i)
#    for j in range(i):
#        value = hamDist(sequences[i], sequences[j])
#        dist.append(value)
#print(dist)

for i in range(1, len(sequences)):
    dist.append(hamDist(sequences[0], sequences[i]))

### plots the hamming distances as a histogram




plt.hist(dist)
plt.show()
