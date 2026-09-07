"""
STUDI KASUS 1: ANALISIS NILAI UJIAN MENGGUNAKAN NUMPY (1D ARRAY)
Dosen ingin mengetahui jumlah data, rata-rata kelas, nilai tertinggi, dan nilai terendah
dari data nilai UTS 10 mahasiswa.
"""

import numpy as np

# Data nilai UTS mahasiswa
nilai_uts = np.array([80, 75, 90, 65, 85, 70, 95, 78, 88, 72])

# Tampilkan struktur data
print("===== HASIL STRUKTUR DATA =====")
print("Data Nilai UTS :", nilai_uts)
print("Dimensi       :", nilai_uts.ndim)
print("Shape         :", nilai_uts.shape)

# Analisis statistik
print("\n===== HASIL ANALISIS NILAI =====")
print("Jumlah Data   :", len(nilai_uts))
print("Total Nilai   :", np.sum(nilai_uts))
print("Rata-rata     :", np.mean(nilai_uts))
print("Nilai Tertinggi :", np.max(nilai_uts))
print("Nilai Terendah  :", np.min(nilai_uts))

# Tugas Percobaan: Tambahkan 5 data nilai baru
print("\n===== TUGAS PERCOBAAN: TAMBAHKAN 5 DATA NILAI BARU =====")
nilai_uts_baru = np.append(nilai_uts, [92, 87, 76, 89, 83])
print("Data Nilai Baru   :", nilai_uts_baru)
print("Jumlah Data Baru  :", len(nilai_uts_baru))
print("Rata-rata Baru    :", np.mean(nilai_uts_baru))
print("Nilai Tertinggi Baru :", np.max(nilai_uts_baru))
print("Nilai Terendah Baru  :", np.min(nilai_uts_baru))
