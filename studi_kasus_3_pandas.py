"""
STUDI KASUS 3: PENGOLAHAN DATASET MAHASISWA MENGGUNAKAN PANDAS
Data tidak hanya berupa angka, tetapi juga nama dan atribut lain.
Menggunakan Pandas untuk menampilkan data dengan struktur yang lebih fleksibel.
"""

import pandas as pd

# A. Series Nilai UAS
print("===== A. SERIES NILAI UAS =====")
nilai_uas = pd.Series(
    [90, 80, 95, 70, 80],
    index=["Andi", "Budi", "Citra", "Deni", "Eka"]
)

print(nilai_uas)
print("\nRata-rata :", nilai_uas.mean())
print("Tertinggi :", nilai_uas.max())
print("Terendah  :", nilai_uas.min())

# B. DataFrame Nilai Mahasiswa
print("\n===== B. DATAFRAME NILAI MAHASISWA =====")
data = {
    "Nama": ["Andi", "Budi", "Citra", "Deni", "Eka"],
    "Tugas": [85, 75, 90, 70, 80],
    "UTS": [80, 70, 85, 75, 85],
    "UAS": [90, 80, 95, 70, 80]
}

df = pd.DataFrame(data)

print(df)
print("\nNama Kolom:")
print(df.columns)
print("\nRata-rata Tugas  :", df["Tugas"].mean())
print("Rata-rata UTS    :", df["UTS"].mean())
print("Rata-rata UAS    :", df["UAS"].mean())

# C. Dataset CSV
print("\n===== C. MEMBACA DATASET CSV =====")
print("Membaca file CSV: ../data/nilai_mahasiswa.csv")
print("(Jika file ada, berikut adalah hasil pembacaannya)\n")

# Simulasi membaca CSV
df_csv = pd.read_csv("nilai_mahasiswa.csv", sep=";")

print("===== MENAMPILKAN DATA =====")
print(df_csv)

print("\n===== INFORMASI DATASET =====")
print(df_csv.info())

print("\n===== STATISTIK =====")
print(df_csv.describe())

print("\n===== ANALISIS SEDERHANA =====")
print("Rata-rata Tugas  :", df_csv["Tugas"].mean())
print("Rata-rata UTS    :", df_csv["UTS"].mean())
print("Rata-rata UAS    :", df_csv["UAS"].mean())

# TUGAS PERCOBAAN: Tambahkan 3 mahasiswa baru
print("\n===== TUGAS PERCOBAAN: TAMBAHKAN 3 MAHASISWA BARU =====")
data_baru = {
    "Nama": ["Fajar", "Gita", "Hendra"],
    "Tugas": [88, 92, 78],
    "UTS": [82, 87, 79],
    "UAS": [91, 85, 82]
}

df_baru = pd.DataFrame(data_baru)
df_lengkap = pd.concat([df_csv, df_baru], ignore_index=True)

print("Data Lengkap (8 mahasiswa):")
print(df_lengkap)

print("\nRata-rata per komponen (data lengkap):")
print("Rata-rata Tugas  :", df_lengkap["Tugas"].mean())
print("Rata-rata UTS    :", df_lengkap["UTS"].mean())
print("Rata-rata UAS    :", df_lengkap["UAS"].mean())

print("\nSimpan hasil ke CSV baru:")
print("df_lengkap.to_csv('nilai_mahasiswa_lengkap.csv', index=False)")
