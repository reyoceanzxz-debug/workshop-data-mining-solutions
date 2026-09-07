"""
STUDI KASUS 2: PENGOLAHAN NILAI MAHASISWA MENGGUNAKAN NUMPY (2D ARRAY)
Data nilai mahasiswa terdiri dari tiga komponen: Tugas, UTS, dan UAS.
Tentukan rata-rata, nilai tertinggi, dan nilai terendah untuk setiap komponen.
"""

import numpy as np

# Data nilai mahasiswa (2D Array)
# Baris: Mahasiswa, Kolom: Tugas, UTS, UAS
nilai = np.array([
    [85, 80, 90],  # Andi
    [75, 70, 80],  # Budi
    [90, 85, 95],  # Citra
    [70, 75, 70],  # Deni
    [80, 85, 80]   # Eka
])

# Nama mahasiswa
mahasiswa = ["Andi", "Budi", "Citra", "Deni", "Eka"]
komponen = ["Tugas", "UTS", "UAS"]

# Tampilkan struktur data
print("===== STRUKTUR ARRAY =====")
print("Dimensi  :", nilai.ndim)
print("Shape    :", nilai.shape)
print("\nData Nilai Mahasiswa:")
print(nilai)

# Percobaan akses data
print("\n===== PERCOBAAN AKSES DATA =====")
print("Nilai mahasiswa pertama (Andi)      :", nilai[0])      # Baris pertama
print("Nilai UAS mahasiswa pertama         :", nilai[0][2])   # Nilai UAS Andi
print("Nilai Tugas semua mahasiswa         :", nilai[:, 0])   # Kolom pertama (Tugas)

# Statistik per komponen
print("\n===== STATISITIK =====")
print("Rata-rata Tugas  :", np.mean(nilai[:, 0]))
print("Tertinggi Tugas  :", np.max(nilai[:, 0]))
print("Terendah Tugas   :", np.min(nilai[:, 0]))

print("\nRata-rata UTS    :", np.mean(nilai[:, 1]))
print("Tertinggi UTS    :", np.max(nilai[:, 1]))
print("Terendah UTS     :", np.min(nilai[:, 1]))

print("\nRata-rata UAS    :", np.mean(nilai[:, 2]))
print("Tertinggi UAS    :", np.max(nilai[:, 2]))
print("Terendah UAS     :", np.min(nilai[:, 2]))

# Tugas Percobaan: Tambahkan 3 mahasiswa baru
print("\n===== TUGAS PERCOBAAN: TAMBAHKAN 3 MAHASISWA BARU =====")
nilai_baru = np.array([
    [88, 82, 91],  # Fajar
    [92, 87, 85],  # Gita
    [78, 79, 82]   # Hendra
])
nilai_lengkap = np.vstack([nilai, nilai_baru])
print("Data Nilai Lengkap:")
print(nilai_lengkap)

print("\nRata-rata per komponen (data lengkap):")
print("Rata-rata Tugas  :", np.mean(nilai_lengkap[:, 0]))
print("Rata-rata UTS    :", np.mean(nilai_lengkap[:, 1]))
print("Rata-rata UAS    :", np.mean(nilai_lengkap[:, 2]))
