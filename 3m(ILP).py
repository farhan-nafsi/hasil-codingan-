import numpy as np
from scipy.optimize import linprog
import matplotlib.pyplot as plt

# Data from the table
pesanan = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
waktu_produksi = [5, 10, 3, 4, 8, 7, 6, 9, 5, 6]  # Waktu produksi setiap pesanan
n = len(pesanan)

# Variables: start times and completion times
# We will have n variables for start times and n variables for completion times, making 2*n total variables
# x = [C1, C2, ..., Cn, s1, s2, ..., sn]

# Objective function coefficients: Minimize the sum of completion times
c = np.concatenate([np.ones(n), np.zeros(n)])

# Equality constraints: Completion time should equal start time plus processing time
A_eq = np.zeros((n, 2 * n))
b_eq = np.zeros(n)

for i in range(n):
    A_eq[i, i] = 1        # Coefficient for Ci
    A_eq[i, n + i] = -1   # Coefficient for si
    b_eq[i] = waktu_produksi[i]

# Inequality constraints: Next job's start time should be greater than or equal to the previous job's completion time
A_ub = np.zeros((n - 1, 2 * n))
b_ub = np.zeros(n - 1)

for i in range(n - 1):
    A_ub[i, n + i + 1] = 1    # Coefficient for s[i+1]
    A_ub[i, i] = -1           # Coefficient for C[i]

# Bounds for each variable
# Completion times (C) and start times (s) must be non-negative
bounds = [(0, None)] * (2 * n)

# Solve the ILP problem using SciPy's linprog function
result = linprog(c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq, bounds=bounds, method='highs')

# Check if the problem has a feasible solution
if result.success:
    # Extract completion times and start times from the result
    completion_times = result.x[:n]
    start_times = result.x[n:]
    
    # Display the results
    print("Pesanan | Waktu Produksi | Start Time | Completion Time")
    for i in range(n):
        print(f"{pesanan[i]:>7} | {waktu_produksi[i]:>14} | {start_times[i]:>10.2f} | {completion_times[i]:>15.2f}")
    
    # Total completion time
    total_completion_time = np.sum(completion_times)
    print(f"Total waktu penyelesaian: {total_completion_time:.2f}")
else:
    print("No feasible solution found")

# Plotting the results
plt.figure(figsize=(12, 6))
plt.bar(range(1, len(pesanan) + 1), waktu_produksi, color='b', alpha=0.6, label='Waktu Produksi')
plt.plot(range(1, len(pesanan) + 1), completion_times, 'g-', marker='o', label='Waktu Penyelesaian')
plt.xlabel('Nomor Pesanan')
plt.ylabel('Jam')
plt.title('Penjadwalan dengan Metode Integer Linear Programming (ILP)')
plt.legend()
plt.xticks(range(1, len(pesanan) + 1), pesanan)
plt.show()
