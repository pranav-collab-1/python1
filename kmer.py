from Bio.Seq import Seq

seq = Seq("ATGATGCA")
k = 3
kmers = [str(seq[i:i+k]) for i in range(len(seq) - k + 1)]
print("K-mers:", kmers)
counts = {}

for kmer in kmers:
    if kmer in counts:
        counts[kmer] += 1
    else:
        counts[kmer] = 1
print("\nK-mer frequencies:")
for kmer, count in counts.items():
    print(kmer, ":", count)
