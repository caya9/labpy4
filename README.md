# LAPORAN TUGAS PRAKTIKUM 4
NAMA    : Chaya Aulia

KELAS   : TI.25.A2

NIM     : 312510197

Matkul  : Pengantar Pemrograman

# 📘 Tujuan Praktikum

-Memahami konsep dasar List pada bahasa pemrograman Python.

-Mampu mengakses, mengubah, menambah, dan menggabungkan elemen list.

-Membuat program sederhana untuk mengelola data dengan struktur list.

# 📚 Dasar Teori

List adalah salah satu tipe data di Python yang berfungsi untuk menyimpan sekumpulan data dalam satu variabel.
Ciri-ciri List:

Dapat menyimpan berbagai tipe data (angka, string, dsb).

Dapat diubah (mutable).

Elemen-elemennya diapit oleh tanda kurung siku [ ].

# LATIHAN 

```python
A = [15, 30, 45, 60, 75]
```
Elemen dapat diakses dengan indeks yang dimulai dari 0.

# 1. Buat list dengan 5 elemen
```kode program
A = [15, 30, 45, 60, 75]
print("List A:", A)
```

# 2. Akses list
```kode program
print("Elemen ke-3:", A[2])
print("Elemen ke-2 sampai ke-4:", A[1:4])
print("Elemen terakhir:", A[-1])
```

# 3. Ubah elemen list
```kode program
A[3] = 150
print("Setelah ubah elemen ke-4:", A)
A[3:] = [225, 300]
print("Setelah ubah elemen ke-4 sampai akhir:", A)
```

# 4. Tambah elemen list
```kode program
B = A[0:2]
print("List B:", B)
B.append("Python")
print("Setelah tambah string:", B)
B.extend([90, 105, 120])
print("Setelah tambah 3 nilai:", B)
C = B + A
print("Gabungan list B dan A:", C)
```
# 🧠 Analisis Program

-List A dibuat dengan lima elemen kelipatan 15.

-Elemen diakses menggunakan indeks (A[2], A[1:4], A[-1]).

-Elemen bisa diubah (mutable), contohnya A[3] = 150.

-Elemen bisa ditambah dengan .append() dan .extend().

-Dua list dapat digabungkan dengan operator +.

-Hasil akhir menunjukkan bahwa Python memungkinkan pengelolaan data dengan mudah menggunakan List.

# 🧮 Tugas Praktikum
Deskripsi:

-Buat program yang dapat menambahkan data mahasiswa ke dalam list, menghitung nilai akhir berdasarkan bobot:

Tugas: 30%

UTS: 35%

UAS: 35%

-Program berjalan terus sampai pengguna menjawab “t”.

# TUGAS PRAKTIKUM 4 - PROGRAM DATA MAHASISWA
```kode 
data_mahasiswa = []

while True:
    print("\n=== Input Data Mahasiswa ===")
    nama = input("Nama        : ")
    tugas = float(input("Nilai Tugas : "))
    uts   = float(input("Nilai UTS   : "))
    uas   = float(input("Nilai UAS   : "))
```
# Hitung nilai akhir
```
akhir = (tugas * 0.30) + (uts * 0.35) + (uas * 0.35)
```
# Simpan ke list
```
data_mahasiswa.append([nama, tugas, uts, uas, akhir])

lanjut = input("Tambah data lagi? (y/t): ")
if lanjut.lower() == 't':
  break
```
# Tampilkan hasil
```
print("\nDaftar Nilai Mahasiswa")
print("="*65)
print("| No |     Nama     | Tugas |  UTS  |  UAS  |  Akhir |")
print("-"*65)

for i, data in enumerate(data_mahasiswa, start=1):
    print(f"| {i:>2} | {data[0]:<12} | {data[1]:>5.1f} | {data[2]:>5.1f} | {data[3]:>5.1f} | {data[4]:>6.2f} |")

print("-"*65)
```
# 🔄 Flowchart Program
```pgsl
+---------------------+
| Mulai               |
+---------+-----------+
          |
          v
+---------------------+
| Input Nama, Tugas,  |
| UTS, dan UAS        |
+---------+-----------+
          |
          v
+---------------------+
| Hitung Nilai Akhir  |
| (0.3*T + 0.35*U +   |
|  0.35*A)            |
+---------+-----------+
          |
          v
+---------------------+
| Simpan ke List      |
+---------+-----------+
          |
          v
+---------------------+
| Tambah data lagi?   |
| (y/t)               |
+----+----------------+
     |y
     v
  (Kembali input)
     |
     t
     v
+---------------------+
| Tampilkan semua     |
| data mahasiswa      |
+---------+-----------+
          |
          v
+---------------------+
| Selesai             |
+---------------------+
```

# 🧾 Kesimpulan

-Dari praktikum ini dapat disimpulkan bahwa:

-List di Python memudahkan penyimpanan dan pengolahan kumpulan data.

-Elemen list bisa diubah, ditambah, bahkan digabungkan dengan list lain.

-Program sederhana dapat dibuat untuk mengelola data mahasiswa menggunakan list dan perulangan.


