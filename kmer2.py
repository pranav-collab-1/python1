from collections import Counter

text =input("Enter Dna Sequence:")
k = 2


kmers = []

for i in range(len(text) - k + 1):
    kmer = text[i:i+k]
    kmers.append(kmer)

print("All k-mers:")
print(kmers)


counts = Counter(kmers)

print("\nK-mer frequencies:")
for kmer, count in counts.items():
    print(kmer, ":", count)


max_count = max(counts.values())


frequent_kmers = []

for kmer, count in counts.items():
    if count == max_count:
        frequent_kmers.append(kmer)

print("\nMost frequent k-mer(s):", frequent_kmers)
print("Number of occurrences:", max_count)
