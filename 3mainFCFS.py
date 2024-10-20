import matplotlib.pyplot as plt

# Data from the table
pesanan = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
waktu_produksi = [5, 10, 3, 4, 8, 7, 6, 9, 5, 6]  # Waktu produksi setiap pesanan
deadline = [40, 60, 50, 30, 55, 70, 80, 90, 100, 100]  # Tenggat waktu setiap pesanan

# Initialize start and completion times for each order
start_times = [0] * len(pesanan)
completion_times = [0] * len(pesanan)

# Calculate start and completion times based on FCFS order
for i in range(len(pesanan)):
    if i == 0:
        start_times[i] = 0  # First order starts at time 0
    else:
        start_times[i] = completion_times[i - 1]  # Next order starts after the previous one finishes
    completion_times[i] = start_times[i] + waktu_produksi[i]

# Display the results
print("Pesanan | Waktu Produksi | Start Time | Completion Time | Deadline")
for i in range(len(pesanan)):
    print(f"{pesanan[i]:>7} | {waktu_produksi[i]:>14} | {start_times[i]:>10} | {completion_times[i]:>15} | {deadline[i]:>8}")

# Plotting the results
plt.figure(figsize=(12, 6))
plt.bar(range(1, len(pesanan) + 1), waktu_produksi, color='b', alpha=0.6, label='Waktu Produksi')
plt.plot(range(1, len(pesanan) + 1), deadline, 'r--', label='Tenggat Waktu')
plt.plot(range(1, len(pesanan) + 1), completion_times, 'g-', marker='o', label='Waktu Penyelesaian')
plt.xlabel('Nomor Pesanan')
plt.ylabel('Jam')
plt.title('Penjadwalan dengan Metode First Come, First Serve (FCFS)')
plt.legend()
plt.xticks(range(1, len(pesanan) + 1), pesanan)
plt.show()
