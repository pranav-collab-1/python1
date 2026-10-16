import matplotlib.pyplot as plt

# Define the corners of the square for A, T, G, and C
corners = {
    'A': (0, 0),  # Bottom-left corner
    'T': (1, 0),  # Bottom-right corner
    'C': (0, 1),  # Top-left corner
    'G': (1, 1)   # Top-right corner
}

# Function to calculate the midpoint between two points
def midpoint(p1, p2):
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)

# Function to plot the sequence
def plot_dna_sequence(sequence):
    # Initialize the starting point as the center of the square
    center = (0, 0)
    current_point = midpoint(center, corners[sequence[0]])
    
    # Store the points for plotting
    x_points = [current_point[0]]
    y_points = [current_point[1]]
    
    # Iterate through the sequence, calculating midpoints
    for nucleotide in sequence[1:]:
        current_point = midpoint(current_point, corners[nucleotide])
        x_points.append(current_point[0])
        y_points.append(current_point[1])
        
    # Plotting
    plt.figure(figsize=(6, 6))
    plt.plot(x_points, y_points, marker='o', color='blue', linestyle='-', markersize=5)
    
    # Plot the square and label the corners
    plt.plot([0, 1, 1, 0, 0], [0, 0, 1, 1, 0], color='black') # Square outline
    for nucleotide, coord in corners.items():
        plt.text(coord[0], coord[1], nucleotide, fontsize=12, ha='center', va='center', color='red')
        
    plt.title(f"DNA Sequence Plot for '{sequence}'")
    plt.xlim(-0.1, 1.1)
    plt.ylim(-0.1, 1.1)
    plt.grid(True)
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.gca().set_aspect('equal')
    plt.show()

# Input DNA sequence
dna_sequence = "TACAGA"
plot_dna_sequence(dna_sequence)
