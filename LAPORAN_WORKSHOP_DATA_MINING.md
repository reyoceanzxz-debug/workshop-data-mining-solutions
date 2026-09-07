# LAPORAN WORKSHOP DATA MINING
## Studi Kasus: Analisis Nilai Mahasiswa Menggunakan NumPy dan Pandas

---

### RINGKASAN EKSEKUTIF

Laporan ini mendokumentasikan solusi tiga studi kasus analisis data menggunakan Python libraries: **NumPy** dan **Pandas**. Setiap studi kasus dirancang untuk mengajarkan konsep fundamental dalam data mining dan manipulasi data.

---

## STUDI KASUS 1: ANALISIS NILAI UJIAN MENGGUNAKAN NUMPY (1D ARRAY)

### Tujuan
Menganalisis data nilai UTS 10 mahasiswa untuk menentukan:
- Jumlah data
- Rata-rata kelas
- Nilai tertinggi
- Nilai terendah

### Data Input
| Nilai UTS |
|-----------|
| 80, 75, 90, 65, 85, 70, 95, 78, 88, 72 |

### Hasil Analisis
| Metrik | Nilai |
|--------|-------|
| Jumlah Data | 10 |
| Rata-rata | 79.8 |
| Nilai Tertinggi | 95 |
| Nilai Terendah | 65 |

### Tugas Percobaan
Tambahkan 5 data nilai baru: 92, 87, 76, 89, 83

**Hasil dengan Data Baru (15 mahasiswa):**
| Metrik | Nilai |
|--------|-------|
| Jumlah Data | 15 |
| Rata-rata | 82.2 |
| Nilai Tertinggi | 95 |
| Nilai Terendah | 65 |

### Konsep Kunci NumPy
- **Array 1D**: Struktur data linear untuk menyimpan urutan nilai
- **np.mean()**: Menghitung rata-rata
- **np.max()**: Mencari nilai maksimum
- **np.min()**: Mencari nilai minimum
- **np.append()**: Menambahkan elemen ke array

---

## STUDI KASUS 2: PENGOLAHAN NILAI MAHASISWA MENGGUNAKAN NUMPY (2D ARRAY)

### Tujuan
Menganalisis data nilai mahasiswa yang terdiri dari tiga komponen (Tugas, UTS, UAS) untuk mencari statistik per komponen.

### Data Input (5 Mahasiswa)
| Mahasiswa | Tugas | UTS | UAS |
|-----------|-------|-----|-----|
| Andi | 85 | 80 | 90 |
| Budi | 75 | 70 | 80 |
| Citra | 90 | 85 | 95 |
| Deni | 70 | 75 | 70 |
| Eka | 80 | 85 | 80 |

### Hasil Analisis per Komponen
| Komponen | Rata-rata | Tertinggi | Terendah |
|----------|-----------|-----------|----------|
| Tugas | 80 | 90 | 70 |
| UTS | 79 | 85 | 70 |
| UAS | 83 | 95 | 70 |

### Tugas Percobaan
Tambahkan 3 mahasiswa baru: Fajar (88,82,91), Gita (92,87,85), Hendra (78,79,82)

**Hasil dengan Data Lengkap (8 mahasiswa):**
| Komponen | Rata-rata |
|----------|-----------|
| Tugas | 82.625 |
| UTS | 80.875 |
| UAS | 83.625 |

### Konsep Kunci NumPy
- **Array 2D**: Struktur data untuk matriks (baris dan kolom)
- **Slicing kolom**: `nilai[:, 0]` untuk mengakses komponen tertentu
- **Slicing baris**: `nilai[0]` untuk mengakses data mahasiswa tertentu
- **np.vstack()**: Menggabungkan array secara vertikal

---

## STUDI KASUS 3: PENGOLAHAN DATASET MAHASISWA MENGGUNAKAN PANDAS

### Tujuan
Mengelola data yang lebih kompleks dengan nama kolom dan baris yang berlabel menggunakan Pandas Series dan DataFrame.

### A. Pandas Series (Nilai UAS)
```
Andi      90
Budi      80
Citra     95
Deni      70
Eka       80
```

**Statistik:**
- Rata-rata: 83
- Tertinggi: 95
- Terendah: 70

### B. Pandas DataFrame (Nilai Mahasiswa)
| Nama | Tugas | UTS | UAS |
|------|-------|-----|-----|
| Andi | 85 | 80 | 90 |
| Budi | 75 | 70 | 80 |
| Citra | 90 | 85 | 95 |
| Deni | 70 | 75 | 70 |
| Eka | 80 | 85 | 80 |

**Statistik:**
| Komponen | Rata-rata |
|----------|-----------|
| Tugas | 80 |
| UTS | 79 |
| UAS | 83 |

### C. Dataset CSV
Format file: `nilai_mahasiswa.csv`
```
NIM;Nama;Kelas;Tugas;UTS;UAS
E31260001;Andi;A;85;80;90
E31260002;Budi;A;75;70;80
E31260003;Citra;B;90;85;95
E31260004;Deni;B;70;75;70
E31260005;Eka;A;80;85;80
```

### Tugas Percobaan
Tambahkan 3 mahasiswa baru ke dataset

**Hasil dengan Data Lengkap (8 mahasiswa):**
| Komponen | Rata-rata |
|----------|-----------|
| Tugas | 82.625 |
| UTS | 80.875 |
| UAS | 83.625 |

### Konsep Kunci Pandas
- **Series**: Array 1D berlabel dengan index
- **DataFrame**: Tabel 2D dengan kolom bernama
- **pd.read_csv()**: Membaca data dari file CSV
- **df.describe()**: Statistik deskriptif otomatis
- **pd.concat()**: Menggabungkan DataFrame
- **df.to_csv()**: Menyimpan data ke CSV

---

## PERBANDINGAN NUMPY vs PANDAS

| Aspek | NumPy | Pandas |
|-------|-------|--------|
| Dimensi | 1D, 2D, N-D | 1D (Series), 2D (DataFrame) |
| Label | Tidak ada | Ada (index, columns) |
| Tipe Data | Homogen | Heterogen |
| Input/Output | Limited | CSV, Excel, SQL, JSON |
| Statistik | Dasar | Lengkap & Otomatis |
| Kegunaan | Komputasi numerik | Analisis data |

---

## KESIMPULAN

1. **NumPy** ideal untuk operasi numerik cepat pada array multidimensi
2. **Pandas** lebih fleksibel untuk data yang kompleks dengan kolom berlabel
3. Kedua library saling melengkapi dalam data mining workflow
4. Pandas built on top of NumPy, memberikan antarmuka yang lebih user-friendly

---

## FILE YANG DISERTAKAN

1. `studi_kasus_1_numpy_1d.py` - Solusi Studi Kasus 1 (NumPy 1D)
2. `studi_kasus_2_numpy_2d.py` - Solusi Studi Kasus 2 (NumPy 2D)
3. `studi_kasus_3_pandas.py` - Solusi Studi Kasus 3 (Pandas)
4. `nilai_mahasiswa.csv` - Dataset CSV untuk Studi Kasus 3

---

**Repository**: https://github.com/reyoceanzxz-debug/workshop-data-mining-solutions

**Tanggal Laporan**: September 2026

**Status**: Selesai ✓
