import matplotlib.pyplot as plt

# DNA sequence
dna = "ATGCATGCAT"
k = 3

# Assign coordinates to nucleotides
corners = {
    'A': (0, 0),
    'T': (1, 0),
    'G': (1, 1),
    'C': (0, 1)
}

# Generate all 3-mers
kmers = [dna[i:i+k] for i in range(len(dna) - k + 1)]

# Calculate CGR coordinates
x_points = []
y_points = []

for kmer in kmers:
    x, y = 0.5, 0.5
    
    for base in kmer:
        cx, cy = corners[base]
        x = (x + cx) / 2
        y = (y + cy) / 2
        
    x_points.append(x)
    y_points.append(y)

# Plot CGR
plt.figure(figsize=(6, 6))
plt.scatter(x_points, y_points, color='blue', s=80)

plt.title("Chaos Game Representation of 3-mers")
plt.xlabel("X-coordinate")
plt.ylabel("Y-coordinate")
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.grid(True)
plt.show()

# Display 3-mers and coordinates
for kmer, x, y in zip(kmers, x_points, y_points):
    print(kmer, ":", (x, y))
