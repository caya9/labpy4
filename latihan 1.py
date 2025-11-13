A = [10, 20, 30, 40, 50]
print("List A:", A)

print("Elemen ke-3:", A[2])

print("Elemen ke-2 sampai ke-4:", A[1:4])

print("Elemen terakhir:", A[-1])

A[3] = 100
print("Setelah ubah elemen ke-4:", A)

A[3:] = [200, 300]
print("Setelah ubah elemen ke-4 sampai terakhir:", A)

B = A[:2]
print("List B (dari 2 elemen pertama A):", B)

B.append("Python")
print("Setelah tambah string:", B)

B.extend([60, 70, 80])
print("Setelah tambah 3 nilai:", B)

gabungan = B + A
print("Gabungan list B dan A:", gabungan)
