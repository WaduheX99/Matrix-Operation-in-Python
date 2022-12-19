MAX = 5

# Fungsi mencetak matrix
def tampilMatrix(matrix, jumlahBaris, jumlahKolom) :
    for i in range(jumlahBaris) :
        for j in range(jumlahKolom) :
            print(matrix[i][j], end = " ")
 
        print()

# Menginputkan matrix
masuk = False
masuk2 = False
while not masuk :
    if __name__ == "__main__" :
        
        A = [[0 for i in range(MAX)]
                for j in range(MAX)]
        B = [[0 for i in range(MAX)]
                for j in range(MAX)]
        
        # Memasukkan jumlah dimensi matrix A
        baris1 = int(input("Masukkan jumlah baris matrix pertama : "))
        kolom1 = int(input("Masukkan jumlah kolom matrix pertama : "))
        
        # Mengecek batas ordo matrix A yang dapat diinputkan
        if baris1 > 5 or kolom1 > 5 :
            print(" ")
            print("Maaf batas ordo matrix yang anda masukkan telah melewati batas!")
            print("Max ordo = 5 x 5 \n")
            
        else :
            # Memasukkan elemen" matrix A
            print("Masukkan elemen matrix pertama : ");
            for i in range(baris1) :
                for j in range(kolom1) :
                    A[i][j] = int(input("Matrix A[" + str(i) +"][" + str(j) + "] : "))

            while not masuk2 :
                # Memasukkan jumlah dimensi matrix B
                baris2 = int(input("Masukkan jumlah baris matrix kedua : "))
                kolom2 = int(input("Masukkan jumlah kolom matrix kedua : "))
                
                # Mengecek batas ordo matrix B yang dapat diinputkan
                if baris2 > 5 or kolom2 > 5 :
                    print("Maaf batas ordo matrix yang anda masukkan telah melewati batas!")
                    print("Max ordo = 5 x 5 \n")

                else :
                    # Memasukkan elemen" matrix B
                    print("Masukkan elemen matrix kedua : ");
                    for i in range(baris2) :
                        for j in range(kolom2) :
                            B[i][j] = int(input("Matrix B[" + str(i) +"][" + str(j) + "] : "))
                    masuk2 = True
                    masuk = True

# Fungsi Menjumlahkan matrix
def penjumlahan (baris1, kolom1, A, baris2, kolom2, B) :
    C = [[0 for i in range(MAX)]
            for j in range(MAX)]

    # Mengecek apakah matrix bisa dijumlahkan
    if baris1 != baris2 or kolom1 != kolom2 :
        print("Operasi tidak dapat dilakukan")
        print("Karena kedua Matrix memiliki ordo yang berbeda")
        return

    for i in range (baris1) :
        ## Loop Kolom
        for j in range (kolom2) :
            C[i][j] = A[i][j] + B[i][j]

    # Mencetak hasil
    print("Hasil penjumlahan : ")
    tampilMatrix(C, baris1, kolom2)

# Fungsi mengurangkan matrix
def pengurangan (baris1, kolom1, A, baris2, kolom2, B) :
    C = [[0 for i in range(MAX)]
            for j in range(MAX)]

    # Mengecek apakah matrix bisa dikurangkan
    if baris1 != baris2 or kolom1 != kolom2 :
        print("Operasi tidak dapat dilakukan")
        print("Karena kedua Matrix memiliki ordo yang berbeda")
        return

    for i in range (baris1) :
        ## Loop Kolom
        for j in range (kolom2) :
            C[i][j] = A[i][j] - B[i][j]

    # Mencetak hasil
    print("Hasil pengurangan : ")
    tampilMatrix(C, baris1, kolom2)

# Fungsi mengalikan matrix
def perkalian(baris1, kolom1, A, baris2, kolom2, B) :
                         
    # Matrix kosong untuk mencetak hasil
    C = [[0 for i in range(MAX)]
            for j in range(MAX)]
 
    # Mengecek apakah matrix bisa dikalikan
    if baris2 != kolom1 :
        print("Operasi tidak dapat dilakukan")
        print("Karena Baris pada Matrix kedua != Kolom Matrix pertama")
        return
     
    # Mengalikan 2 Matrix
    for i in range(baris1) :
        for j in range(kolom2) :
            C[i][j] = 0
            for k in range(baris2) :
                C[i][j] += A[i][k] * B[k][j];
 
    # Mencetak hasil
    print("Hasil perkalian : ")
    tampilMatrix(C, baris1, kolom2)

# Fungsi Mentransposekan matrix
def transpose(matrix, jumlahBaris, jumlahKolom) :
    result = [[0 for x1 in range(jumlahBaris)] for y1 in range(jumlahKolom)]

    for i in range(jumlahBaris):
        for j in range(jumlahKolom):
            result[j][i] = matrix[i][j]

    # Mencetak hasil
    print("Hasil Transpose : ")
    for r in result:
        print(r)

## Masuk Ke MENU
selesai = False

while not selesai :
    print(" ")
    print("====== PROGRAM MATRIX 3X3 ======")
    print("| 1. Penjumlahan               | ")
    print("| 2. Pengurangan               | ")
    print("| 3. Perkalian                 | ")
    print("| 4. Transpose                 | ")
    print("| 5. Tampil Matrix             | ")
    print("| 6. Exit                      | ")
    print("================================ \n")
    print("Masukkan pilihan : \n")

    pilih = input()

    if pilih == "1" :
        print("Matrix A : ")
        tampilMatrix(A, baris1, kolom1)
        print("Matrix B : ")
        tampilMatrix(B, baris2, kolom2)
        print(" ")
        penjumlahan(baris1, kolom1, A, baris2, kolom2, B)

    elif pilih == "2" :
        print("Matrix A : ")
        tampilMatrix(A, baris1, kolom1)
        print("Matrix B : ")
        tampilMatrix(B, baris2, kolom2)
        print(" ")
        pengurangan(baris1, kolom1, A, baris2, kolom2, B)

    elif pilih == "3" :
        print("Matrix A : ")
        tampilMatrix(A, baris1, kolom1)
        print("Matrix B : ")
        tampilMatrix(B, baris2, kolom2)
        print(" ")
        perkalian(baris1, kolom1, A, baris2, kolom2, B)

    elif pilih == "4" :
        print("======== PILIH TRANSPOSE ========")
        print("| 1. Matrix A                   | ")
        print("| 2. Matrix B                   | ")
        print("================================= \n")
        pilih2 = input()

        if pilih2 == "1" :
            print("Matrix A : ")
            tampilMatrix(A, baris1, kolom1)
            print(" ")
            transpose(A, baris1, kolom1)
        
        elif pilih2 == "2" :
            print("Matrix B : ")
            tampilMatrix(B, baris2, kolom2)
            print(" ")
            transpose(B, baris2, kolom2)

        else : 
            print("Maaf, opsi yang Anda masukkan tidak valid")

    elif pilih == "5" :
        # Mencetak matrix A
        print("Matrix A : ")
        tampilMatrix(A, baris1, kolom1)
    
        # Mencetak matrix B
        print("Matrix B : ")
        tampilMatrix(B, baris2, kolom2)
    
    elif pilih == "6" :
        print("Keluar Program")
        selesai = True

    else : 
        print("Maaf, opsi yang Anda masukkan tidak valid")