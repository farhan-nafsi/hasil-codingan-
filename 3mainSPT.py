import matplotlib.pyplot as plt

# Data from the table
pesanan = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
waktu_produksi = [5, 10, 3, 4, 8, 7, 6, 9, 5, 6]  # Waktu produksi setiap pesanan
deadline = [40, 60, 50, 30, 55, 70, 80, 90, 100, 100]  # Tenggat waktu setiap pesanan

# Sort jobs by the shortest processing time first
sorted_indices = sorted(range(len(waktu_produksi)), key=lambda k: waktu_produksi[k])
sorted_pesanan = [pesanan[i] for i in sorted_indices]
sorted_waktu_produksi = [waktu_produksi[i] for i in sorted_indices]
sorted_deadline = [deadline[i] for i in sorted_indices]

# Calculate start and completion times
start_times = [0] * len(sorted_pesanan)
completion_times = [0] * len(sorted_pesanan)

for i in range(len(sorted_pesanan)):
    if i == 0:
        start_times[i] = 0
    else:
        start_times[i] = completion_times[i - 1]
    completion_times[i] = start_times[i] + sorted_waktu_produksi[i]

# Display the results
print("Pesanan (sorted by SPT) | Waktu Produksi | Start Time | Completion Time | Deadline")
for i in range(len(sorted_pesanan)):
    print(f"{sorted_pesanan[i]:>19} | {sorted_waktu_produksi[i]:>14} | {start_times[i]:>10} | {completion_times[i]:>15} | {sorted_deadline[i]:>8}")

# Plotting the results
plt.figure(figsize=(12, 6))
plt.bar(range(1, len(sorted_pesanan) + 1), sorted_waktu_produksi, color='b', alpha=0.6, label='Waktu Produksi')
plt.plot(range(1, len(sorted_pesanan) + 1), sorted_deadline, 'r--', label='Tenggat Waktu')
plt.plot(range(1, len(sorted_pesanan) + 1), completion_times, 'g-', marker='o', label='Waktu Penyelesaian')
plt.xlabel('Nomor Pesanan (sorted by SPT)')
plt.ylabel('Jam')
plt.title('Penjadwalan dengan Metode Shortest Processing Time First (SPT)')
plt.legend()
plt.xticks(range(1, len(sorted_pesanan) + 1), sorted_pesanan)
plt.show()
