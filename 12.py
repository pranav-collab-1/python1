length = float(input("Enter classroom length in metres: "))
breadth = float(input("Enter classroom breadth in metres: "))
cost_per_square_metre = float(
 input("Enter flooring cost per square metre: ")
)
area = length * breadth
perimeter = 2 * (length + breadth)
total_flooring_cost = area * cost_per_square_metre
print("\n----- ROOM CALCULATION -----")
print(f"Area = {area:.2f} square metres")
print(f"Perimeter = {perimeter:.2f} metres")
print(f"Total Flooring Cost = Rs. {total_flooring_cost:.2f}")
