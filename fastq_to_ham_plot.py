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
        lastLen = len(seq)
    return validatedSeqs
        
def hamDist(str1, str2):
   #Count the # of differences between equal length strings str1 and str2
   diffs = 0
   return diffs

#Make some kind of plot that contains the data you've calculated.
plt.show()

