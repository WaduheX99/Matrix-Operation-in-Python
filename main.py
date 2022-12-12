## FAZA FARESHA AFFANDI
## A11.2021.13917
## A11.43UG2

def inputMatrix1(): ## fungsi untuk menginput matrix A
    inputMatrix1.matrix1 = []
    i1 = [0] * (9)

    ## Membuat matrix kosong 3x3
    for x1 in range(3) :
        inputMatrix1.matrix1.append([])
        for y1 in range(3) :
            inputMatrix1.matrix1[x1].append(0)

    ## Menginputkan elemen" matrix
    print("Inputkan Matrix A : ")
    m = 0
    for x in range(0, 8 + 1, 1):
        print("Masukkan elemen ke - " + str(x + 1))
        i1[m] = int(input())
        m = m + 1

    ## Memasukkan elemen" yang sudah diinput ke dalam matrix kosong
    inputMatrix1.matrix1 [0][0] = i1[0]
    inputMatrix1.matrix1 [0][1] = i1[1]
    inputMatrix1.matrix1 [0][2] = i1[2]
    inputMatrix1.matrix1 [1][0] = i1[3]
    inputMatrix1.matrix1 [1][1] = i1[4]
    inputMatrix1.matrix1 [1][2] = i1[5]
    inputMatrix1.matrix1 [2][0] = i1[6]
    inputMatrix1.matrix1 [2][1] = i1[7]
    inputMatrix1.matrix1 [2][2] = i1[8]
    print(" ")


def inputMatrix2(): ## fungsi untuk menginput matrix B
    inputMatrix2.matrix2 = []
    j1 = [0] * (9)
    
    ## Membuat matrix kosong 3x3
    for x2 in range(3) :
        inputMatrix2.matrix2.append([])
        for y2 in range(3) :
            inputMatrix2.matrix2[x2].append(0)

    print("Inputkan Matrix B : ")
    n = 0
    for y in range(0, 8 + 1, 1):
        print("Masukkan elemen ke - " + str(y + 1))
        j1[n] = int(input())
        n = n + 1

    ## Memasukkan elemen" yang sudah diinput ke dalam matrix kosong
    inputMatrix2.matrix2 [0][0] = j1[0]
    inputMatrix2.matrix2 [0][1] = j1[1]
    inputMatrix2.matrix2 [0][2] = j1[2]
    inputMatrix2.matrix2 [1][0] = j1[3]
    inputMatrix2.matrix2 [1][1] = j1[4]
    inputMatrix2.matrix2 [1][2] = j1[5]
    inputMatrix2.matrix2 [2][0] = j1[6]
    inputMatrix2.matrix2 [2][1] = j1[7]
    inputMatrix2.matrix2 [2][2] = j1[8]
    print(" ")


def cetakMatrix1(): ## fungsi untuk mencetak matrix A
    print (" ")
    print ("Matrix A : \n")
    for x1 in range(3) :
        print (inputMatrix1.matrix1[x1])

    print(" ")


def cetakMatrix2(): ## fungsi untuk mencetak matrix B
    print (" ")
    print ("Matrix B : \n")
    for x2 in range(3) :
        print (inputMatrix2.matrix2[x2])

    print(" ")
    

def penjumlahan(): ## fungsi operasi penjumlahan matrix

    result = [[0,0,0],
            [0,0,0],
            [0,0,0]]

    ## Loop baris
    for i in range (0, len(inputMatrix1.matrix1)) :
        ## Loop Kolom
        for j in range (0, len(inputMatrix2.matrix2)) :
            result[i][j] = inputMatrix1.matrix1[i][j] + inputMatrix2.matrix2[i][j]
            
    print("Hasil Penjumlahan Matrix : ")

    for r in result :
        print(r)


def perkalian(): ## fungsi operasi perkalian matrix

    result = [[0,0,0],
            [0,0,0],
            [0,0,0]]

    ## Loop baris
    for i in range (len(inputMatrix1.matrix1)) :
        ## Loop Kolom
        for j in range (len(inputMatrix2.matrix2)) :
            ## Loop perkalian
            for k in range (len(inputMatrix2.matrix2)) :
                result[i][j] += inputMatrix1.matrix1[i][k]*inputMatrix2.matrix2[k][j]

    for r in result :
        print(r)

def determinan(): ## fungsi operasi determinan matrix
    operasi = [0] * (3)
    dt = 0
    operasi[0] = inputMatrix1.matrix1[0][0] * (inputMatrix1.matrix1[1][1] * inputMatrix1.matrix1[2][2] - inputMatrix1.matrix1[2][1] * inputMatrix1.matrix1[1][2])
    operasi[1] = inputMatrix1.matrix1[0][1] * (inputMatrix1.matrix1[1][0] * inputMatrix1.matrix1[2][2] - inputMatrix1.matrix1[2][0] * inputMatrix1.matrix1[1][2])
    operasi[2] = inputMatrix1.matrix1[0][2] * (inputMatrix1.matrix1[1][0] * inputMatrix1.matrix1[2][1] - inputMatrix1.matrix1[2][0] * inputMatrix1.matrix1[1][1])
    dt = operasi[0] - operasi[1] + operasi[2]
    ## Output jawaban determinan
    print (" ")
    print ("Hasil determinan matrix A : ")
    print (dt)


def transpose(): ## fungsi operasi transpose matrix

    result = [[0,0,0],
            [0,0,0],
            [0,0,0]]

    for i in range(len(inputMatrix1.matrix1)):
        for j in range(len(inputMatrix1.matrix1[0])):
            result[j][i] = inputMatrix1.matrix1[i][j]

    print("Hasil transpose Matrix A : ")
    for r in result :
        print (r)


## Masuk Ke MENU
print("====== PROGRAM MATRIX 3X3 ======")
print("| 1. Penjumlahan               | ")
print("| 2. Perkalian                 | ")
print("| 3. Determinan                | ")
print("| 4. Transpose                 | ")
print("| 5. Exit                      | ")
print("================================ \n")
print("Masukkan pilihan : \n")

pilih = int(input())

if pilih == 1 :
    inputMatrix1()
    inputMatrix2()
    cetakMatrix1()
    cetakMatrix2()
    penjumlahan()

elif pilih == 2 :
    inputMatrix1()
    inputMatrix2()
    cetakMatrix1()
    cetakMatrix2()
    perkalian()

elif pilih == 3 :
    inputMatrix1()
    cetakMatrix1()
    determinan()

elif pilih == 4 :
    inputMatrix1()
    cetakMatrix1()
    transpose()

elif pilih == 5 :
    quit()

else : 
    print("tak valid")

