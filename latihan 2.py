data_mahasiswa = []

while True:
    print("\nMasukkan Data Mahasiswa")
    nama = input("Nama mahasiswa: ")
    tugas = float(input("Nilai Tugas (30%): "))
    uts = float(input("Nilai UTS (35%): "))
    uas = float(input("Nilai UAS (35%): "))

    nilai_akhir = (tugas * 0.30) + (uts * 0.35) + (uas * 0.35)

    data_mahasiswa.append([nama, tugas, uts, uas, nilai_akhir])

    tambah = input("Tambah data lagi? (y/t): ").lower()
    if tambah == 't':
        break

print("\nDaftar Nilai Mahasiswa")
print("="*60)
print(f"{'No':<4}{'Nama':<15}{'Tugas':<10}{'UTS':<10}{'UAS':<10}{'Akhir':<10}")
print("-"*60)
no = 1
for mhs in data_mahasiswa:
    print(f"{no:<4}{mhs[0]:<15}{mhs[1]:<10}{mhs[2]:<10}{mhs[3]:<10}{mhs[4]:<10.2f}")
    no += 1
print("="*60)
